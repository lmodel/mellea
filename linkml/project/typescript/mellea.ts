export type NamedElementId = string;
export type RepositoryCatalogId = string;
export type PythonPackageId = string;
export type ModelElementId = string;
export type BackendSpecId = string;
export type FormatterSpecId = string;
export type ContextSpecId = string;
export type SessionSpecId = string;
export type ComponentSpecId = string;
export type RequirementSpecId = string;
export type SamplingStrategySpecId = string;
export type PluginSpecId = string;
export type HookPayloadSpecId = string;
export type TelemetryMetricSpecId = string;
export type CliCommandSpecId = string;
export type ApiModelSpecId = string;
export type ApiFieldSpecId = string;
export type MethodSpecId = string;
export type ModelIdentifierSpecId = string;
export type IntrinsicAdapterSpecId = string;
/**
* Logical package buckets used to classify Mellea source modules.
*/
export enum PackageKindEnum {
    
    /** core */
    CORE = "CORE",
    /** stdlib */
    STDLIB = "STDLIB",
    /** backends */
    BACKENDS = "BACKENDS",
    /** formatters */
    FORMATTERS = "FORMATTERS",
    /** helpers */
    HELPERS = "HELPERS",
    /** plugins */
    PLUGINS = "PLUGINS",
    /** telemetry */
    TELEMETRY = "TELEMETRY",
    /** cli */
    CLI = "CLI",
    /** docs examples */
    DOCS_EXAMPLES = "DOCS_EXAMPLES",
    /** test */
    TEST = "TEST",
};
/**
* Kind of Python declaration captured by a ModelElement entry.
*/
export enum ElementKindEnum {
    
    /** class */
    CLASS = "CLASS",
    /** enum */
    ENUM = "ENUM",
    /** dataclass */
    DATACLASS = "DATACLASS",
    /** typed dict */
    TYPED_DICT = "TYPED_DICT",
    /** pydantic model */
    PYDANTIC_MODEL = "PYDANTIC_MODEL",
    /** protocol */
    PROTOCOL = "PROTOCOL",
    /** function */
    FUNCTION = "FUNCTION",
    /** mixin */
    MIXIN = "MIXIN",
};
/**
* Where in the project an element surfaces (source, API, CLI, ...).
*/
export enum CoverageScopeEnum {
    
    /** source */
    SOURCE = "SOURCE",
    /** api */
    API = "API",
    /** cli */
    CLI = "CLI",
    /** example */
    EXAMPLE = "EXAMPLE",
    /** test */
    TEST = "TEST",
};
/**
* Whether a Mellea context preserves linear ordering or not.
*/
export enum ContextLinearityEnum {
    
    /** Sequential, ordered history. */
    LINEAR = "LINEAR",
    /** Tree- or graph-shaped history. */
    NON_LINEAR = "NON_LINEAR",
};
/**
* High-level category of a Mellea stdlib component.
*/
export enum ComponentCategoryEnum {
    
    /** instruction */
    INSTRUCTION = "INSTRUCTION",
    /** message */
    MESSAGE = "MESSAGE",
    /** tool message */
    TOOL_MESSAGE = "TOOL_MESSAGE",
    /** document */
    DOCUMENT = "DOCUMENT",
    /** intrinsic */
    INTRINSIC = "INTRINSIC",
    /** mobject */
    MOBJECT = "MOBJECT",
    /** query */
    QUERY = "QUERY",
    /** transform */
    TRANSFORM = "TRANSFORM",
    /** genstub */
    GENSTUB = "GENSTUB",
    /** requirement */
    REQUIREMENT = "REQUIREMENT",
    /** stream event */
    STREAM_EVENT = "STREAM_EVENT",
};
/**
* Direction of a wire model (HTTP request, response, or both).
*/
export enum RequestResponseEnum {
    
    /** Inbound request payload. */
    REQUEST = "REQUEST",
    /** Outbound response payload. */
    RESPONSE = "RESPONSE",
    /** Model used in both directions (rare). */
    BOTH = "BOTH",
};
/**
* Backend families discovered under mellea/backends/.
*/
export enum BackendFamilyEnum {
    
    /** Backend family backed by mellea/backends/bedrock.py. */
    BEDROCK = "BEDROCK",
    /** Backend family backed by mellea/backends/dummy.py. */
    DUMMY = "DUMMY",
    /** Backend family backed by mellea/backends/huggingface.py. */
    HUGGINGFACE = "HUGGINGFACE",
    /** Backend family backed by mellea/backends/litellm.py. */
    LITELLM = "LITELLM",
    /** Backend family backed by mellea/backends/ollama.py. */
    OLLAMA = "OLLAMA",
    /** Backend family backed by mellea/backends/openai.py. */
    OPENAI = "OPENAI",
    /** Backend family backed by mellea/backends/watsonx.py. */
    WATSONX = "WATSONX",
};
/**
* Execution mode of a Mellea plugin (derived from PluginMode).
*/
export enum PluginModeEnum {
    
