#!/usr/bin/env python3
"""Generate the Mellea LinkML schema directly from the Mellea Python sources.

This script analyses the live Mellea codebase (``mellea/`` and ``cli/``) and
emits a fresh LinkML YAML schema at::

    linkml/src/mellea/schema/mellea.yaml

The architectural skeleton (subsets, slots, structural classes) is encoded in
this script.  Source-derivable pieces - namely the enum permissible values,
the list of supported backend families, and the per-package element inventory
- are re-extracted from Python sources on every run via ``ast``.  This lets the
schema track upstream code changes reproducibly: re-run the script after any
Mellea refactor and commit the regenerated YAML.

Usage::

    python3 linkml/scripts/schema_to_linkml.py
    python3 linkml/scripts/schema_to_linkml.py --repo-root /path/to/mellea
    python3 linkml/scripts/schema_to_linkml.py --out-file /tmp/mellea.yaml

Inputs (parsed):

* ``mellea/plugins/types.py``           - ``PluginMode``, ``HookType``
* ``mellea/backends/adapters/catalog.py`` - ``AdapterType``
* ``mellea/backends/*.py``              - one file per backend family
* ``mellea/**`` and ``cli/**``          - class / enum / dataclass inventory

Only the Python standard library + PyYAML (already a transitive dependency of
LinkML) are required.
"""

from __future__ import annotations

import argparse
import ast
import datetime as _dt
import sys
from collections import OrderedDict, defaultdict
from pathlib import Path
from typing import Any

import yaml


# ---------------------------------------------------------------------------
# Configuration (todo: consider https://linkml.io/valuesets/ integration)
# ---------------------------------------------------------------------------

REPO_ROOT_DEFAULT = Path(__file__).resolve().parents[2]
OUT_FILE_DEFAULT = (
    REPO_ROOT_DEFAULT / "linkml" / "src" / "mellea" / "schema" / "mellea.yaml"
)

# Top-level Python packages to scan, mapped to their PackageKindEnum bucket.
PACKAGE_KIND_MAP: dict[str, str] = {
    "mellea/core": "STDLIB",
    "mellea/stdlib": "STDLIB",
    "mellea/backends": "BACKENDS",
    "mellea/formatters": "FORMATTERS",
    "mellea/helpers": "HELPERS",
    "mellea/plugins": "PLUGINS",
    "mellea/telemetry": "TELEMETRY",
    "mellea/templates": "STDLIB",
    "cli": "CLI",
}

# Backend module filename (under mellea/backends/) -> BackendFamilyEnum value.
# Sourced from the actual backend files; non-backend helpers are excluded.
BACKEND_MODULE_TO_FAMILY: dict[str, str] = {
    "ollama": "OLLAMA",
    "huggingface": "HUGGINGFACE",
    "openai": "OPENAI",
    "watsonx": "WATSONX",
    "litellm": "LITELLM",
    "bedrock": "BEDROCK",
    "dummy": "DUMMY",
}

