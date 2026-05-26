#!/usr/bin/env python3
"""Overlay SSSOM mappings onto generated LinkML schema YAML files.

This is the "overlay-only" path: it does NOT re-parse upstream sources.
Use it when an ``*.sssom.tsv`` file under ``--mappings-dir`` has been
edited and the new mappings need to be pushed into the schema YAML(s)
without regenerating them from scratch.

The script is schema-agnostic. For each YAML file in ``--schema-dir`` the
subject-side CURIE prefix is taken from the schema's own ``default_prefix``
(e.g. a schema with ``default_prefix: myschema`` consumes TSV rows whose
``subject_id`` starts with ``myschema:``). Pass ``--subject-prefix`` to
override this auto-detection (useful when running against a single schema
whose ``default_prefix`` differs from the TSV convention).

For each YAML file in ``--schema-dir`` the script:

1. Loads ``classes``, ``enums``, ``slots`` and ``types``.
2. For every element whose unsuffixed local name appears as a subject in
   one of the SSSOM TSVs (using the schema's subject prefix), merges the
   predicate-mapped CURIEs into the matching LinkML mapping slot
   (``exact_mappings``, ``close_mappings``, ``broad_mappings``,
   ``narrow_mappings``, ``related_mappings``). Existing entries are
   preserved; duplicates are dropped.
3. Permissible-value-scoped subjects of the form
   ``<prefix>:EnumName.PV_NAME`` are merged onto the matching permissible
   value inside ``enums``.
4. Adds any referenced object-side prefixes to the YAML's ``prefixes``
   block (URIs come from each TSV's ``#curie_map:`` metadata).
5. Writes the YAML back using ``schema_to_linkml._yaml_dump`` so the output
   keeps the same byte-level shape as a freshly-generated file.

The script is idempotent: running it twice on a clean tree produces no
further changes.
"""

from __future__ import annotations

import argparse
import sys
from collections import OrderedDict
from pathlib import Path

import yaml

# Reuse the canonical YAML formatter from schema_to_linkml.py so overlaid
# files keep the exact byte-level shape of a fresh generator run.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from schema_to_linkml import _yaml_dump

# SKOS predicate -> LinkML mapping slot.
SSSOM_PREDICATE_TO_LINKML_SLOT: dict[str, str] = {
    "skos:exactMatch": "exact_mappings",
    "skos:closeMatch": "close_mappings",
    "skos:broadMatch": "broad_mappings",
    "skos:narrowMatch": "narrow_mappings",
    "skos:relatedMatch": "related_mappings",
}

# Prefixes that are intrinsic to LinkML / SSSOM and need not be declared on
# every schema YAML.
_SSSOM_BUILTIN_PREFIXES = {"sssom", "owl", "rdf", "rdfs", "skos", "semapv", "linkml"}


# ---------------------------------------------------------------------------
# Canonical layout of mapping slots inside a class / enum / type body
# ---------------------------------------------------------------------------
#
# schema_to_linkml.py emits class / enum / type bodies in this canonical
# order (see VersionEmitter.emit_*):
#
#   description, abstract, is_a, tree_root, mixins, mixin,
#   class_uri / enum_uri / uri,
#   exact_mappings, aliases, in_subset,
#   permissible_values / attributes / slots, ...
#
# New mapping slots are inserted just AFTER the latest preceding
# already-present mapping slot, or just BEFORE the first post-mapping anchor
# that already exists.

_POST_MAPPING_ANCHORS_CLASS = (
    "aliases",
    "in_subset",
    "attributes",
    "slots",
    "slot_usage",
    "rules",
    "comments",
    "annotations",
)
_POST_MAPPING_ANCHORS_ENUM = ("aliases", "in_subset", "permissible_values")
_POST_MAPPING_ANCHORS_TYPE = ("aliases", "in_subset", "pattern", "annotations")
_POST_MAPPING_ANCHORS_SLOT = ("aliases", "in_subset", "annotations")

