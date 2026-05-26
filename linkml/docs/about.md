# About mellea

LinkML schema describing the [Mellea](https://github.com/lmodel/mellea) codebase architecture and public data models.

## Status

- **Schema version:** commit df6d0fd
- **Coverage target:** core library (`mellea/`) and CLI (`cli/`)
- **Generation:** auto-derived from live Mellea Python sources by
  [`linkml/scripts/schema_to_linkml.py`](https://github.com/lmodel/mellea/blob/main/linkml/scripts/schema_to_linkml.py)
- **Test fixtures:** auto-derived from live sources by
  [`linkml/scripts/gen_test_fixtures.py`](https://github.com/lmodel/mellea/blob/main/linkml/scripts/gen_test_fixtures.py)
  — 62 valid + 4 counter-examples under `linkml/tests/data/`
- **SSSOM overlay:** schema-agnostic injector
  [`linkml/scripts/apply_sssom_overlay.py`](https://github.com/lmodel/mellea/blob/main/linkml/scripts/apply_sssom_overlay.py) merges CURIE alignments from `src/mellea/mappings/*.sssom.tsv` into the generated YAML's `exact_mappings` / `close_mappings` / `broad_mappings` / `narrow_mappings` / `related_mappings` slots (classes, enums, types, slots, and per-permissible-value)
- **Validated by:** `just lint` (0 errors), `just gen-project`, `just test` (62 pytest fixtures pass; `linkml-run-examples` accepts valid set and rejects all counter-examples)

## What the schema models

| Subset             | Classes |
|--------------------|---------|
| `core_runtime`     | `BackendSpec`, `FormatterSpec`, `ContextSpec`, `SessionSpec`, `ComponentSpec`, `RequirementSpec`, `SamplingStrategySpec`, `MethodSpec` |
| `interface_surface`| `RepositoryCatalog`, `CliCommandSpec`, `ApiModelSpec`, `ApiFieldSpec`, `ModelIdentifierSpec`, `IntrinsicAdapterSpec` |
| `observability`    | `PluginSpec`, `HookPayloadSpec`, `TelemetryMetricSpec` |

## Source-derived elements

These schema elements are re-extracted from Python sources on every
regeneration — no hand-editing required when upstream changes:

| Schema element        | Source of truth                                    |
|-----------------------|----------------------------------------------------|
| `PluginModeEnum`      | `mellea/plugins/types.py::PluginMode`              |
| `HookTypeEnum`        | `mellea/plugins/types.py::HookType`                |
| `AdapterTypeEnum`     | `mellea/backends/adapters/catalog.py::AdapterType` |
| `BackendFamilyEnum`   | `mellea/backends/*.py` filenames                   |
| `coverage_inventory`  | AST scan of `mellea/` + `cli/` (per-package counts)|

## Project automation: just commands

All schema and artifact generation, validation, and testing is managed via [just](https://just.systems/) recipes. Run these from the `linkml/` workspace:

```bash
# Regenerate the LinkML schema YAML from live Mellea Python sources
just gen-linkml

# Regenerate test fixtures from live sources
just gen-fixtures

# Apply SSSOM mappings to the generated schema YAML
just apply-sssom-overlay

# Convenience: refresh schema, mappings, and fixtures
just regen-all

# Full pipeline: regenerate, validate, and test
just regen-and-test

# Generate project files (Python, Java, TypeScript, OWL)
just gen-project

# Generate documentation
just gen-doc

# Run all tests
just test

# Lint the schema
just lint

# Build docs and run test server
just testdoc

# Install project dependencies
just install

# Update project template and LinkML packages
just update

# Clean all generated files
just clean
```

See the `project.justfile` and `justfile` for full details, including advanced recipes for migrations, deployment, and internal maintenance.

The overlay is idempotent: re-running on a clean tree produces no further changes. The subject-side CURIE prefix is taken from each schema's own `default_prefix`, so the same script is reusable for downstream LinkML schemas without modification (override with `--subject-prefix` if needed).

See [`linkml/scripts/README.md`](https://github.com/lmodel/mellea/blob/main/linkml/scripts/README.md) for generator details and the process for adding new auto-derived enums.

## Coverage inventory (as of commit df6d0fd)

| Package            | Total | Breakdown |
|--------------------|------:|-----------|
| `cli`              | 86 | CLASS=42, DATACLASS=5, ENUM=4, PYDANTIC_MODEL=20, TYPED_DICT=15 |
| `mellea/backends`  | 28 | CLASS=22, DATACLASS=2, ENUM=1, MIXIN=1, PYDANTIC_MODEL=2 |
| `mellea/core`      | 27 | CLASS=20, DATACLASS=5, ENUM=1, PROTOCOL=1 |
| `mellea/formatters`| 57 | CLASS=39, ENUM=1, MIXIN=1, PYDANTIC_MODEL=16 |
| `mellea/helpers`   | 6  | CLASS=2, ENUM=1, PYDANTIC_MODEL=1, TYPED_DICT=2 |
| `mellea/plugins`   | 32 | CLASS=28, DATACLASS=2, ENUM=2 |
| `mellea/stdlib`    | 69 | CLASS=50, DATACLASS=10, ENUM=1, PROTOCOL=2, PYDANTIC_MODEL=4, TYPED_DICT=2 |
| `mellea/telemetry` | 11 | CLASS=11 |
| **Total enums**    | 11 | (across all packages) |

Inventory counts are regenerated automatically and stored as the
`coverage_inventory` annotation on the schema header.

## Validation fixtures

| Fixture pattern                    | Count | Source                                |
|------------------------------------|------:|---------------------------------------|
| `BackendSpec-<family>.yaml`        |     7 | `mellea/backends/*.py`                |
| `IntrinsicAdapterSpec-<name>.yaml` |    13 | `mellea/backends/adapters/catalog.py` |
| `ModelIdentifierSpec-<const>.yaml` |    42 | `mellea/backends/model_ids.py`        |
| Counter-examples (invalid)         |     4 | hand-curated                          |

All valid fixtures load through `linkml_runtime.yaml_loader`; all
counter-examples are rejected by `linkml-run-examples`.

## Cross-schema mappings

Curated SSSOM/TSV alignments to six downstream schemas live under
[`src/mellea/mappings/`](https://github.com/lmodel/mellea/blob/main/linkml/src/mellea/mappings/).

These files contain artificially-curated (`semapv:LLMBasedMatching`) mappings, parse cleanly with [pypi sssom](https://pypi.org/project/sssom/), use real Mellea CURIEs validated against [`linkml/src/mellea/schema/mellea.yaml`](https://github.com/lmodel/mellea/blob/main/linkml/src/mellea/schema/mellea.yaml), and carry per-row rationale (with name-collision notes such as `RequirementSpec` vs `nexus:Requirement`) in the `comment` column.

The three **flagship** alignments are the densest and target schemas with genuine domain overlap with the Mellea runtime: the [ai-atlas-nexus](https://github.com/IBM/ai-atlas-nexus) AI Risk Ontology, the [Model Context Protocol](https://modelcontextprotocol.io/), and [SPDX 3](https://spdx.github.io/spdx-spec/v3.0.1/) (AI-package / SBOM).

The remaining three (ISO 27001, MITRE ATT&CK, FINOS CDM event-position) are provided as smaller, honest cross-domain alignments centred on observability, audit, and structural analogues.

| Mapping set | exact | close | narrow | related | Total | Strongest alignment |
|---|---:|---:|---:|---:|---:|---|
| [`mellea-to-ai-atlas-nexus`](https://github.com/lmodel/mellea/blob/main/linkml/src/mellea/mappings/mellea-to-ai-atlas-nexus.sssom.tsv) | 1 | 9 | 1 | 25 | **36** | `AdapterTypeEnum` <-> `nexus:AdapterType` (exact) |
| [`mellea-to-mcp`](https://github.com/lmodel/mellea/blob/main/linkml/src/mellea/mappings/mellea-to-mcp.sssom.tsv) | – | 8 | – | 12 | **20** | `ComponentCategoryEnum.MESSAGE` <-> `mcp:PromptMessage` |
| [`mellea-to-spdx`](https://github.com/lmodel/mellea/blob/main/linkml/src/mellea/mappings/mellea-to-spdx.sssom.tsv) | – | 6 | – | 8 | **14** | `ModelIdentifierSpec` / `IntrinsicAdapterSpec` <-> `spdx:AIPackage` |
| [`mellea-to-iso27001`](https://github.com/lmodel/mellea/blob/main/linkml/src/mellea/mappings/mellea-to-iso27001.sssom.tsv) | – | 2 | – | 10 | **12** | `TelemetryMetricSpec` <-> `iso27001:MonitoringItem` |
| [`mellea-to-attack`](https://github.com/lmodel/mellea/blob/main/linkml/src/mellea/mappings/mellea-to-attack.sssom.tsv) | – | – | – | 9 | **9** | `TelemetryMetricSpec` <-> `attack:DataSource` |
| [`mellea-to-cdm_event_position`](https://github.com/lmodel/mellea/blob/main/linkml/src/mellea/mappings/mellea-to-cdm_event_position.sssom.tsv) | – | – | – | 6 | **6** | `RepositoryCatalog` <-> `common_domain_model:Portfolio` (structural) |
| **Total** | **1** | **25** | **1** | **70** | **97** | |

Coverage reflects genuine domain overlap, not row inflation. Mellea models an AI runtime / code architecture, so:

- **ai-atlas-nexus** (AI governance ontology) aligns on adapter type,
  provider, model, intrinsic, component, requirement, and lifecycle hooks.
- **MCP** (AI runtime protocol) aligns cleanly on stdlib component
  categories — `INSTRUCTION` <-> `Prompt`, `MESSAGE` <-> `PromptMessage` / `SamplingMessage`, `TOOL_MESSAGE` <-> `ToolUseContent` / `ToolResultContent`, `DOCUMENT` <-> `Resource`.
- **SPDX 3** aligns on AI model provenance via `AIPackage`, on repository
  packaging via `Sbom` / `Package`, and on plugins via `Extension`.
- **ISO 27001** aligns on observability/audit primitives —
  `TelemetryMetricSpec` <-> `MonitoringItem` (closeMatch),
  `PluginModeEnum.AUDIT` <-> `InternalAudit`.
- **MITRE ATT&CK** aligns weakly on detection/observability —
  `TelemetryMetricSpec` <-> `DataSource`, `HookPayloadSpec` <-> `DataComponent`.
- **FINOS CDM event-position** has essentially no domain overlap; only
  structural aggregation analogues at low confidence are recorded.

Object CURIEs are validated against each target schema under
`src/mellea/mappings/<target>/docs/schema/`. Run `just apply-sssom-overlay` after editing any TSV: the schema-agnostic
[`apply_sssom_overlay.py`](https://github.com/lmodel/mellea/blob/main/linkml/scripts/apply_sssom_overlay.py) script projects every row into the generated schema YAML as native LinkML mapping slots, registers each target prefix from the TSV's `curie_map`, and lands permissible-value subjects (`<prefix>:EnumName.PV_NAME`, e.g. `mellea:BackendFamilyEnum.HUGGINGFACE`) on the matching permissible value rather than enum body.

## Continuous integration

Two GitHub Actions workflows operate against the `linkml/` subdirectory (both set `defaults.run.working-directory: linkml` and cache against `linkml/uv.lock`):

| Workflow | Triggers | Job |
|----------|----------|-----|
| [`.github/workflows/linkml-main.yaml`](https://github.com/lmodel/mellea/blob/main/.github/workflows/linkml-main.yaml) | `push: [main]`, `pull_request` | `just test` on the 3.11–3.14 Python matrix |
| [`.github/workflows/linkml-deploy-docs.yaml`](https://github.com/lmodel/mellea/blob/main/.github/workflows/linkml-deploy-docs.yaml) | `push: [main]`, `workflow_dispatch` | `just gen-doc` + `mkdocs gh-deploy` |

The deploy workflow pushes to the `gh-pages` branch via git, so only
`contents: write` is required — Pages / OIDC permissions are unused.

## Known gaps

- Stylistic `linkml-lint` warnings (naming conventions on permissible values, missing per-slot descriptions) — non-blocking; addressable in a follow-up.
- `mellea/templates/` (Jinja templates) is intentionally excluded — no Python declarations to capture.
- Per-component instance data (concrete `BackendSpec` / `ComponentSpec`
  records) is not yet emitted; the schema currently defines the *shape* of such instances. A follow-up generator pass can populate them.
- Generator output under [`linkml/project/`](https://github.com/lmodel/mellea/blob/main/linkml/project/) (gen-sqla, gen-pandera, gen-namespaces, …) is excluded from ruff via `force-exclude` + `extend-exclude` in the root [`pyproject.toml`](https://github.com/lmodel/mellea/blob/main/pyproject.toml) `[tool.ruff]` block. In-place fixes are pointless because `just gen-project` regenerates and clobbers them — upstream linkml templates are the source of the style noise.