# Enums that cannot be source-derived 1:1 (they are descriptive metamodel
# enums).  Listed here to keep the schema self-contained.
STATIC_ENUMS: "OrderedDict[str, dict]" = OrderedDict(
    [
        (
            "PackageKindEnum",
            {
                "description": "Logical package buckets used to classify Mellea source modules.",
                "permissible_values": OrderedDict(
                    (v, {"description": v.replace("_", " ").lower()})
                    for v in [
                        "CORE",
                        "STDLIB",
                        "BACKENDS",
                        "FORMATTERS",
                        "HELPERS",
                        "PLUGINS",
                        "TELEMETRY",
                        "CLI",
                        "DOCS_EXAMPLES",
                        "TEST",
                    ]
                ),
            },
        ),
        (
            "ElementKindEnum",
            {
                "description": "Kind of Python declaration captured by a ModelElement entry.",
                "permissible_values": OrderedDict(
                    (v, {"description": v.replace("_", " ").lower()})
                    for v in [
                        "CLASS",
                        "ENUM",
                        "DATACLASS",
                        "TYPED_DICT",
                        "PYDANTIC_MODEL",
                        "PROTOCOL",
                        "FUNCTION",
                        "MIXIN",
                    ]
                ),
            },
        ),
        (
            "CoverageScopeEnum",
            {
                "description": "Where in the project an element surfaces (source, API, CLI, ...).",
                "permissible_values": OrderedDict(
                    (v, {"description": v.replace("_", " ").lower()})
                    for v in ["SOURCE", "API", "CLI", "EXAMPLE", "TEST"]
                ),
            },
        ),
        (
            "ContextLinearityEnum",
            {
                "description": "Whether a Mellea context preserves linear ordering or not.",
                "permissible_values": OrderedDict(
                    [
                        ("LINEAR", {"description": "Sequential, ordered history."}),
                        (
                            "NON_LINEAR",
                            {"description": "Tree- or graph-shaped history."},
                        ),
                    ]
                ),
            },
        ),
        (
            "ComponentCategoryEnum",
            {
                "description": "High-level category of a Mellea stdlib component.",
                "permissible_values": OrderedDict(
                    (v, {"description": v.replace("_", " ").lower()})
                    for v in [
                        "INSTRUCTION",
                        "MESSAGE",
                        "TOOL_MESSAGE",
                        "DOCUMENT",
                        "INTRINSIC",
                        "MOBJECT",
                        "QUERY",
                        "TRANSFORM",
                        "GENSTUB",
                        "REQUIREMENT",
                        "STREAM_EVENT",
                    ]
                ),
            },
        ),
        (
            "RequestResponseEnum",
            {
                "description": "Direction of a wire model (HTTP request, response, or both).",
                "permissible_values": OrderedDict(
                    [
                        ("REQUEST", {"description": "Inbound request payload."}),
                        ("RESPONSE", {"description": "Outbound response payload."}),
                        (
                            "BOTH",
                            {
                                "description": "Model used in both directions (rare)."
                            },
                        ),
                    ]
                ),
            },
        ),
    ]
)


# ---------------------------------------------------------------------------
# Naming helpers
# ---------------------------------------------------------------------------


def upper_snake(name: str) -> str:
    """Normalize a Python enum member name to LinkML UPPER_SNAKE_CASE."""
    return name.upper()


# ---------------------------------------------------------------------------
# AST-based inventory
# ---------------------------------------------------------------------------


_ENUM_BASES = {"Enum", "StrEnum", "IntEnum", "enum.Enum", "enum.StrEnum", "enum.IntEnum"}


def _base_name(b: ast.expr) -> str:
    """Return the textual name of a class base (last attribute if dotted)."""
    if isinstance(b, ast.Name):
        return b.id
    if isinstance(b, ast.Attribute):
        return f"{_base_name(b.value)}.{b.attr}"
    if isinstance(b, ast.Subscript):
        return _base_name(b.value)
    if isinstance(b, ast.Call):
        return _base_name(b.func)
    return ""


def _decorator_name(d: ast.expr) -> str:
    if isinstance(d, ast.Call):
        return _base_name(d.func)
    return _base_name(d)


def _classify(node: ast.ClassDef) -> str:
    bases = {_base_name(b) for b in node.bases}
    bases_last = {b.rsplit(".", 1)[-1] for b in bases}

    decos = {_decorator_name(d).rsplit(".", 1)[-1] for d in node.decorator_list}

    if bases_last & {"Enum", "StrEnum", "IntEnum"}:
        return "ENUM"
    if "BaseModel" in bases_last:
        return "PYDANTIC_MODEL"
    if "TypedDict" in bases_last:
        return "TYPED_DICT"
    if "Protocol" in bases_last:
        return "PROTOCOL"
    if "dataclass" in decos:
        return "DATACLASS"
    if node.name.endswith("Mixin"):
        return "MIXIN"
    return "CLASS"