# Relative order of the five mapping slots within a body.
_MAPPING_SLOT_ORDER = (
    "exact_mappings",
    "close_mappings",
    "broad_mappings",
    "narrow_mappings",
    "related_mappings",
)


# ---------------------------------------------------------------------------
# SSSOM TSV parsing
# ---------------------------------------------------------------------------


def _parse_sssom_metadata(path: Path) -> dict:
    """Parse the leading ``#`` metadata block of an SSSOM TSV as YAML."""
    buf: list[str] = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("#"):
                break
            # Strip the leading ``#`` and, if present, the single space SSSOM
            # writers conventionally place between the hash and the YAML
            # payload (``# key: value``). Indentation beyond that single
            # space is preserved as YAML structure.
            stripped = line[1:]
            if stripped.startswith(" "):
                stripped = stripped[1:]
            buf.append(stripped)
    if not buf:
        return {}
    try:
        meta = yaml.safe_load("".join(buf))
    except yaml.YAMLError:
        return {}
    return meta if isinstance(meta, dict) else {}


def _parse_sssom_rows(path: Path) -> tuple[list[str], list[list[str]]]:
    """Return ``(header, rows)`` from the TSV body (skipping metadata)."""
    header: list[str] | None = None
    rows: list[list[str]] = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\r\n")
            if not line or line.startswith("#"):
                continue
            fields = line.split("\t")
            if header is None:
                header = fields
                continue
            rows.append(fields)
    return (header or []), rows


def _strip_subject_prefix(curie: str, subject_prefix: str) -> str | None:
    """Return the local name if ``curie`` starts with ``subject_prefix:``.

    Permissible-value-scoped subjects of the form
    ``<subject_prefix>:EnumName.PV_NAME`` are returned unchanged (minus the
    prefix) so callers can split on ``.``.
    """
    px = f"{subject_prefix}:"
    if curie.startswith(px):
        return curie[len(px) :]
    return None


# ---------------------------------------------------------------------------
# Mapping index
# ---------------------------------------------------------------------------


class MappingIndex:
    """subject_local_name -> mapping_slot -> ordered list of object CURIEs."""

    def __init__(self) -> None:
        """Initialize empty per-subject mapping and prefix-URI dictionaries."""
        self.by_name: dict[str, dict[str, list[str]]] = {}
        self.prefix_uris: dict[str, str] = {}

    def add(self, name: str, slot: str, obj_curie: str) -> None:
        """Record a CURIE mapping under ``name``/``slot``, preserving insertion order."""
        slot_map = self.by_name.setdefault(name, {})
        existing = slot_map.setdefault(slot, [])
        if obj_curie not in existing:
            existing.append(obj_curie)

    def used_prefixes_for(self, name: str) -> set[str]:
        """Return the set of CURIE prefixes referenced by any mapping on ``name``."""
        out: set[str] = set()
        for curies in self.by_name.get(name, {}).values():
            for c in curies:
                if ":" in c:
                    out.add(c.split(":", 1)[0])
        return out


class RawMappings:
    """Unfiltered SSSOM rows + accumulated ``curie_map`` URIs.

    Subject-prefix filtering is deferred to :meth:`index_for` so a single
    pool of TSVs can drive multiple schemas with different
    ``default_prefix`` values.
    """

    def __init__(self) -> None:
        """Initialize an empty row pool and prefix-URI dictionary."""
        # (subject_curie, predicate, object_curie)
        self.rows: list[tuple[str, str, str]] = []
        self.prefix_uris: dict[str, str] = {}

    def index_for(self, subject_prefix: str) -> MappingIndex:
        """Build a :class:`MappingIndex` filtered to rows whose subject uses ``subject_prefix``."""
        idx = MappingIndex()
        idx.prefix_uris = dict(self.prefix_uris)
        for subject, predicate, obj in self.rows:
            local = _strip_subject_prefix(subject, subject_prefix)
            if local is None:
                continue
            slot = SSSOM_PREDICATE_TO_LINKML_SLOT.get(predicate)
            if slot is None or not obj:
                continue
            idx.add(local, slot, obj)
        return idx


