# LinkML schema regeneration

The Mellea LinkML schema at [`linkml/src/mellea/schema/mellea.yaml`](../src/mellea/schema/mellea.yaml) is auto-generated from the live Mellea Python sources by [`schema_to_linkml.py`](./schema_to_linkml.py).

## When to run

Re-run the generator whenever upstream code changes that affect any of:

- enum members of `mellea.plugins.types.PluginMode` or `HookType`
- enum members of `mellea.backends.adapters.catalog.AdapterType`
- the list of backend modules under `mellea/backends/`
- the per-package class / dataclass / Pydantic-model inventory you want to reflect in the schema's `coverage_inventory` annotation

The generator is **idempotent** — running it twice in a row produces the same output (modulo the `version` / `generated_on` date fields).

## How to run

From the `linkml/` workspace folder:

```bash
just regen-schema    # writes linkml/src/mellea/schema/mellea.yaml
just lint            # validates the regenerated schema
just gen-project     # regenerates Pydantic / Java / TS / OWL artifacts
just test            # runs the LinkML project test suite
```

Or invoke the script directly:

```bash
uv run python linkml/scripts/schema_to_linkml.py
uv run python linkml/scripts/schema_to_linkml.py --stdout | diff - src/mellea/schema/mellea.yaml
```

## What gets re-derived

| Schema element                | Source of truth                              |
|------------------------------|-----------------------------------------------|
| `PluginModeEnum`             | `mellea/plugins/types.py::PluginMode`        |
| `HookTypeEnum`               | `mellea/plugins/types.py::HookType`          |
| `AdapterTypeEnum`            | `mellea/backends/adapters/catalog.py::AdapterType` |
| `BackendFamilyEnum`          | `mellea/backends/*.py` filenames             |
| `coverage_inventory` annotation | AST scan of `mellea/` + `cli/`            |

The architectural classes, slots, subsets, and types are hand-curated in the generator (see the top of `schema_to_linkml.py`) — they describe the *shape* of the schema rather than a per-symbol mirror of the codebase.

## Test fixtures

A sibling generator [`gen_test_fixtures.py`](./gen_test_fixtures.py) extracts real upstream data into LinkML-compatible YAML fixtures used to validate the schema. Each fixture is named `<ClassName>-<desc>.yaml` so the loader in [`tests/test_data.py`](../tests/test_data.py) can dispatch it to the right generated Pydantic class.

| Fixture pattern                          | Source of truth                              |
|------------------------------------------|----------------------------------------------|
| `BackendSpec-<family>.yaml`              | `mellea/backends/*.py` filenames             |
| `IntrinsicAdapterSpec-<name>.yaml`       | `mellea/backends/adapters/catalog.py`        |
| `ModelIdentifierSpec-<const>.yaml`       | `mellea/backends/model_ids.py`               |

The generator also writes a small set of hand-curated counter-examples to `tests/data/invalid/` that intentionally violate the schema (missing required slots, unknown enum values). `just test` runs them through `linkml-run-examples` to confirm validation actually rejects them.

Run with:

```bash
just regen-fixtures     # refresh tests/data/{valid,invalid}/
just test               # validate (pytest + linkml-run-examples)
```

Only files starting with the auto-generated header are purged on re-run, so additional hand-authored fixtures placed in either directory are preserved.

## Adding a new auto-derived enum

1. Locate the source `Enum` / `StrEnum` class you want to mirror.
2. Add a call to `find_enum(...)` + `build_enum_from_source(...)` inside `build_enums()` in [`schema_to_linkml.py`](./schema_to_linkml.py).
3. Run `just regen-schema && just lint && just gen-project`.