def _enum_members(node: ast.ClassDef) -> list[tuple[str, str | None]]:
    """Return ``[(name, str_value_or_None), ...]`` for enum member assignments."""
    out: list[tuple[str, str | None]] = []
    for stmt in node.body:
        target = None
        value: ast.expr | None = None
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(
            stmt.targets[0], ast.Name
        ):
            target = stmt.targets[0].id
            value = stmt.value
        elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
            target = stmt.target.id
            value = stmt.value

        if not target or target.startswith("_") or target == target.lower():
            # Skip private and lower-case (likely helpers, not enum members).
            continue
        str_val: str | None = None
        if isinstance(value, ast.Constant) and isinstance(value.value, str):
            str_val = value.value
        out.append((target, str_val))
    return out


def _iter_py(root: Path, sub: str) -> list[Path]:
    base = root / sub
    if not base.is_dir():
        return []
    return sorted(
        p
        for p in base.rglob("*.py")
        if "__pycache__" not in p.parts
        and "/linkml/" not in str(p)
        and "/.venv/" not in str(p)
    )


def collect_inventory(repo_root: Path) -> dict:
    """Walk Python sources and collect per-package class + enum inventory."""
    per_package: dict[str, dict[str, list[dict]]] = defaultdict(
        lambda: defaultdict(list)
    )
    enums_by_qualified_name: dict[str, dict] = {}

    for sub, package_kind in PACKAGE_KIND_MAP.items():
        for path in _iter_py(repo_root, sub):
            try:
                tree = ast.parse(path.read_text(encoding="utf-8"))
            except SyntaxError:
                continue
            rel = path.relative_to(repo_root).as_posix()
            for node in ast.walk(tree):
                if not isinstance(node, ast.ClassDef):
                    continue
                kind = _classify(node)
                entry = {
                    "name": node.name,
                    "kind": kind,
                    "source_file": rel,
                    "package_kind": package_kind,
                }
                per_package[sub][kind].append(entry)
                if kind == "ENUM":
                    members = _enum_members(node)
                    qname = f"{rel}::{node.name}"
                    enums_by_qualified_name[qname] = {
                        "name": node.name,
                        "source_file": rel,
                        "members": members,
                    }
    return {
        "per_package": {k: dict(v) for k, v in per_package.items()},
        "enums": enums_by_qualified_name,
    }


def discover_backend_families(repo_root: Path) -> "OrderedDict[str, dict]":
    """Map filenames under ``mellea/backends/`` to BackendFamilyEnum members."""
    backends_dir = repo_root / "mellea" / "backends"
    perm: "OrderedDict[str, dict]" = OrderedDict()
    if not backends_dir.is_dir():
        return perm
    for path in sorted(backends_dir.glob("*.py")):
        stem = path.stem
        family = BACKEND_MODULE_TO_FAMILY.get(stem)
        if not family:
            continue
        perm[family] = {
            "description": f"Backend family backed by mellea/backends/{stem}.py.",
            "annotations": OrderedDict([("source_file", f"mellea/backends/{stem}.py")]),
        }
    return perm


def find_enum(inv: dict, source_file: str, name: str) -> dict | None:
    return inv["enums"].get(f"{source_file}::{name}")


def build_enum_from_source(
    enum_info: dict | None, description: str, fallback_values: list[str]
) -> dict:
    """Build a permissible-value block from extracted Python source.

    Falls back to ``fallback_values`` when the source enum cannot be found
    (e.g. file renamed) so the schema remains generatable.
    """
    perm: "OrderedDict[str, dict]" = OrderedDict()
    if enum_info and enum_info["members"]:
        for member, str_val in enum_info["members"]:
            body: dict[str, Any] = {"description": member.replace("_", " ").lower()}
            if str_val is not None:
                body["annotations"] = OrderedDict([("python_value", str_val)])
            perm[upper_snake(member)] = body
    else:
        for v in fallback_values:
            perm[upper_snake(v)] = {"description": v.replace("_", " ").lower()}
    out = {"description": description, "permissible_values": perm}
    if enum_info:
        out["annotations"] = OrderedDict(
            [("derived_from", f"{enum_info['source_file']}::{enum_info['name']}")]
        )
    return out