def load_mappings(mappings_dir: Path) -> RawMappings:
    """Load every ``*.sssom.tsv`` under ``mappings_dir`` into one raw pool."""
    raw = RawMappings()
    for tsv in sorted(mappings_dir.glob("*.sssom.tsv")):
        meta = _parse_sssom_metadata(tsv)
        curie_map = meta.get("curie_map") or {}
        if isinstance(curie_map, dict):
            for px, uri in curie_map.items():
                if px in _SSSOM_BUILTIN_PREFIXES:
                    continue
                raw.prefix_uris.setdefault(px, uri)

        header, rows = _parse_sssom_rows(tsv)
        if not header:
            continue
        col = {name: i for i, name in enumerate(header)}
        try:
            si = col["subject_id"]
            pi = col["predicate_id"]
            oi = col["object_id"]
        except KeyError as missing:
            print(
                f"WARN: {tsv.name} missing required column "
                f"{missing.args[0]!r}; skipping file",
                file=sys.stderr,
            )
            continue
        for row in rows:
            if len(row) <= max(si, pi, oi):
                continue
            subject = row[si].strip()
            predicate = row[pi].strip()
            obj = row[oi].strip()
            if not subject or not predicate:
                continue
            raw.rows.append((subject, predicate, obj))
    return raw


# ---------------------------------------------------------------------------
# YAML overlay
# ---------------------------------------------------------------------------


def _to_ordered(value):
    """Recursively convert plain dicts to OrderedDicts (preserving order)."""
    if isinstance(value, dict):
        return OrderedDict((k, _to_ordered(v)) for k, v in value.items())
    if isinstance(value, list):
        return [_to_ordered(v) for v in value]
    return value


def _insert_mapping_slot(
    body: OrderedDict, slot: str, curies: list[str], post_anchors: tuple[str, ...]
) -> None:
    """Place ``slot`` at its canonical position within ``body``.

    Insertion rules:

    * If ``slot`` already exists, its value is replaced in place.
    * Otherwise insert just after the latest preceding mapping slot already
      in ``body``; failing that, just before the next succeeding mapping
      slot; failing that, just before the first post-mapping anchor that
      already exists; failing that, append.
    """
    if slot in body:
        body[slot] = curies
        return

    target_after: str | None = None
    slot_idx = _MAPPING_SLOT_ORDER.index(slot)
    for s in _MAPPING_SLOT_ORDER[:slot_idx]:
        if s in body:
            target_after = s

    target_before: str | None = None
    if target_after is None:
        for s in _MAPPING_SLOT_ORDER[slot_idx + 1 :]:
            if s in body:
                target_before = s
                break
        if target_before is None:
            for k in post_anchors:
                if k in body:
                    target_before = k
                    break

    rebuilt: OrderedDict = OrderedDict()
    inserted = False
    if target_after is not None:
        for k, v in body.items():
            rebuilt[k] = v
            if k == target_after and not inserted:
                rebuilt[slot] = curies
                inserted = True
    elif target_before is not None:
        for k, v in body.items():
            if k == target_before and not inserted:
                rebuilt[slot] = curies
                inserted = True
            rebuilt[k] = v
    if not inserted:
        rebuilt = OrderedDict(body)
        rebuilt[slot] = curies

    body.clear()
    body.update(rebuilt)


def _merge_mappings(
    body: OrderedDict, slot_map: dict[str, list[str]], post_anchors: tuple[str, ...]
) -> tuple[bool, int]:
    """Merge ``slot_map`` into ``body``. Returns ``(touched, links_added)``."""
    touched = False
    links_added = 0
    # Apply slots in canonical order so the YAML diff is stable across runs.
    for slot in _MAPPING_SLOT_ORDER:
        curies = slot_map.get(slot)
        if not curies:
            continue
        existing = body.get(slot)
        if existing is None:
            _insert_mapping_slot(body, slot, list(curies), post_anchors)
            links_added += len(curies)
            touched = True
        else:
            new_list = list(existing)
            added_here = 0
            for c in curies:
                if c not in new_list:
                    new_list.append(c)
                    added_here += 1
            if added_here:
                body[slot] = new_list
                links_added += added_here
                touched = True
    return touched, links_added


