## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============== Generators ==============
#
# These recipes regenerate artifacts under linkml/ from the live Mellea
# Python sources. They are idempotent: re-run after any upstream code change
# (new enum value, new backend module, new intrinsic, ...) to refresh.

# Regenerate the LinkML schema YAML (src/mellea/schema/mellea.yaml) from the
# live Mellea Python sources (enums, backend modules, package inventory).
[group('generators')]
gen-linkml:
  uv run python scripts/schema_to_linkml.py

# Regenerate test fixtures under tests/data/{valid,invalid}/ from the live
# Mellea sources (backend modules, intrinsics catalog, model_ids.py). Run
# after `gen-linkml` so the fixtures stay in sync with the schema.
[group('generators')]
gen-fixtures:
  uv run python scripts/gen_test_fixtures.py

# Apply curated SSSOM mapping TSVs to the generated LinkML schema YAMLs (idempotent).
[group('model development')]
apply-sssom-overlay:
  uv run python scripts/apply_sssom_overlay.py \
    --schema-dir src/mellea/schema \
    --mappings-dir src/mellea/mappings

# Convenience: refresh Linkml schema, sssom mappings, and test fixtures.
[group('generators')]
regen-all: gen-linkml gen-fixtures apply-sssom-overlay

# Convenience: full regenerate + validate pipeline. Useful after an upstream
# Mellea refactor to confirm the schema is still consistent and all fixtures
# still validate.
[group('generators')]
regen-and-test: regen-all lint gen-project test

# ============== Supplemental generator recipes (beyond gen-project defaults) ==============
# gen-project already covers: graphql, jsonldcontext, jsonld, jsonschema, owl,
# prefixmap, proto, python, shex, shacl, sqlddl, excel, typescript.
# Explicit in main justfile: java, typescript (dup), owl (dup), pydantic (→ datamodel/).
# The recipes below cover the remaining available generators.
# Run all at once with: just gen-project-extended

# ---- Schema / metadata formats ----

# NOTE: recipe named gen-merged-schema to avoid conflict with CDM's gen-linkml recipe
# Generate a single self-contained merged LinkML YAML with all imports resolved
[group('model development - extended')]
gen-merged-schema:
  mkdir -p {{dest}}/linkml
  uv run gen-linkml --mergeimports -o {{dest}}/linkml/{{schema_name}}.merged.linkml.yaml {{source_schema_path}}

# gen-yaml CLI hits the linkml-runtime 1.11.0 RepresenterError (JsonObj missing SafeDumper representer).
# Use the same patched script as _gen-yaml until linkml-runtime > 1.11.0 lands.
# Generate resolved YAML schema (patched yamlgen)
[group('model development - extended')]
gen-yaml-artifact:
  mkdir -p {{dest}}/yaml
  uv run python scripts/patched/gen_yaml_patched.py {{source_schema_path}} > {{dest}}/yaml/{{schema_name}}.yaml

# Generate SSSOM mapping TSV from schema slot_uri / mappings
[group('model development - extended')]
gen-sssom-artifact:
  mkdir -p {{dest}}/sssom
  uv run gen-sssom --mergeimports -o {{dest}}/sssom/{{schema_name}}.sssom.tsv {{source_schema_path}}

# Generate Python namespace manager for all prefixes in the schema
[group('model development - extended')]
gen-namespaces-artifact:
  mkdir -p {{dest}}/namespaces
  uv run gen-namespaces --mergeimports {{source_schema_path}} > {{dest}}/namespaces/{{schema_name}}.namespaces.py

# Generate TSV summary (classes, slots, counts — useful in spreadsheets)
[group('model development - extended')]
gen-summary-artifact:
  mkdir -p {{dest}}/summary
  uv run gen-summary --mergeimports {{source_schema_path}} > {{dest}}/summary/{{schema_name}}.summary.tsv

# ---- Visualization / diagram formats ----

# Generate a single combined Graphviz DOT graph of the schema
[group('model development - extended')]
gen-graphviz-artifact:
  mkdir -p {{dest}}/graphviz
  uv run gen-graphviz --mergeimports -f dot -o {{dest}}/graphviz/{{schema_name}}.dot {{source_schema_path}}

# Generate per-class Mermaid class diagram Markdown files (one .md per class)
[group('model development - extended')]
gen-mermaid-artifact:
  mkdir -p {{dest}}/mermaid
  uv run gen-mermaid-class-diagram --mergeimports -d {{dest}}/mermaid {{source_schema_path}}

# Generate Mermaid ER diagram (single file, mermaid format)
[group('model development - extended')]
gen-erdiagram-artifact:
  mkdir -p {{dest}}/erdiagram
  uv run gen-erdiagram --mergeimports -f mermaid {{source_schema_path}} > {{dest}}/erdiagram/{{schema_name}}.er.md

# Generate PlantUML diagram (stdout → single file)
[group('model development - extended')]
gen-plantuml-artifact:
  mkdir -p {{dest}}/plantuml
  uv run gen-plantuml --mergeimports {{source_schema_path}} > {{dest}}/plantuml/{{schema_name}}.plantuml

# ---- Data / query formats ----