# ---------------------------------------------------------------------------
# Static schema scaffolding (subsets, types, slots, classes)
# ---------------------------------------------------------------------------


def build_header(repo_root: Path) -> "OrderedDict[str, Any]":
    today = _dt.date.today().isoformat()
    head: "OrderedDict[str, Any]" = OrderedDict()
    head["id"] = "https://w3id.org/lmodel/mellea"
    head["name"] = "mellea"
    head["title"] = "mellea"
    head["description"] = (
        "LinkML schema describing the Mellea codebase architecture and public "
        "data models. Generated from Python sources by "
        "linkml/scripts/schema_to_linkml.py."
    )
    head["license"] = "Apache-2.0"
    head["see_also"] = [
        "https://github.com/lmodel/mellea",
        "https://lmodel.github.io/mellea",
    ]
    head["source"] = "https://github.com/lmodel/mellea"
    head["version"] = today
    head["annotations"] = OrderedDict(
        [
            ("coverage_target", "core-library-and-cli"),
            ("analyzed_scope", "mellea+cli (linkml/ excluded)"),
            ("generated_by", "linkml/scripts/schema_to_linkml.py"),
            ("generated_on", today),
        ]
    )
    return head


PREFIXES: "OrderedDict[str, str]" = OrderedDict(
    [
        ("mellea", "https://w3id.org/lmodel/mellea/"),
        ("linkml", "https://w3id.org/linkml/"),
        ("schema", "http://schema.org/"),
        ("dcterms", "http://purl.org/dc/terms/"),
    ]
)

IMPORTS: list[str] = ["linkml:types"]

TYPES: "OrderedDict[str, dict]" = OrderedDict(
    [
        (
            "PythonDottedPath",
            {
                "base": "str",
                "uri": "xsd:string",
                "description": "Python import-style dotted path.",
                "pattern": r"^[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)*$",
            },
        ),
        (
            "RepositoryRelativePath",
            {
                "base": "str",
                "uri": "xsd:string",
                "description": "Relative path from repository root.",
                "pattern": r"^[^\0]+$",
            },
        ),
    ]
)

SUBSETS: "OrderedDict[str, dict]" = OrderedDict(
    [
        (
            "core_runtime",
            {"description": "Core runtime abstractions and execution flow."},
        ),
        (
            "interface_surface",
            {"description": "API or CLI-facing interfaces and wire models."},
        ),
        (
            "observability",
            {"description": "Telemetry, plugin hooks, and instrumentation."},
        ),
    ]
)