    /** sequential */
    SEQUENTIAL = "SEQUENTIAL",
    /** transform */
    TRANSFORM = "TRANSFORM",
    /** concurrent */
    CONCURRENT = "CONCURRENT",
    /** audit */
    AUDIT = "AUDIT",
    /** fire and forget */
    FIRE_AND_FORGET = "FIRE_AND_FORGET",
};
/**
* Lifecycle hook stages (derived from HookType).
*/
export enum HookTypeEnum {
    
    /** session pre init */
    SESSION_PRE_INIT = "SESSION_PRE_INIT",
    /** session post init */
    SESSION_POST_INIT = "SESSION_POST_INIT",
    /** session reset */
    SESSION_RESET = "SESSION_RESET",
    /** session cleanup */
    SESSION_CLEANUP = "SESSION_CLEANUP",
    /** component pre execute */
    COMPONENT_PRE_EXECUTE = "COMPONENT_PRE_EXECUTE",
    /** component post success */
    COMPONENT_POST_SUCCESS = "COMPONENT_POST_SUCCESS",
    /** component post error */
    COMPONENT_POST_ERROR = "COMPONENT_POST_ERROR",
    /** generation pre call */
    GENERATION_PRE_CALL = "GENERATION_PRE_CALL",
    /** generation post call */
    GENERATION_POST_CALL = "GENERATION_POST_CALL",
    /** generation error */
    GENERATION_ERROR = "GENERATION_ERROR",
    /** validation pre check */
    VALIDATION_PRE_CHECK = "VALIDATION_PRE_CHECK",
    /** validation post check */
    VALIDATION_POST_CHECK = "VALIDATION_POST_CHECK",
    /** sampling loop start */
    SAMPLING_LOOP_START = "SAMPLING_LOOP_START",
    /** sampling iteration */
    SAMPLING_ITERATION = "SAMPLING_ITERATION",
    /** sampling repair */
    SAMPLING_REPAIR = "SAMPLING_REPAIR",
    /** sampling loop end */
    SAMPLING_LOOP_END = "SAMPLING_LOOP_END",
    /** tool pre invoke */
    TOOL_PRE_INVOKE = "TOOL_PRE_INVOKE",
    /** tool post invoke */
    TOOL_POST_INVOKE = "TOOL_POST_INVOKE",
};
/**
* Adapter implementation type (derived from AdapterType).
*/
export enum AdapterTypeEnum {
    
    /** lora */
    LORA = "LORA",
    /** alora */
    ALORA = "ALORA",
};


/**
 * Abstract base for any named, identifiable schema element.
 */
export interface NamedElement {
    /** Stable identifier for a schema element. */
    id: string,
    /** Human-readable name. */
    name: string,
    /** Narrative description of the element. */
    description?: string,
    /** Python module path where this element is defined. */
    module_path?: string,
    /** Source file relative to repository root. */
    source_file?: string,
    /** Package bucket. */
    package_kind?: string,
    /** Kind of Python declaration. */
    element_kind?: string,
    /** Where this element surfaces (source/API/CLI/example/test). */
    coverage_scope?: string,
    /** Free-form classification tags. */
    tags?: string[],
}


/**
 * Top-level catalog rooting the analysed repository snapshot.
 */
export interface RepositoryCatalog extends NamedElement {
    /** Slot describing the repository root. */
    repository_root?: string,
    /** Slot describing the analyzed on. */
    analyzed_on?: date,
    /** Slot describing the includes path. */
    includes_path?: string[],
    /** Slot describing the excludes path. */
    excludes_path?: string[],
    /** Slot describing the declares element. */
    declares_element?: ModelElement[],
}


/**
 * A logical Python package (directory) inside the repository.
 */
export interface PythonPackage extends NamedElement {
    /** Slot describing the package name. */
    package_name?: string,
    /** Slot describing the depends on package. */
    depends_on_package?: PythonPackage[],
    /** Slot describing the declares element. */
    declares_element?: ModelElement[],
}


/**
 * Abstract base for concrete architectural elements.
 */
export interface ModelElement extends NamedElement {
}


/**
 * Specification of a Mellea backend implementation.
 */
export interface BackendSpec extends ModelElement {
    /** Slot describing the backend family. */
    backend_family?: string,
    /** Slot describing the model identifier. */
    model_identifier?: ModelIdentifierSpec[],
    /** Slot describing the default formatter. */
    default_formatter?: FormatterSpecId,
    /** Slot describing the model options key. */
    model_options_key?: string[],
    /** Slot describing the supports streaming. */
    supports_streaming?: boolean,
    /** Slot describing the supports tool calls. */
    supports_tool_calls?: boolean,
    /** Slot describing the supports multimodal. */
    supports_multimodal?: boolean,
}


