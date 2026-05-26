-- # Abstract Class: NamedElement Description: Abstract base for any named, identifiable schema element.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
-- # Class: RepositoryCatalog Description: Top-level catalog rooting the analysed repository snapshot.
--     * Slot: repository_root Description: Slot describing the repository root.
--     * Slot: analyzed_on Description: Slot describing the analyzed on.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
-- # Class: PythonPackage Description: A logical Python package (directory) inside the repository.
--     * Slot: package_name Description: Slot describing the package name.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
--     * Slot: PythonPackage_id Description: Autocreated FK slot
-- # Abstract Class: ModelElement Description: Abstract base for concrete architectural elements.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
--     * Slot: RepositoryCatalog_id Description: Autocreated FK slot
--     * Slot: PythonPackage_id Description: Autocreated FK slot
-- # Class: BackendSpec Description: Specification of a Mellea backend implementation.
--     * Slot: backend_family Description: Slot describing the backend family.
--     * Slot: default_formatter Description: Slot describing the default formatter.
--     * Slot: supports_streaming Description: Slot describing the supports streaming.
--     * Slot: supports_tool_calls Description: Slot describing the supports tool calls.
--     * Slot: supports_multimodal Description: Slot describing the supports multimodal.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
-- # Class: FormatterSpec Description: Specification of an output formatter for a backend.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
-- # Class: ContextSpec Description: Specification of a context implementation.
--     * Slot: context_linearity Description: Slot describing the context linearity.
--     * Slot: stores_component_history Description: Slot describing the stores component history.
--     * Slot: accepts_message_attachments Description: Slot describing the accepts message attachments.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
-- # Class: SessionSpec Description: Specification of a Mellea session.
--     * Slot: uses_backend Description: Slot describing the uses backend.
--     * Slot: uses_context Description: Slot describing the uses context.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
-- # Class: ComponentSpec Description: Specification of a Mellea stdlib component type.
--     * Slot: component_category Description: Slot describing the component category.
--     * Slot: parsed_output_type Description: Slot describing the parsed output type.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
-- # Class: RequirementSpec Description: Specification of a requirement validator.
--     * Slot: validation_style Description: Slot describing the validation style.
--     * Slot: may_trigger_repair Description: Slot describing the may trigger repair.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
-- # Class: SamplingStrategySpec Description: Specification of a sampling-loop strategy.
--     * Slot: selection_policy Description: Slot describing the selection policy.
--     * Slot: loop_budget_hint Description: Slot describing the loop budget hint.
--     * Slot: may_trigger_repair Description: Slot describing the may trigger repair.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
-- # Class: PluginSpec Description: Specification of a Mellea plugin and the hooks it registers.
--     * Slot: plugin_mode Description: Slot describing the plugin mode.
--     * Slot: plugin_priority Description: Slot describing the plugin priority.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
-- # Class: HookPayloadSpec Description: Specification of a hook payload model.
--     * Slot: lifecycle_role Description: Slot describing the lifecycle role.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
--     * Slot: PluginSpec_id Description: Autocreated FK slot
-- # Class: TelemetryMetricSpec Description: Specification of a telemetry metric emitted by Mellea.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
-- # Class: CliCommandSpec Description: Specification of a CLI command exposed under `m`.
--     * Slot: command_group Description: Slot describing the command group.
--     * Slot: command_path Description: Slot describing the command path.
--     * Slot: command_purpose Description: Slot describing the command purpose.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
-- # Class: ApiModelSpec Description: Specification of an HTTP API wire model.
--     * Slot: request_or_response Description: Slot describing the request or response.
--     * Slot: openai_object_type Description: Slot describing the openai object type.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
--     * Slot: CliCommandSpec_id Description: Autocreated FK slot
-- # Class: ApiFieldSpec Description: Specification of a single field in an API model.
--     * Slot: field_name Description: Slot describing the field name.
--     * Slot: field_type Description: Slot describing the field type.
--     * Slot: required_field Description: Slot describing the required field.
--     * Slot: allows_null Description: Slot describing the allows null.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
--     * Slot: ApiModelSpec_id Description: Autocreated FK slot
-- # Class: MethodSpec Description: Specification of a method exposed by a runtime class.
--     * Slot: method_name Description: Slot describing the method name.
--     * Slot: method_signature Description: Slot describing the method signature.
--     * Slot: lifecycle_role Description: Slot describing the lifecycle role.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
--     * Slot: SessionSpec_id Description: Autocreated FK slot
-- # Class: ModelIdentifierSpec Description: Cross-provider identifier table for a single model.
--     * Slot: hf_model_name Description: Slot describing the hf model name.
--     * Slot: ollama_name Description: Slot describing the ollama name.
--     * Slot: watsonx_name Description: Slot describing the watsonx name.
--     * Slot: openai_name Description: Slot describing the openai name.
--     * Slot: bedrock_name Description: Slot describing the bedrock name.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
--     * Slot: BackendSpec_id Description: Autocreated FK slot
-- # Class: IntrinsicAdapterSpec Description: Specification of an intrinsic adapter (LoRA / aLoRA).
--     * Slot: repo_id Description: Slot describing the repo id.
--     * Slot: id Description: Stable identifier for a schema element.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Narrative description of the element.
--     * Slot: module_path Description: Python module path where this element is defined.
--     * Slot: source_file Description: Source file relative to repository root.
--     * Slot: package_kind Description: Package bucket.
--     * Slot: element_kind Description: Kind of Python declaration.
-- # Class: NamedElement_coverage_scope
--     * Slot: NamedElement_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: NamedElement_tags
--     * Slot: NamedElement_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: RepositoryCatalog_includes_path
--     * Slot: RepositoryCatalog_id Description: Autocreated FK slot
--     * Slot: includes_path Description: Slot describing the includes path.
-- # Class: RepositoryCatalog_excludes_path
--     * Slot: RepositoryCatalog_id Description: Autocreated FK slot
--     * Slot: excludes_path Description: Slot describing the excludes path.
-- # Class: RepositoryCatalog_coverage_scope
--     * Slot: RepositoryCatalog_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: RepositoryCatalog_tags
--     * Slot: RepositoryCatalog_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: PythonPackage_coverage_scope
--     * Slot: PythonPackage_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: PythonPackage_tags
--     * Slot: PythonPackage_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: ModelElement_coverage_scope
--     * Slot: ModelElement_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: ModelElement_tags
--     * Slot: ModelElement_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: BackendSpec_model_options_key
--     * Slot: BackendSpec_id Description: Autocreated FK slot
--     * Slot: model_options_key Description: Slot describing the model options key.
-- # Class: BackendSpec_coverage_scope
--     * Slot: BackendSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: BackendSpec_tags
--     * Slot: BackendSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: FormatterSpec_coverage_scope
--     * Slot: FormatterSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: FormatterSpec_tags
--     * Slot: FormatterSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: ContextSpec_coverage_scope
--     * Slot: ContextSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: ContextSpec_tags
--     * Slot: ContextSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: SessionSpec_coverage_scope
--     * Slot: SessionSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: SessionSpec_tags
--     * Slot: SessionSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: ComponentSpec_input_modality
--     * Slot: ComponentSpec_id Description: Autocreated FK slot
--     * Slot: input_modality Description: Slot describing the input modality.
-- # Class: ComponentSpec_coverage_scope
--     * Slot: ComponentSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: ComponentSpec_tags
--     * Slot: ComponentSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: RequirementSpec_coverage_scope
--     * Slot: RequirementSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: RequirementSpec_tags
--     * Slot: RequirementSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: SamplingStrategySpec_coverage_scope
--     * Slot: SamplingStrategySpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: SamplingStrategySpec_tags
--     * Slot: SamplingStrategySpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: PluginSpec_hook_type
--     * Slot: PluginSpec_id Description: Autocreated FK slot
--     * Slot: hook_type Description: Slot describing the hook type.
-- # Class: PluginSpec_coverage_scope
--     * Slot: PluginSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: PluginSpec_tags
--     * Slot: PluginSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: HookPayloadSpec_hook_type
--     * Slot: HookPayloadSpec_id Description: Autocreated FK slot
--     * Slot: hook_type Description: Slot describing the hook type.
-- # Class: HookPayloadSpec_coverage_scope
--     * Slot: HookPayloadSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: HookPayloadSpec_tags
--     * Slot: HookPayloadSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: TelemetryMetricSpec_metric_name
--     * Slot: TelemetryMetricSpec_id Description: Autocreated FK slot
--     * Slot: metric_name Description: Slot describing the metric name.
-- # Class: TelemetryMetricSpec_coverage_scope
--     * Slot: TelemetryMetricSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: TelemetryMetricSpec_tags
--     * Slot: TelemetryMetricSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: CliCommandSpec_coverage_scope
--     * Slot: CliCommandSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: CliCommandSpec_tags
--     * Slot: CliCommandSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: ApiModelSpec_coverage_scope
--     * Slot: ApiModelSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: ApiModelSpec_tags
--     * Slot: ApiModelSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: ApiFieldSpec_coverage_scope
--     * Slot: ApiFieldSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: ApiFieldSpec_tags
--     * Slot: ApiFieldSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: MethodSpec_coverage_scope
--     * Slot: MethodSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: MethodSpec_tags
--     * Slot: MethodSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: ModelIdentifierSpec_provider_name
--     * Slot: ModelIdentifierSpec_id Description: Autocreated FK slot
--     * Slot: provider_name Description: Slot describing the provider name.
-- # Class: ModelIdentifierSpec_coverage_scope
--     * Slot: ModelIdentifierSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: ModelIdentifierSpec_tags
--     * Slot: ModelIdentifierSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.
-- # Class: IntrinsicAdapterSpec_adapter_type
--     * Slot: IntrinsicAdapterSpec_id Description: Autocreated FK slot
--     * Slot: adapter_type Description: Slot describing the adapter type.
-- # Class: IntrinsicAdapterSpec_coverage_scope
--     * Slot: IntrinsicAdapterSpec_id Description: Autocreated FK slot
--     * Slot: coverage_scope Description: Where this element surfaces (source/API/CLI/example/test).
-- # Class: IntrinsicAdapterSpec_tags
--     * Slot: IntrinsicAdapterSpec_id Description: Autocreated FK slot
--     * Slot: tags Description: Free-form classification tags.