def build_slots() -> "OrderedDict[str, dict]":
    """Schema-level slot definitions.  Order is significant for diff stability."""
    slots: "OrderedDict[str, dict]" = OrderedDict()

    def _add(name: str, **kwargs: Any) -> None:
        slots[name] = OrderedDict(kwargs)

    # Identity / metadata
    _add(
        "id",
        identifier=True,
        required=True,
        range="uriorcurie",
        slot_uri="schema:identifier",
        description="Stable identifier for a schema element.",
    )
    _add(
        "name",
        required=True,
        range="string",
        slot_uri="schema:name",
        description="Human-readable name.",
    )
    _add(
        "description",
        range="string",
        slot_uri="schema:description",
        description="Narrative description of the element.",
    )
    _add(
        "module_path",
        range="PythonDottedPath",
        description="Python module path where this element is defined.",
    )
    _add(
        "source_file",
        range="RepositoryRelativePath",
        description="Source file relative to repository root.",
    )
    _add("package_kind", range="PackageKindEnum", description="Package bucket.")
    _add(
        "element_kind",
        range="ElementKindEnum",
        description="Kind of Python declaration.",
    )
    _add(
        "coverage_scope",
        range="CoverageScopeEnum",
        multivalued=True,
        description="Where this element surfaces (source/API/CLI/example/test).",
    )
    _add(
        "tags",
        range="string",
        multivalued=True,
        description="Free-form classification tags.",
    )

    # Catalog
    _add("repository_root", range="RepositoryRelativePath")
    _add("analyzed_on", range="date")
    _add("includes_path", range="RepositoryRelativePath", multivalued=True)
    _add("excludes_path", range="RepositoryRelativePath", multivalued=True)
    _add("package_name", range="string")
    _add(
        "depends_on_package",
        range="PythonPackage",
        multivalued=True,
        inlined_as_list=True,
    )
    _add(
        "declares_element",
        range="ModelElement",
        multivalued=True,
        inlined_as_list=True,
    )

    # Backends
    _add("backend_family", range="BackendFamilyEnum")
    _add(
        "model_identifier",
        range="ModelIdentifierSpec",
        multivalued=True,
        inlined_as_list=True,
    )
    _add("default_formatter", range="FormatterSpec")
    _add("model_options_key", range="string", multivalued=True)
    _add("supports_streaming", range="boolean")
    _add("supports_tool_calls", range="boolean")
    _add("supports_multimodal", range="boolean")

    # Context / session
    _add("context_linearity", range="ContextLinearityEnum")
    _add("stores_component_history", range="boolean")
    _add("accepts_message_attachments", range="boolean")
    _add("uses_backend", range="BackendSpec")
    _add("uses_context", range="ContextSpec")
    _add("exposed_method", range="MethodSpec", multivalued=True, inlined_as_list=True)
    _add(
        "uses_component_type",
        range="ComponentSpec",
        multivalued=True,
        inlined_as_list=True,
    )

    # Components / requirements / sampling
    _add("component_category", range="ComponentCategoryEnum")
    _add("input_modality", range="string", multivalued=True)
    _add("parsed_output_type", range="string")
    _add("validation_style", range="string")
    _add("may_trigger_repair", range="boolean")
    _add("selection_policy", range="string")
    _add("loop_budget_hint", range="integer")

    # Plugins / hooks / telemetry
    _add("plugin_mode", range="PluginModeEnum")
    _add("hook_type", range="HookTypeEnum", multivalued=True)
    _add(
        "payload_model",
        range="HookPayloadSpec",
        multivalued=True,
        inlined_as_list=True,
    )
    _add("plugin_priority", range="integer")
    _add("metric_name", range="string", multivalued=True)

    # CLI / API
    _add("command_group", range="string")
    _add("command_path", range="string")
    _add("command_purpose", range="string")
    _add("input_model", range="ApiModelSpec", multivalued=True, inlined_as_list=True)
    _add("output_model", range="ApiModelSpec", multivalued=True, inlined_as_list=True)
    _add("request_or_response", range="RequestResponseEnum")
    _add("openai_object_type", range="string")
    _add("has_field", range="ApiFieldSpec", multivalued=True, inlined_as_list=True)
    _add("field_name", range="string")
    _add("field_type", range="string")
    _add("required_field", range="boolean")
    _add("allows_null", range="boolean")
    _add("method_name", range="string")
    _add("method_signature", range="string")
    _add("lifecycle_role", range="string")

    # Adapters / model ids
    _add("adapter_type", range="AdapterTypeEnum", multivalued=True)
    _add("repo_id", range="string")
    _add("provider_name", range="string", multivalued=True)
    _add("hf_model_name", range="string")
    _add("ollama_name", range="string")
    _add("watsonx_name", range="string")
    _add("openai_name", range="string")
    _add("bedrock_name", range="string")

    # Patch in a friendly description on every recommended slot so linkml-lint
    # is happy with the schema's metadata completeness.
    for slot_name, body in slots.items():
        body.setdefault("description", f"Slot describing the {slot_name.replace('_', ' ')}.")
    return slots