def _ensure_prefixes(
    data: OrderedDict,
    needed: set[str],
    prefix_uris: dict[str, str],
    own_prefix: str | None,
) -> bool:
    """Add referenced prefixes to ``data['prefixes']``. Returns changed flag."""
    changed = False
    prefixes = data.get("prefixes")
    if not isinstance(prefixes, dict):
        prefixes = OrderedDict()
        data["prefixes"] = prefixes
    own_prefixes = {own_prefix} if own_prefix else set()
    for px in sorted(needed):
        if px in _SSSOM_BUILTIN_PREFIXES or px in own_prefixes:
            continue
        if px in prefixes:
            continue
        uri = prefix_uris.get(px)
        if uri is None:
            print(
                f"WARN: prefix {px!r} referenced by a mapping but no URI "
                f"found in any sssom curie_map; declare it manually.",
                file=sys.stderr,
            )
            continue
        prefixes[px] = uri
        changed = True
    return changed


# ---------------------------------------------------------------------------
# Whole-file overlay
# ---------------------------------------------------------------------------


def overlay_file(
    schema_path: Path,
    raw_mappings: RawMappings,
    subject_prefix_override: str | None = None,
) -> tuple[int, int]:
    """Overlay mappings onto one schema YAML in place.

    Subject-side CURIE prefix is taken from the schema's ``default_prefix``
    unless ``subject_prefix_override`` is provided.

    Returns ``(elements_updated, links_added)``. The file is rewritten only
    when at least one element was modified or a new prefix was declared.
    """
    text = schema_path.read_text(encoding="utf-8")
    # Preserve the original ``---`` + leading ``#`` comment block verbatim;
    # schema_to_linkml.py owns the header and we don't want to rewrite it.
    header_lines: list[str] = []
    body_start = 0
    for raw in text.splitlines(keepends=True):
        stripped = raw.rstrip("\n")
        if stripped == "---" or stripped.startswith("#") or stripped == "":
            header_lines.append(raw)
            body_start += len(raw)
            if stripped == "" and any(
                hl.lstrip().startswith("#") for hl in header_lines
            ):
                break
        else:
            break
    header = "".join(header_lines)

    data = yaml.safe_load(text)
    if data is None:
        data = OrderedDict()
    data = _to_ordered(data)

    # Determine the subject-side CURIE prefix for this schema. Explicit
    # override wins; otherwise fall back to the schema's ``default_prefix``.
    subject_prefix = subject_prefix_override or data.get("default_prefix")
    if not subject_prefix or not isinstance(subject_prefix, str):
        print(
            f"WARN: {schema_path.name}: no 'default_prefix' found and no "
            "--subject-prefix override given; skipping.",
            file=sys.stderr,
        )
        return 0, 0
    mappings = raw_mappings.index_for(subject_prefix)
    if not mappings.by_name:
        return 0, 0

    elements_updated = 0
    links_added = 0
    used_prefixes: set[str] = set()

    for collection_key, post_anchors in (
        ("classes", _POST_MAPPING_ANCHORS_CLASS),
        ("slots", _POST_MAPPING_ANCHORS_SLOT),
        ("enums", _POST_MAPPING_ANCHORS_ENUM),
        ("types", _POST_MAPPING_ANCHORS_TYPE),
    ):
        collection = data.get(collection_key)
        if not isinstance(collection, dict):
            continue
        for name, body in collection.items():
            if not isinstance(body, OrderedDict):
                continue
            slot_map = mappings.by_name.get(name)
            if not slot_map:
                continue
            touched, n_added = _merge_mappings(body, slot_map, post_anchors)
            if touched:
                elements_updated += 1
                links_added += n_added
                used_prefixes |= mappings.used_prefixes_for(name)

    # Permissible-value-scoped subjects: ``EnumName.PV_NAME`` -> merge onto
    # ``enums[EnumName].permissible_values[PV_NAME]``.
    enums_block = data.get("enums")
    if isinstance(enums_block, dict):
        for subject_name, slot_map in mappings.by_name.items():
            if "." not in subject_name:
                continue
            enum_name, _, pv_name = subject_name.partition(".")
            enum_body = enums_block.get(enum_name)
            if not isinstance(enum_body, OrderedDict):
                continue
            pvs = enum_body.get("permissible_values")
            if not isinstance(pvs, OrderedDict):
                continue
            pv_body = pvs.get(pv_name)
            if pv_body is None:
                continue
            if not isinstance(pv_body, OrderedDict):
                # Scalar value (e.g. PV declared as ``LORA:``) -- promote to a
                # mapping body so we have somewhere to attach the slots.
                pv_body = OrderedDict()
                pvs[pv_name] = pv_body
            touched, n_added = _merge_mappings(
                pv_body, slot_map, _POST_MAPPING_ANCHORS_ENUM
            )
            if touched:
                elements_updated += 1
                links_added += n_added
                used_prefixes |= mappings.used_prefixes_for(subject_name)

    prefixes_changed = _ensure_prefixes(
        data, used_prefixes, mappings.prefix_uris, subject_prefix
    )

    if elements_updated or prefixes_changed:
        if not header:
            header = (
                "# Overlaid by linkml/scripts/apply_sssom_overlay.py.\n"
                "# Do not edit mapping slots by hand; rerun the script to "
                "refresh.\n"
                "---\n"
            )
        out = header + _yaml_dump(data)
        if not out.endswith("\n"):
            out += "\n"
        schema_path.write_text(out, encoding="utf-8")
    return elements_updated, links_added


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    """CLI entry point: merge SSSOM mappings into the generated LinkML schema."""
    here = Path(__file__).resolve().parent
    repo_root = here.parent
    default_schema_dir = repo_root / "src" / "mellea" / "schema"
    default_mappings_dir = repo_root / "src" / "mellea" / "mappings"

    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument(
        "--schema-dir",
        type=Path,
        default=default_schema_dir,
        help="directory containing LinkML schema YAML files",
    )
    p.add_argument(
        "--mappings-dir",
        type=Path,
        default=default_mappings_dir,
        help="directory containing *.sssom.tsv mapping files",
    )
    p.add_argument(
        "--subject-prefix",
        default=None,
        help=(
            "CURIE prefix (without trailing ':') identifying subject rows "
            "in the SSSOM TSVs. Defaults to each schema's own "
            "'default_prefix'."
        ),
    )
    args = p.parse_args(argv)

    if not args.schema_dir.is_dir():
        print(
            f"ERROR: schema-dir {args.schema_dir} is not a directory", file=sys.stderr
        )
        return 1
    if not args.mappings_dir.is_dir():
        print(
            f"ERROR: mappings-dir {args.mappings_dir} is not a directory",
            file=sys.stderr,
        )
        return 1

    raw = load_mappings(args.mappings_dir)
    if not raw.rows:
        print(
            f"No mapping rows loaded from {args.mappings_dir} "
            "(expected *.sssom.tsv files); nothing to do.",
            file=sys.stderr,
        )
        return 0

    print(f"Loaded {len(raw.rows)} mapping rows from {args.mappings_dir}")

    schemas = sorted(args.schema_dir.glob("*.yaml"))
    if not schemas:
        print(f"No YAML schemas in {args.schema_dir}", file=sys.stderr)
        return 1

    files_changed = 0
    total_elements = 0
    total_links = 0
    for path in schemas:
        elements, links = overlay_file(path, raw, args.subject_prefix)
        if elements:
            files_changed += 1
            total_elements += elements
            total_links += links
            print(f"  {path.name}: +{links} links across {elements} elements")

    if total_links:
        print(
            f"\nOverlay complete: {total_links} new mappings applied to "
            f"{total_elements} elements across {files_changed} files"
        )
    else:
        print(
            "\nOverlay complete: schemas already in sync with SSSOM files "
            "- no changes needed"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