CREATE TABLE "NamedElement" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NamedElement_id" ON "NamedElement" (id);

CREATE TABLE "RepositoryCatalog" (
	repository_root TEXT,
	analyzed_on DATE,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RepositoryCatalog_id" ON "RepositoryCatalog" (id);

CREATE TABLE "PythonPackage" (
	package_name TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	"PythonPackage_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PythonPackage_id") REFERENCES "PythonPackage" (id)
);
CREATE INDEX "ix_PythonPackage_id" ON "PythonPackage" (id);

CREATE TABLE "FormatterSpec" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_FormatterSpec_id" ON "FormatterSpec" (id);

CREATE TABLE "ContextSpec" (
	context_linearity VARCHAR(10),
	stores_component_history BOOLEAN,
	accepts_message_attachments BOOLEAN,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ContextSpec_id" ON "ContextSpec" (id);

CREATE TABLE "ComponentSpec" (
	component_category VARCHAR(12),
	parsed_output_type TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ComponentSpec_id" ON "ComponentSpec" (id);

CREATE TABLE "RequirementSpec" (
	validation_style TEXT,
	may_trigger_repair BOOLEAN,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RequirementSpec_id" ON "RequirementSpec" (id);

CREATE TABLE "SamplingStrategySpec" (
	selection_policy TEXT,
	loop_budget_hint INTEGER,
	may_trigger_repair BOOLEAN,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SamplingStrategySpec_id" ON "SamplingStrategySpec" (id);

CREATE TABLE "PluginSpec" (
	plugin_mode VARCHAR(15),
	plugin_priority INTEGER,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PluginSpec_id" ON "PluginSpec" (id);

CREATE TABLE "TelemetryMetricSpec" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TelemetryMetricSpec_id" ON "TelemetryMetricSpec" (id);

CREATE TABLE "CliCommandSpec" (
	command_group TEXT,
	command_path TEXT,
	command_purpose TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CliCommandSpec_id" ON "CliCommandSpec" (id);

CREATE TABLE "IntrinsicAdapterSpec" (
	repo_id TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_IntrinsicAdapterSpec_id" ON "IntrinsicAdapterSpec" (id);

CREATE TABLE "ModelElement" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	"RepositoryCatalog_id" TEXT,
	"PythonPackage_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("RepositoryCatalog_id") REFERENCES "RepositoryCatalog" (id),
	FOREIGN KEY("PythonPackage_id") REFERENCES "PythonPackage" (id)
);
CREATE INDEX "ix_ModelElement_id" ON "ModelElement" (id);

CREATE TABLE "BackendSpec" (
	backend_family VARCHAR(11),
	default_formatter TEXT,
	supports_streaming BOOLEAN,
	supports_tool_calls BOOLEAN,
	supports_multimodal BOOLEAN,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	PRIMARY KEY (id),
	FOREIGN KEY(default_formatter) REFERENCES "FormatterSpec" (id)
);
CREATE INDEX "ix_BackendSpec_id" ON "BackendSpec" (id);

CREATE TABLE "HookPayloadSpec" (
	lifecycle_role TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	"PluginSpec_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PluginSpec_id") REFERENCES "PluginSpec" (id)
);
CREATE INDEX "ix_HookPayloadSpec_id" ON "HookPayloadSpec" (id);

CREATE TABLE "ApiModelSpec" (
	request_or_response VARCHAR(8),
	openai_object_type TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	"CliCommandSpec_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CliCommandSpec_id") REFERENCES "CliCommandSpec" (id)
);
CREATE INDEX "ix_ApiModelSpec_id" ON "ApiModelSpec" (id);

CREATE TABLE "NamedElement_coverage_scope" (
	"NamedElement_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("NamedElement_id", coverage_scope),
	FOREIGN KEY("NamedElement_id") REFERENCES "NamedElement" (id)
);
CREATE INDEX "ix_NamedElement_coverage_scope_NamedElement_id" ON "NamedElement_coverage_scope" ("NamedElement_id");
CREATE INDEX "ix_NamedElement_coverage_scope_coverage_scope" ON "NamedElement_coverage_scope" (coverage_scope);

CREATE TABLE "NamedElement_tags" (
	"NamedElement_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("NamedElement_id", tags),
	FOREIGN KEY("NamedElement_id") REFERENCES "NamedElement" (id)
);
CREATE INDEX "ix_NamedElement_tags_NamedElement_id" ON "NamedElement_tags" ("NamedElement_id");
CREATE INDEX "ix_NamedElement_tags_tags" ON "NamedElement_tags" (tags);

CREATE TABLE "RepositoryCatalog_includes_path" (
	"RepositoryCatalog_id" TEXT,
	includes_path TEXT,
	PRIMARY KEY ("RepositoryCatalog_id", includes_path),
	FOREIGN KEY("RepositoryCatalog_id") REFERENCES "RepositoryCatalog" (id)
);
CREATE INDEX "ix_RepositoryCatalog_includes_path_RepositoryCatalog_id" ON "RepositoryCatalog_includes_path" ("RepositoryCatalog_id");
CREATE INDEX "ix_RepositoryCatalog_includes_path_includes_path" ON "RepositoryCatalog_includes_path" (includes_path);

CREATE TABLE "RepositoryCatalog_excludes_path" (
	"RepositoryCatalog_id" TEXT,
	excludes_path TEXT,
	PRIMARY KEY ("RepositoryCatalog_id", excludes_path),
	FOREIGN KEY("RepositoryCatalog_id") REFERENCES "RepositoryCatalog" (id)
);
CREATE INDEX "ix_RepositoryCatalog_excludes_path_RepositoryCatalog_id" ON "RepositoryCatalog_excludes_path" ("RepositoryCatalog_id");
CREATE INDEX "ix_RepositoryCatalog_excludes_path_excludes_path" ON "RepositoryCatalog_excludes_path" (excludes_path);

CREATE TABLE "RepositoryCatalog_coverage_scope" (
	"RepositoryCatalog_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("RepositoryCatalog_id", coverage_scope),
	FOREIGN KEY("RepositoryCatalog_id") REFERENCES "RepositoryCatalog" (id)
);
CREATE INDEX "ix_RepositoryCatalog_coverage_scope_RepositoryCatalog_id" ON "RepositoryCatalog_coverage_scope" ("RepositoryCatalog_id");
CREATE INDEX "ix_RepositoryCatalog_coverage_scope_coverage_scope" ON "RepositoryCatalog_coverage_scope" (coverage_scope);

CREATE TABLE "RepositoryCatalog_tags" (
	"RepositoryCatalog_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("RepositoryCatalog_id", tags),
	FOREIGN KEY("RepositoryCatalog_id") REFERENCES "RepositoryCatalog" (id)
);
CREATE INDEX "ix_RepositoryCatalog_tags_RepositoryCatalog_id" ON "RepositoryCatalog_tags" ("RepositoryCatalog_id");
CREATE INDEX "ix_RepositoryCatalog_tags_tags" ON "RepositoryCatalog_tags" (tags);

CREATE TABLE "PythonPackage_coverage_scope" (
	"PythonPackage_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("PythonPackage_id", coverage_scope),
	FOREIGN KEY("PythonPackage_id") REFERENCES "PythonPackage" (id)
);
CREATE INDEX "ix_PythonPackage_coverage_scope_PythonPackage_id" ON "PythonPackage_coverage_scope" ("PythonPackage_id");
CREATE INDEX "ix_PythonPackage_coverage_scope_coverage_scope" ON "PythonPackage_coverage_scope" (coverage_scope);

CREATE TABLE "PythonPackage_tags" (
	"PythonPackage_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("PythonPackage_id", tags),
	FOREIGN KEY("PythonPackage_id") REFERENCES "PythonPackage" (id)
);
CREATE INDEX "ix_PythonPackage_tags_PythonPackage_id" ON "PythonPackage_tags" ("PythonPackage_id");
CREATE INDEX "ix_PythonPackage_tags_tags" ON "PythonPackage_tags" (tags);

CREATE TABLE "FormatterSpec_coverage_scope" (
	"FormatterSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("FormatterSpec_id", coverage_scope),
	FOREIGN KEY("FormatterSpec_id") REFERENCES "FormatterSpec" (id)
);
CREATE INDEX "ix_FormatterSpec_coverage_scope_coverage_scope" ON "FormatterSpec_coverage_scope" (coverage_scope);
CREATE INDEX "ix_FormatterSpec_coverage_scope_FormatterSpec_id" ON "FormatterSpec_coverage_scope" ("FormatterSpec_id");

CREATE TABLE "FormatterSpec_tags" (
	"FormatterSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("FormatterSpec_id", tags),
	FOREIGN KEY("FormatterSpec_id") REFERENCES "FormatterSpec" (id)
);
CREATE INDEX "ix_FormatterSpec_tags_tags" ON "FormatterSpec_tags" (tags);
CREATE INDEX "ix_FormatterSpec_tags_FormatterSpec_id" ON "FormatterSpec_tags" ("FormatterSpec_id");

CREATE TABLE "ContextSpec_coverage_scope" (
	"ContextSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("ContextSpec_id", coverage_scope),
	FOREIGN KEY("ContextSpec_id") REFERENCES "ContextSpec" (id)
);
CREATE INDEX "ix_ContextSpec_coverage_scope_ContextSpec_id" ON "ContextSpec_coverage_scope" ("ContextSpec_id");
CREATE INDEX "ix_ContextSpec_coverage_scope_coverage_scope" ON "ContextSpec_coverage_scope" (coverage_scope);

CREATE TABLE "ContextSpec_tags" (
	"ContextSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("ContextSpec_id", tags),
	FOREIGN KEY("ContextSpec_id") REFERENCES "ContextSpec" (id)
);
CREATE INDEX "ix_ContextSpec_tags_ContextSpec_id" ON "ContextSpec_tags" ("ContextSpec_id");
CREATE INDEX "ix_ContextSpec_tags_tags" ON "ContextSpec_tags" (tags);

CREATE TABLE "ComponentSpec_input_modality" (
	"ComponentSpec_id" TEXT,
	input_modality TEXT,
	PRIMARY KEY ("ComponentSpec_id", input_modality),
	FOREIGN KEY("ComponentSpec_id") REFERENCES "ComponentSpec" (id)
);
CREATE INDEX "ix_ComponentSpec_input_modality_input_modality" ON "ComponentSpec_input_modality" (input_modality);
CREATE INDEX "ix_ComponentSpec_input_modality_ComponentSpec_id" ON "ComponentSpec_input_modality" ("ComponentSpec_id");

CREATE TABLE "ComponentSpec_coverage_scope" (
	"ComponentSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("ComponentSpec_id", coverage_scope),
	FOREIGN KEY("ComponentSpec_id") REFERENCES "ComponentSpec" (id)
);
CREATE INDEX "ix_ComponentSpec_coverage_scope_coverage_scope" ON "ComponentSpec_coverage_scope" (coverage_scope);
CREATE INDEX "ix_ComponentSpec_coverage_scope_ComponentSpec_id" ON "ComponentSpec_coverage_scope" ("ComponentSpec_id");

CREATE TABLE "ComponentSpec_tags" (
	"ComponentSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("ComponentSpec_id", tags),
	FOREIGN KEY("ComponentSpec_id") REFERENCES "ComponentSpec" (id)
);
CREATE INDEX "ix_ComponentSpec_tags_ComponentSpec_id" ON "ComponentSpec_tags" ("ComponentSpec_id");
CREATE INDEX "ix_ComponentSpec_tags_tags" ON "ComponentSpec_tags" (tags);

CREATE TABLE "RequirementSpec_coverage_scope" (
	"RequirementSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("RequirementSpec_id", coverage_scope),
	FOREIGN KEY("RequirementSpec_id") REFERENCES "RequirementSpec" (id)
);
CREATE INDEX "ix_RequirementSpec_coverage_scope_coverage_scope" ON "RequirementSpec_coverage_scope" (coverage_scope);
CREATE INDEX "ix_RequirementSpec_coverage_scope_RequirementSpec_id" ON "RequirementSpec_coverage_scope" ("RequirementSpec_id");

CREATE TABLE "RequirementSpec_tags" (
	"RequirementSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("RequirementSpec_id", tags),
	FOREIGN KEY("RequirementSpec_id") REFERENCES "RequirementSpec" (id)
);
CREATE INDEX "ix_RequirementSpec_tags_RequirementSpec_id" ON "RequirementSpec_tags" ("RequirementSpec_id");
CREATE INDEX "ix_RequirementSpec_tags_tags" ON "RequirementSpec_tags" (tags);

CREATE TABLE "SamplingStrategySpec_coverage_scope" (
	"SamplingStrategySpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("SamplingStrategySpec_id", coverage_scope),
	FOREIGN KEY("SamplingStrategySpec_id") REFERENCES "SamplingStrategySpec" (id)
);
CREATE INDEX "ix_SamplingStrategySpec_coverage_scope_SamplingStrategySpec_id" ON "SamplingStrategySpec_coverage_scope" ("SamplingStrategySpec_id");
CREATE INDEX "ix_SamplingStrategySpec_coverage_scope_coverage_scope" ON "SamplingStrategySpec_coverage_scope" (coverage_scope);

CREATE TABLE "SamplingStrategySpec_tags" (
	"SamplingStrategySpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("SamplingStrategySpec_id", tags),
	FOREIGN KEY("SamplingStrategySpec_id") REFERENCES "SamplingStrategySpec" (id)
);
CREATE INDEX "ix_SamplingStrategySpec_tags_tags" ON "SamplingStrategySpec_tags" (tags);
CREATE INDEX "ix_SamplingStrategySpec_tags_SamplingStrategySpec_id" ON "SamplingStrategySpec_tags" ("SamplingStrategySpec_id");

CREATE TABLE "PluginSpec_hook_type" (
	"PluginSpec_id" TEXT,
	hook_type VARCHAR(22),
	PRIMARY KEY ("PluginSpec_id", hook_type),
	FOREIGN KEY("PluginSpec_id") REFERENCES "PluginSpec" (id)
);
CREATE INDEX "ix_PluginSpec_hook_type_PluginSpec_id" ON "PluginSpec_hook_type" ("PluginSpec_id");
CREATE INDEX "ix_PluginSpec_hook_type_hook_type" ON "PluginSpec_hook_type" (hook_type);

CREATE TABLE "PluginSpec_coverage_scope" (
	"PluginSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("PluginSpec_id", coverage_scope),
	FOREIGN KEY("PluginSpec_id") REFERENCES "PluginSpec" (id)
);
CREATE INDEX "ix_PluginSpec_coverage_scope_PluginSpec_id" ON "PluginSpec_coverage_scope" ("PluginSpec_id");
CREATE INDEX "ix_PluginSpec_coverage_scope_coverage_scope" ON "PluginSpec_coverage_scope" (coverage_scope);

CREATE TABLE "PluginSpec_tags" (
	"PluginSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("PluginSpec_id", tags),
	FOREIGN KEY("PluginSpec_id") REFERENCES "PluginSpec" (id)
);
CREATE INDEX "ix_PluginSpec_tags_tags" ON "PluginSpec_tags" (tags);
CREATE INDEX "ix_PluginSpec_tags_PluginSpec_id" ON "PluginSpec_tags" ("PluginSpec_id");

CREATE TABLE "TelemetryMetricSpec_metric_name" (
	"TelemetryMetricSpec_id" TEXT,
	metric_name TEXT,
	PRIMARY KEY ("TelemetryMetricSpec_id", metric_name),
	FOREIGN KEY("TelemetryMetricSpec_id") REFERENCES "TelemetryMetricSpec" (id)
);
CREATE INDEX "ix_TelemetryMetricSpec_metric_name_TelemetryMetricSpec_id" ON "TelemetryMetricSpec_metric_name" ("TelemetryMetricSpec_id");
CREATE INDEX "ix_TelemetryMetricSpec_metric_name_metric_name" ON "TelemetryMetricSpec_metric_name" (metric_name);

CREATE TABLE "TelemetryMetricSpec_coverage_scope" (
	"TelemetryMetricSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("TelemetryMetricSpec_id", coverage_scope),
	FOREIGN KEY("TelemetryMetricSpec_id") REFERENCES "TelemetryMetricSpec" (id)
);
CREATE INDEX "ix_TelemetryMetricSpec_coverage_scope_TelemetryMetricSpec_id" ON "TelemetryMetricSpec_coverage_scope" ("TelemetryMetricSpec_id");
CREATE INDEX "ix_TelemetryMetricSpec_coverage_scope_coverage_scope" ON "TelemetryMetricSpec_coverage_scope" (coverage_scope);

CREATE TABLE "TelemetryMetricSpec_tags" (
	"TelemetryMetricSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("TelemetryMetricSpec_id", tags),
	FOREIGN KEY("TelemetryMetricSpec_id") REFERENCES "TelemetryMetricSpec" (id)
);
CREATE INDEX "ix_TelemetryMetricSpec_tags_tags" ON "TelemetryMetricSpec_tags" (tags);
CREATE INDEX "ix_TelemetryMetricSpec_tags_TelemetryMetricSpec_id" ON "TelemetryMetricSpec_tags" ("TelemetryMetricSpec_id");

CREATE TABLE "CliCommandSpec_coverage_scope" (
	"CliCommandSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("CliCommandSpec_id", coverage_scope),
	FOREIGN KEY("CliCommandSpec_id") REFERENCES "CliCommandSpec" (id)
);
CREATE INDEX "ix_CliCommandSpec_coverage_scope_CliCommandSpec_id" ON "CliCommandSpec_coverage_scope" ("CliCommandSpec_id");
CREATE INDEX "ix_CliCommandSpec_coverage_scope_coverage_scope" ON "CliCommandSpec_coverage_scope" (coverage_scope);

CREATE TABLE "CliCommandSpec_tags" (
	"CliCommandSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("CliCommandSpec_id", tags),
	FOREIGN KEY("CliCommandSpec_id") REFERENCES "CliCommandSpec" (id)
);
CREATE INDEX "ix_CliCommandSpec_tags_CliCommandSpec_id" ON "CliCommandSpec_tags" ("CliCommandSpec_id");
CREATE INDEX "ix_CliCommandSpec_tags_tags" ON "CliCommandSpec_tags" (tags);

CREATE TABLE "IntrinsicAdapterSpec_adapter_type" (
	"IntrinsicAdapterSpec_id" TEXT,
	adapter_type VARCHAR(5),
	PRIMARY KEY ("IntrinsicAdapterSpec_id", adapter_type),
	FOREIGN KEY("IntrinsicAdapterSpec_id") REFERENCES "IntrinsicAdapterSpec" (id)
);
CREATE INDEX "ix_IntrinsicAdapterSpec_adapter_type_IntrinsicAdapterSpec_id" ON "IntrinsicAdapterSpec_adapter_type" ("IntrinsicAdapterSpec_id");
CREATE INDEX "ix_IntrinsicAdapterSpec_adapter_type_adapter_type" ON "IntrinsicAdapterSpec_adapter_type" (adapter_type);

CREATE TABLE "IntrinsicAdapterSpec_coverage_scope" (
	"IntrinsicAdapterSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("IntrinsicAdapterSpec_id", coverage_scope),
	FOREIGN KEY("IntrinsicAdapterSpec_id") REFERENCES "IntrinsicAdapterSpec" (id)
);
CREATE INDEX "ix_IntrinsicAdapterSpec_coverage_scope_coverage_scope" ON "IntrinsicAdapterSpec_coverage_scope" (coverage_scope);
CREATE INDEX "ix_IntrinsicAdapterSpec_coverage_scope_IntrinsicAdapterSpec_id" ON "IntrinsicAdapterSpec_coverage_scope" ("IntrinsicAdapterSpec_id");

CREATE TABLE "IntrinsicAdapterSpec_tags" (
	"IntrinsicAdapterSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("IntrinsicAdapterSpec_id", tags),
	FOREIGN KEY("IntrinsicAdapterSpec_id") REFERENCES "IntrinsicAdapterSpec" (id)
);
CREATE INDEX "ix_IntrinsicAdapterSpec_tags_tags" ON "IntrinsicAdapterSpec_tags" (tags);
CREATE INDEX "ix_IntrinsicAdapterSpec_tags_IntrinsicAdapterSpec_id" ON "IntrinsicAdapterSpec_tags" ("IntrinsicAdapterSpec_id");

CREATE TABLE "SessionSpec" (
	uses_backend TEXT,
	uses_context TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	PRIMARY KEY (id),
	FOREIGN KEY(uses_backend) REFERENCES "BackendSpec" (id),
	FOREIGN KEY(uses_context) REFERENCES "ContextSpec" (id)
);
CREATE INDEX "ix_SessionSpec_id" ON "SessionSpec" (id);

CREATE TABLE "ApiFieldSpec" (
	field_name TEXT,
	field_type TEXT,
	required_field BOOLEAN,
	allows_null BOOLEAN,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	"ApiModelSpec_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ApiModelSpec_id") REFERENCES "ApiModelSpec" (id)
);
CREATE INDEX "ix_ApiFieldSpec_id" ON "ApiFieldSpec" (id);

CREATE TABLE "ModelIdentifierSpec" (
	hf_model_name TEXT,
	ollama_name TEXT,
	watsonx_name TEXT,
	openai_name TEXT,
	bedrock_name TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	"BackendSpec_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("BackendSpec_id") REFERENCES "BackendSpec" (id)
);
CREATE INDEX "ix_ModelIdentifierSpec_id" ON "ModelIdentifierSpec" (id);

CREATE TABLE "ModelElement_coverage_scope" (
	"ModelElement_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("ModelElement_id", coverage_scope),
	FOREIGN KEY("ModelElement_id") REFERENCES "ModelElement" (id)
);
CREATE INDEX "ix_ModelElement_coverage_scope_ModelElement_id" ON "ModelElement_coverage_scope" ("ModelElement_id");
CREATE INDEX "ix_ModelElement_coverage_scope_coverage_scope" ON "ModelElement_coverage_scope" (coverage_scope);

CREATE TABLE "ModelElement_tags" (
	"ModelElement_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("ModelElement_id", tags),
	FOREIGN KEY("ModelElement_id") REFERENCES "ModelElement" (id)
);
CREATE INDEX "ix_ModelElement_tags_ModelElement_id" ON "ModelElement_tags" ("ModelElement_id");
CREATE INDEX "ix_ModelElement_tags_tags" ON "ModelElement_tags" (tags);

CREATE TABLE "BackendSpec_model_options_key" (
	"BackendSpec_id" TEXT,
	model_options_key TEXT,
	PRIMARY KEY ("BackendSpec_id", model_options_key),
	FOREIGN KEY("BackendSpec_id") REFERENCES "BackendSpec" (id)
);
CREATE INDEX "ix_BackendSpec_model_options_key_model_options_key" ON "BackendSpec_model_options_key" (model_options_key);
CREATE INDEX "ix_BackendSpec_model_options_key_BackendSpec_id" ON "BackendSpec_model_options_key" ("BackendSpec_id");

CREATE TABLE "BackendSpec_coverage_scope" (
	"BackendSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("BackendSpec_id", coverage_scope),
	FOREIGN KEY("BackendSpec_id") REFERENCES "BackendSpec" (id)
);
CREATE INDEX "ix_BackendSpec_coverage_scope_BackendSpec_id" ON "BackendSpec_coverage_scope" ("BackendSpec_id");
CREATE INDEX "ix_BackendSpec_coverage_scope_coverage_scope" ON "BackendSpec_coverage_scope" (coverage_scope);

CREATE TABLE "BackendSpec_tags" (
	"BackendSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("BackendSpec_id", tags),
	FOREIGN KEY("BackendSpec_id") REFERENCES "BackendSpec" (id)
);
CREATE INDEX "ix_BackendSpec_tags_BackendSpec_id" ON "BackendSpec_tags" ("BackendSpec_id");
CREATE INDEX "ix_BackendSpec_tags_tags" ON "BackendSpec_tags" (tags);

CREATE TABLE "HookPayloadSpec_hook_type" (
	"HookPayloadSpec_id" TEXT,
	hook_type VARCHAR(22),
	PRIMARY KEY ("HookPayloadSpec_id", hook_type),
	FOREIGN KEY("HookPayloadSpec_id") REFERENCES "HookPayloadSpec" (id)
);
CREATE INDEX "ix_HookPayloadSpec_hook_type_HookPayloadSpec_id" ON "HookPayloadSpec_hook_type" ("HookPayloadSpec_id");
CREATE INDEX "ix_HookPayloadSpec_hook_type_hook_type" ON "HookPayloadSpec_hook_type" (hook_type);

CREATE TABLE "HookPayloadSpec_coverage_scope" (
	"HookPayloadSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("HookPayloadSpec_id", coverage_scope),
	FOREIGN KEY("HookPayloadSpec_id") REFERENCES "HookPayloadSpec" (id)
);
CREATE INDEX "ix_HookPayloadSpec_coverage_scope_coverage_scope" ON "HookPayloadSpec_coverage_scope" (coverage_scope);
CREATE INDEX "ix_HookPayloadSpec_coverage_scope_HookPayloadSpec_id" ON "HookPayloadSpec_coverage_scope" ("HookPayloadSpec_id");

CREATE TABLE "HookPayloadSpec_tags" (
	"HookPayloadSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("HookPayloadSpec_id", tags),
	FOREIGN KEY("HookPayloadSpec_id") REFERENCES "HookPayloadSpec" (id)
);
CREATE INDEX "ix_HookPayloadSpec_tags_tags" ON "HookPayloadSpec_tags" (tags);
CREATE INDEX "ix_HookPayloadSpec_tags_HookPayloadSpec_id" ON "HookPayloadSpec_tags" ("HookPayloadSpec_id");

CREATE TABLE "ApiModelSpec_coverage_scope" (
	"ApiModelSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("ApiModelSpec_id", coverage_scope),
	FOREIGN KEY("ApiModelSpec_id") REFERENCES "ApiModelSpec" (id)
);
CREATE INDEX "ix_ApiModelSpec_coverage_scope_ApiModelSpec_id" ON "ApiModelSpec_coverage_scope" ("ApiModelSpec_id");
CREATE INDEX "ix_ApiModelSpec_coverage_scope_coverage_scope" ON "ApiModelSpec_coverage_scope" (coverage_scope);

CREATE TABLE "ApiModelSpec_tags" (
	"ApiModelSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("ApiModelSpec_id", tags),
	FOREIGN KEY("ApiModelSpec_id") REFERENCES "ApiModelSpec" (id)
);
CREATE INDEX "ix_ApiModelSpec_tags_tags" ON "ApiModelSpec_tags" (tags);
CREATE INDEX "ix_ApiModelSpec_tags_ApiModelSpec_id" ON "ApiModelSpec_tags" ("ApiModelSpec_id");

CREATE TABLE "MethodSpec" (
	method_name TEXT,
	method_signature TEXT,
	lifecycle_role TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	module_path TEXT,
	source_file TEXT,
	package_kind VARCHAR(13),
	element_kind VARCHAR(14),
	"SessionSpec_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("SessionSpec_id") REFERENCES "SessionSpec" (id)
);
CREATE INDEX "ix_MethodSpec_id" ON "MethodSpec" (id);

CREATE TABLE "SessionSpec_coverage_scope" (
	"SessionSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("SessionSpec_id", coverage_scope),
	FOREIGN KEY("SessionSpec_id") REFERENCES "SessionSpec" (id)
);
CREATE INDEX "ix_SessionSpec_coverage_scope_SessionSpec_id" ON "SessionSpec_coverage_scope" ("SessionSpec_id");
CREATE INDEX "ix_SessionSpec_coverage_scope_coverage_scope" ON "SessionSpec_coverage_scope" (coverage_scope);

CREATE TABLE "SessionSpec_tags" (
	"SessionSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("SessionSpec_id", tags),
	FOREIGN KEY("SessionSpec_id") REFERENCES "SessionSpec" (id)
);
CREATE INDEX "ix_SessionSpec_tags_tags" ON "SessionSpec_tags" (tags);
CREATE INDEX "ix_SessionSpec_tags_SessionSpec_id" ON "SessionSpec_tags" ("SessionSpec_id");

CREATE TABLE "ApiFieldSpec_coverage_scope" (
	"ApiFieldSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("ApiFieldSpec_id", coverage_scope),
	FOREIGN KEY("ApiFieldSpec_id") REFERENCES "ApiFieldSpec" (id)
);
CREATE INDEX "ix_ApiFieldSpec_coverage_scope_ApiFieldSpec_id" ON "ApiFieldSpec_coverage_scope" ("ApiFieldSpec_id");
CREATE INDEX "ix_ApiFieldSpec_coverage_scope_coverage_scope" ON "ApiFieldSpec_coverage_scope" (coverage_scope);

CREATE TABLE "ApiFieldSpec_tags" (
	"ApiFieldSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("ApiFieldSpec_id", tags),
	FOREIGN KEY("ApiFieldSpec_id") REFERENCES "ApiFieldSpec" (id)
);
CREATE INDEX "ix_ApiFieldSpec_tags_ApiFieldSpec_id" ON "ApiFieldSpec_tags" ("ApiFieldSpec_id");
CREATE INDEX "ix_ApiFieldSpec_tags_tags" ON "ApiFieldSpec_tags" (tags);

CREATE TABLE "ModelIdentifierSpec_provider_name" (
	"ModelIdentifierSpec_id" TEXT,
	provider_name TEXT,
	PRIMARY KEY ("ModelIdentifierSpec_id", provider_name),
	FOREIGN KEY("ModelIdentifierSpec_id") REFERENCES "ModelIdentifierSpec" (id)
);
CREATE INDEX "ix_ModelIdentifierSpec_provider_name_provider_name" ON "ModelIdentifierSpec_provider_name" (provider_name);
CREATE INDEX "ix_ModelIdentifierSpec_provider_name_ModelIdentifierSpec_id" ON "ModelIdentifierSpec_provider_name" ("ModelIdentifierSpec_id");

CREATE TABLE "ModelIdentifierSpec_coverage_scope" (
	"ModelIdentifierSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("ModelIdentifierSpec_id", coverage_scope),
	FOREIGN KEY("ModelIdentifierSpec_id") REFERENCES "ModelIdentifierSpec" (id)
);
CREATE INDEX "ix_ModelIdentifierSpec_coverage_scope_ModelIdentifierSpec_id" ON "ModelIdentifierSpec_coverage_scope" ("ModelIdentifierSpec_id");
CREATE INDEX "ix_ModelIdentifierSpec_coverage_scope_coverage_scope" ON "ModelIdentifierSpec_coverage_scope" (coverage_scope);

CREATE TABLE "ModelIdentifierSpec_tags" (
	"ModelIdentifierSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("ModelIdentifierSpec_id", tags),
	FOREIGN KEY("ModelIdentifierSpec_id") REFERENCES "ModelIdentifierSpec" (id)
);
CREATE INDEX "ix_ModelIdentifierSpec_tags_tags" ON "ModelIdentifierSpec_tags" (tags);
CREATE INDEX "ix_ModelIdentifierSpec_tags_ModelIdentifierSpec_id" ON "ModelIdentifierSpec_tags" ("ModelIdentifierSpec_id");

CREATE TABLE "MethodSpec_coverage_scope" (
	"MethodSpec_id" TEXT,
	coverage_scope VARCHAR(7),
	PRIMARY KEY ("MethodSpec_id", coverage_scope),
	FOREIGN KEY("MethodSpec_id") REFERENCES "MethodSpec" (id)
);
CREATE INDEX "ix_MethodSpec_coverage_scope_coverage_scope" ON "MethodSpec_coverage_scope" (coverage_scope);
CREATE INDEX "ix_MethodSpec_coverage_scope_MethodSpec_id" ON "MethodSpec_coverage_scope" ("MethodSpec_id");

CREATE TABLE "MethodSpec_tags" (
	"MethodSpec_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("MethodSpec_id", tags),
	FOREIGN KEY("MethodSpec_id") REFERENCES "MethodSpec" (id)
);
CREATE INDEX "ix_MethodSpec_tags_tags" ON "MethodSpec_tags" (tags);
CREATE INDEX "ix_MethodSpec_tags_MethodSpec_id" ON "MethodSpec_tags" ("MethodSpec_id");