def build_classes() -> "OrderedDict[str, dict]":
    """Structural classes that pin the schema's architectural shape."""

    def _cls(
        name: str,
        *,
        is_a: str | None = None,
        abstract: bool = False,
        tree_root: bool = False,
        in_subset: list[str] | None = None,
        slots: list[str] | None = None,
        description: str | None = None,
    ) -> tuple[str, OrderedDict]:
        body: OrderedDict[str, Any] = OrderedDict()
        if description:
            body["description"] = description
        if is_a:
            body["is_a"] = is_a
        if abstract:
            body["abstract"] = True
        if tree_root:
            body["tree_root"] = True
        if in_subset:
            body["in_subset"] = in_subset
        if slots:
            body["slots"] = slots
        return name, body

    classes = OrderedDict(
        [
            _cls(
                "NamedElement",
                abstract=True,
                description="Abstract base for any named, identifiable schema element.",
                slots=[
                    "id",
                    "name",
                    "description",
                    "module_path",
                    "source_file",
                    "package_kind",
                    "element_kind",
                    "coverage_scope",
                    "tags",
                ],
            ),
            _cls(
                "RepositoryCatalog",
                is_a="NamedElement",
                tree_root=True,
                in_subset=["interface_surface"],
                description="Top-level catalog rooting the analysed repository snapshot.",
                slots=[
                    "repository_root",
                    "analyzed_on",
                    "includes_path",
                    "excludes_path",
                    "declares_element",
                ],
            ),
            _cls(
                "PythonPackage",
                is_a="NamedElement",
                description="A logical Python package (directory) inside the repository.",
                slots=["package_name", "depends_on_package", "declares_element"],
            ),
            _cls(
                "ModelElement",
                is_a="NamedElement",
                abstract=True,
                description="Abstract base for concrete architectural elements.",
            ),
            _cls(
                "BackendSpec",
                is_a="ModelElement",
                in_subset=["core_runtime", "interface_surface"],
                description="Specification of a Mellea backend implementation.",
                slots=[
                    "backend_family",
                    "model_identifier",
                    "default_formatter",
                    "model_options_key",
                    "supports_streaming",
                    "supports_tool_calls",
                    "supports_multimodal",
                ],
            ),
            _cls(
                "FormatterSpec",
                is_a="ModelElement",
                in_subset=["core_runtime"],
                description="Specification of an output formatter for a backend.",
            ),
            _cls(
                "ContextSpec",
                is_a="ModelElement",
                in_subset=["core_runtime"],
                description="Specification of a context implementation.",
                slots=[
                    "context_linearity",
                    "stores_component_history",
                    "accepts_message_attachments",
                ],
            ),
            _cls(
                "SessionSpec",
                is_a="ModelElement",
                in_subset=["core_runtime"],
                description="Specification of a Mellea session.",
                slots=["uses_backend", "uses_context", "exposed_method"],
            ),
            _cls(
                "ComponentSpec",
                is_a="ModelElement",
                in_subset=["core_runtime"],
                description="Specification of a Mellea stdlib component type.",
                slots=["component_category", "input_modality", "parsed_output_type"],
            ),
            _cls(
                "RequirementSpec",
                is_a="ModelElement",
                in_subset=["core_runtime"],
                description="Specification of a requirement validator.",
                slots=["validation_style", "may_trigger_repair"],
            ),
            _cls(
                "SamplingStrategySpec",
                is_a="ModelElement",
                in_subset=["core_runtime"],
                description="Specification of a sampling-loop strategy.",
                slots=["selection_policy", "loop_budget_hint", "may_trigger_repair"],
            ),
            _cls(
                "PluginSpec",
                is_a="ModelElement",
                in_subset=["observability"],
                description="Specification of a Mellea plugin and the hooks it registers.",
                slots=["plugin_mode", "hook_type", "payload_model", "plugin_priority"],
            ),
            _cls(
                "HookPayloadSpec",
                is_a="ModelElement",
                in_subset=["observability"],
                description="Specification of a hook payload model.",
                slots=["hook_type", "lifecycle_role"],
            ),
            _cls(
                "TelemetryMetricSpec",
                is_a="ModelElement",
                in_subset=["observability"],
                description="Specification of a telemetry metric emitted by Mellea.",
                slots=["metric_name"],
            ),
            _cls(
                "CliCommandSpec",
                is_a="ModelElement",
                in_subset=["interface_surface"],
                description="Specification of a CLI command exposed under `m`.",
                slots=[
                    "command_group",
                    "command_path",
                    "command_purpose",
                    "input_model",
                    "output_model",
                ],
            ),
            _cls(
                "ApiModelSpec",
                is_a="ModelElement",
                in_subset=["interface_surface"],
                description="Specification of an HTTP API wire model.",
                slots=["request_or_response", "openai_object_type", "has_field"],
            ),
            _cls(
                "ApiFieldSpec",
                is_a="NamedElement",
                in_subset=["interface_surface"],
                description="Specification of a single field in an API model.",
                slots=["field_name", "field_type", "required_field", "allows_null"],
            ),
            _cls(
                "MethodSpec",
                is_a="NamedElement",
                in_subset=["core_runtime"],
                description="Specification of a method exposed by a runtime class.",
                slots=["method_name", "method_signature", "lifecycle_role"],
            ),
            _cls(
                "ModelIdentifierSpec",
                is_a="NamedElement",
                in_subset=["interface_surface"],
                description="Cross-provider identifier table for a single model.",
                slots=[
                    "hf_model_name",
                    "ollama_name",
                    "watsonx_name",
                    "openai_name",
                    "bedrock_name",
                    "provider_name",
                ],
            ),
            _cls(
                "IntrinsicAdapterSpec",
                is_a="NamedElement",
                in_subset=["interface_surface"],
                description="Specification of an intrinsic adapter (LoRA / aLoRA).",
                slots=["repo_id", "adapter_type"],
            ),
        ]
    )
    return classes