# gen-rdf embeds ./cdm_*.context.jsonld refs that rdflib resolves against the
# schema @base URL (https://w3id.org/lmodel/…), returning HTTP 404. Patched
# script strips those refs; all prefix bindings are in the merged context.
# Generate RDF/Turtle representation of the schema
[group('model development - extended')]
gen-rdf-artifact:
  mkdir -p {{dest}}/rdf
  uv run python scripts/patched/gen_rdf_patched.py --mergeimports -o {{dest}}/rdf/{{schema_name}}.ttl {{source_schema_path}}

# Generate a directory of SPARQL validation queries (one query per constraint)
[group('model development - extended')]
gen-sparql-artifact:
  mkdir -p {{dest}}/sparql
  uv run gen-sparql --mergeimports -d {{dest}}/sparql {{source_schema_path}}

# Generate CSV data dictionary of classes and slots
[group('model development - extended')]
gen-csv-artifact:
  mkdir -p {{dest}}/csv
  uv run gen-csv --mergeimports {{source_schema_path}} > {{dest}}/csv/{{schema_name}}.csv

# ---- Database formats ----

# Generate DBML (Database Markup Language) for schema visualization tools (DBDiagram etc.)
[group('model development - extended')]
gen-dbml-artifact:
  mkdir -p {{dest}}/dbml
  uv run python3 scripts/patched/gen_dbml_patched.py -s {{source_schema_path}} -o {{dest}}/dbml/{{schema_name}}.dbml

# Generate SQLAlchemy ORM models
[group('model development - extended')]
gen-sqla-artifact:
  mkdir -p {{dest}}/sqla
  uv run gen-sqla --mergeimports {{source_schema_path}} > {{dest}}/sqla/{{schema_name}}_sqlalchemy.py

# Generate SQL validation queries
[group('model development - extended')]
gen-sqlvalidation-artifact:
  mkdir -p {{dest}}/sqlvalidation
  uv run gen-sqlvalidation --mergeimports {{source_schema_path}} > {{dest}}/sqlvalidation/{{schema_name}}.sql

# Generate TerminusDB JSON-LD schema
[group('model development - extended')]
gen-terminusdb-artifact:
  mkdir -p {{dest}}/terminusdb
  uv run gen-terminusdb --mergeimports {{source_schema_path}} > {{dest}}/terminusdb/{{schema_name}}.json

# Generate TypeDB TypeQL schema definitions
[group('model development - extended')]
gen-typedb-artifact:
  mkdir -p {{dest}}/typedb
  uv run gen-typedb --mergeimports {{source_schema_path}} > {{dest}}/typedb/{{schema_name}}.tql

# ---- Language bindings ----

# Generate Go structs (stdout → single file)
[group('model development - extended')]
gen-golang-artifact:
  mkdir -p {{dest}}/golang
  uv run gen-golang --mergeimports {{source_schema_path}} > {{dest}}/golang/{{schema_name}}.go

# Generate Rust crate (directory with Cargo.toml + src/)
[group('model development - extended')]
gen-rust-artifact:
  mkdir -p {{dest}}/rust
  uv run gen-rust --mergeimports --force -o {{dest}}/rust {{source_schema_path}}

# Generate C++17 header file
[group('model development - extended')]
gen-cpp-artifact:
  mkdir -p {{dest}}/cpp
  uv run gen-cpp-header --mergeimports {{source_schema_path}} > {{dest}}/cpp/{{schema_name}}.h

# Generate Pandera dataframe validation schemas
[group('model development - extended')]
gen-pandera-artifact:
  mkdir -p {{dest}}/pandera
  uv run python3 scripts/patched/gen_pandera_patched.py {{source_schema_path}} > {{dest}}/pandera/{{schema_name}}_pandera.py

# Generate Markdown data dictionary (single combined file)
# NOTE Bug 12: gen-markdown-datadict creates a new ERDiagramGenerator (and
# therefore re-loads the full CDM schema) for every one of the 2500+ CDM
# classes, hanging indefinitely.  scripts/gen_markdown_datadict_patched.py
# overrides _generate_class_diagram to cache one ERDiagramGenerator instance.
[group('model development - extended')]
gen-markdown-datadict-artifact:
  mkdir -p {{dest}}/markdown-datadict
  uv run python3 scripts/patched/gen_markdown_datadict_patched.py --mergeimports {{source_schema_path}} > {{dest}}/markdown-datadict/{{schema_name}}.md

# Generate GOLR (SOLR) view configurations (one JSON per class)
[group('model development - extended')]
gen-golr-artifact:
  mkdir -p {{dest}}/golr
  uv run gen-golr-views --mergeimports -d {{dest}}/golr {{source_schema_path}}

# ---- Aggregate ----

# Usage: just gen-project && just gen-project-extended
# Run all supplemental generators (those not already covered by gen-project)
[group('model development - extended')]
gen-project-extended: \
  gen-merged-schema \
  gen-yaml-artifact \
  gen-sssom-artifact \
  gen-namespaces-artifact \
  gen-summary-artifact \
  gen-graphviz-artifact \
  gen-mermaid-artifact \
  gen-erdiagram-artifact \
  gen-plantuml-artifact \
  gen-rdf-artifact \
  gen-sparql-artifact \
  gen-csv-artifact \
  gen-dbml-artifact \
  gen-sqla-artifact \
  gen-sqlvalidation-artifact \
  gen-terminusdb-artifact \
  gen-typedb-artifact \
  gen-golang-artifact \
  gen-rust-artifact \
  gen-cpp-artifact \
  gen-pandera-artifact \
  gen-markdown-datadict-artifact \
  gen-golr-artifact