/**
 * Specification of an output formatter for a backend.
 */
export interface FormatterSpec extends ModelElement {
}


/**
 * Specification of a context implementation.
 */
export interface ContextSpec extends ModelElement {
    /** Slot describing the context linearity. */
    context_linearity?: string,
    /** Slot describing the stores component history. */
    stores_component_history?: boolean,
    /** Slot describing the accepts message attachments. */
    accepts_message_attachments?: boolean,
}


/**
 * Specification of a Mellea session.
 */
export interface SessionSpec extends ModelElement {
    /** Slot describing the uses backend. */
    uses_backend?: BackendSpecId,
    /** Slot describing the uses context. */
    uses_context?: ContextSpecId,
    /** Slot describing the exposed method. */
    exposed_method?: MethodSpec[],
}


/**
 * Specification of a Mellea stdlib component type.
 */
export interface ComponentSpec extends ModelElement {
    /** Slot describing the component category. */
    component_category?: string,
    /** Slot describing the input modality. */
    input_modality?: string[],
    /** Slot describing the parsed output type. */
    parsed_output_type?: string,
}


/**
 * Specification of a requirement validator.
 */
export interface RequirementSpec extends ModelElement {
    /** Slot describing the validation style. */
    validation_style?: string,
    /** Slot describing the may trigger repair. */
    may_trigger_repair?: boolean,
}


/**
 * Specification of a sampling-loop strategy.
 */
export interface SamplingStrategySpec extends ModelElement {
    /** Slot describing the selection policy. */
    selection_policy?: string,
    /** Slot describing the loop budget hint. */
    loop_budget_hint?: number,
    /** Slot describing the may trigger repair. */
    may_trigger_repair?: boolean,
}


/**
 * Specification of a Mellea plugin and the hooks it registers.
 */
export interface PluginSpec extends ModelElement {
    /** Slot describing the plugin mode. */
    plugin_mode?: string,
    /** Slot describing the hook type. */
    hook_type?: string,
    /** Slot describing the payload model. */
    payload_model?: HookPayloadSpec[],
    /** Slot describing the plugin priority. */
    plugin_priority?: number,
}


/**
 * Specification of a hook payload model.
 */
export interface HookPayloadSpec extends ModelElement {
    /** Slot describing the hook type. */
    hook_type?: string,
    /** Slot describing the lifecycle role. */
    lifecycle_role?: string,
}


/**
 * Specification of a telemetry metric emitted by Mellea.
 */
export interface TelemetryMetricSpec extends ModelElement {
    /** Slot describing the metric name. */
    metric_name?: string[],
}


/**
 * Specification of a CLI command exposed under `m`.
 */
export interface CliCommandSpec extends ModelElement {
    /** Slot describing the command group. */
    command_group?: string,
    /** Slot describing the command path. */
    command_path?: string,
    /** Slot describing the command purpose. */
    command_purpose?: string,
    /** Slot describing the input model. */
    input_model?: ApiModelSpec[],
    /** Slot describing the output model. */
    output_model?: ApiModelSpec[],
}


/**
 * Specification of an HTTP API wire model.
 */
export interface ApiModelSpec extends ModelElement {
    /** Slot describing the request or response. */
    request_or_response?: string,
    /** Slot describing the openai object type. */
    openai_object_type?: string,
    /** Slot describing the has field. */
    has_field?: ApiFieldSpec[],
}


/**
 * Specification of a single field in an API model.
 */
export interface ApiFieldSpec extends NamedElement {
    /** Slot describing the field name. */
    field_name?: string,
    /** Slot describing the field type. */
    field_type?: string,
    /** Slot describing the required field. */
    required_field?: boolean,
    /** Slot describing the allows null. */
    allows_null?: boolean,
}


/**
 * Specification of a method exposed by a runtime class.
 */
export interface MethodSpec extends NamedElement {
    /** Slot describing the method name. */
    method_name?: string,
    /** Slot describing the method signature. */
    method_signature?: string,
    /** Slot describing the lifecycle role. */
    lifecycle_role?: string,
}


/**
 * Cross-provider identifier table for a single model.
 */
export interface ModelIdentifierSpec extends NamedElement {
    /** Slot describing the hf model name. */
    hf_model_name?: string,
    /** Slot describing the ollama name. */
    ollama_name?: string,
    /** Slot describing the watsonx name. */
    watsonx_name?: string,
    /** Slot describing the openai name. */
    openai_name?: string,
    /** Slot describing the bedrock name. */
    bedrock_name?: string,
    /** Slot describing the provider name. */
    provider_name?: string[],
}


/**
 * Specification of an intrinsic adapter (LoRA / aLoRA).
 */
export interface IntrinsicAdapterSpec extends NamedElement {
    /** Slot describing the repo id. */
    repo_id?: string,
    /** Slot describing the adapter type. */
    adapter_type?: string,
}