# ---------------------------------------------------------------------------
# Schema assembly
# ---------------------------------------------------------------------------


def _inventory_annotations(inv: dict) -> str:
    """Deterministic per-package summary as a single multi-line string.

    Schema-level annotations only accept scalar values (LinkML loader treats
    nested dicts as ``Annotation`` constructor kwargs and lists of dicts fail
    JSON-schema validation).  A formatted string keeps the inventory visible
    in the schema while staying within those constraints.
    """
    lines: list[str] = []
    for sub in sorted(inv["per_package"]):
        by_kind = inv["per_package"][sub]
        kind_counts = OrderedDict((k, len(by_kind[k])) for k in sorted(by_kind))
        total = sum(kind_counts.values())
        kinds = " ".join(f"{k}={v}" for k, v in kind_counts.items())
        lines.append(f"{sub}: total={total} ({kinds})")
    lines.append(f"enum_total: {len(inv['enums'])}")
    return "\n".join(lines)


def build_enums(repo_root: Path, inv: dict) -> "OrderedDict[str, dict]":
    """Assemble the full ``enums:`` block (static + source-derived)."""
    enums: "OrderedDict[str, dict]" = OrderedDict()
    enums.update(STATIC_ENUMS)

    enums["BackendFamilyEnum"] = {
        "description": "Backend families discovered under mellea/backends/.",
        "permissible_values": discover_backend_families(repo_root),
        "annotations": OrderedDict([("derived_from", "mellea/backends/*.py")]),
    }

    plugin_mode = find_enum(inv, "mellea/plugins/types.py", "PluginMode")
    enums["PluginModeEnum"] = build_enum_from_source(
        plugin_mode,
        description="Execution mode of a Mellea plugin (derived from PluginMode).",
        fallback_values=[
            "SEQUENTIAL",
            "TRANSFORM",
            "CONCURRENT",
            "AUDIT",
            "FIRE_AND_FORGET",
        ],
    )

    hook_type = find_enum(inv, "mellea/plugins/types.py", "HookType")
    enums["HookTypeEnum"] = build_enum_from_source(
        hook_type,
        description="Lifecycle hook stages (derived from HookType).",
        fallback_values=[
            "SESSION_PRE_INIT",
            "SESSION_POST_INIT",
            "SESSION_RESET",
            "SESSION_CLEANUP",
            "COMPONENT_PRE_EXECUTE",
            "COMPONENT_POST_SUCCESS",
            "COMPONENT_POST_ERROR",
            "GENERATION_PRE_CALL",
            "GENERATION_POST_CALL",
            "GENERATION_ERROR",
            "VALIDATION_PRE_CHECK",
            "VALIDATION_POST_CHECK",
            "SAMPLING_LOOP_START",
            "SAMPLING_ITERATION",
            "SAMPLING_REPAIR",
            "SAMPLING_LOOP_END",
            "TOOL_PRE_INVOKE",
            "TOOL_POST_INVOKE",
        ],
    )

    adapter_type = find_enum(
        inv, "mellea/backends/adapters/catalog.py", "AdapterType"
    )
    enums["AdapterTypeEnum"] = build_enum_from_source(
        adapter_type,
        description="Adapter implementation type (derived from AdapterType).",
        fallback_values=["LORA", "ALORA"],
    )

    return enums


def build_schema(repo_root: Path) -> "OrderedDict[str, Any]":
    inv = collect_inventory(repo_root)
    schema = build_header(repo_root)
    schema["annotations"]["coverage_inventory"] = _inventory_annotations(inv)
    schema["prefixes"] = PREFIXES
    schema["default_prefix"] = "mellea"
    schema["default_range"] = "string"
    schema["imports"] = list(IMPORTS)
    schema["types"] = TYPES
    schema["subsets"] = SUBSETS
    schema["enums"] = build_enums(repo_root, inv)
    schema["slots"] = build_slots()
    schema["classes"] = build_classes()
    return schema


# ---------------------------------------------------------------------------
# YAML emission
# ---------------------------------------------------------------------------


def _yaml_dump(obj: Any) -> str:
    """Deterministic YAML dump preserving insertion order."""

    class _Dumper(yaml.SafeDumper):
        def increase_indent(self, flow=False, indentless=False):  # noqa: D401
            # Force block sequences to indent under their parent key.
            return super().increase_indent(flow=flow, indentless=False)

    def _represent_ordered(dumper: yaml.SafeDumper, data: OrderedDict) -> Any:
        return dumper.represent_mapping(
            "tag:yaml.org,2002:map", list(data.items())
        )

    _Dumper.add_representer(OrderedDict, _represent_ordered)
    _Dumper.add_representer(
        defaultdict,
        lambda d, data: d.represent_mapping(
            "tag:yaml.org,2002:map", list(data.items())
        ),
    )

    return yaml.dump(
        obj,
        Dumper=_Dumper,
        sort_keys=False,
        default_flow_style=False,
        width=100,
        allow_unicode=True,
        indent=2,
    )


def render(schema: dict) -> str:
    body = _yaml_dump(schema)
    header = (
        "# Auto-generated by linkml/scripts/schema_to_linkml.py.\n"
        "# Do not edit by hand; rerun the generator to refresh.\n"
        "# See linkml/scripts/README.md for details.\n"
        "---\n"
    )
    return header + body


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def _parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument(
        "--repo-root",
        type=Path,
        default=REPO_ROOT_DEFAULT,
        help="Path to the Mellea repository root (default: auto-detect).",
    )
    p.add_argument(
        "--out-file",
        type=Path,
        default=OUT_FILE_DEFAULT,
        help="Destination YAML path.",
    )
    p.add_argument(
        "--stdout",
        action="store_true",
        help="Write to stdout instead of --out-file.",
    )
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(list(sys.argv[1:] if argv is None else argv))
    schema = build_schema(args.repo_root.resolve())
    text = render(schema)
    if args.stdout:
        sys.stdout.write(text)
        return 0
    args.out_file.parent.mkdir(parents=True, exist_ok=True)
    args.out_file.write_text(text, encoding="utf-8")
    print(f"wrote {args.out_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
