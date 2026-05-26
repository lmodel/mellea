import pandera.polars as pla
from pandera.api.polars.types import PolarsData
from . import panderagen_polars_schema as pa_pl
import polars as pl
from typing import Optional


from pandera.typing import (
    Index,
    DataFrame,
    Series
)
from pandera.engines.polars_engine import (
    DateTime,
    Date,
    Time,
    Enum,
    Struct,
    List,
    Object
)


from linkml.generators.panderagen.linkml_pandera_validator import LinkmlPanderaValidator as _LinkmlPanderaValidator


# These are all str for now
ID_TYPES = {
    "NamedElement": "str",
    "ModelElement": "str",
    "RepositoryCatalog": "str",
    "PythonPackage": "str",
    "ModelIdentifierSpec": "str",
    "BackendSpec": "str",
    "MethodSpec": "str",
    "SessionSpec": "str",
    "HookPayloadSpec": "str",
    "PluginSpec": "str",
    "ApiFieldSpec": "str",
    "ApiModelSpec": "str",
    "CliCommandSpec": "str",
    "FormatterSpec": "str",
    "ContextSpec": "str",
    "ComponentSpec": "str",
    "RequirementSpec": "str",
    "SamplingStrategySpec": "str",
    "TelemetryMetricSpec": "str",
    "IntrinsicAdapterSpec": "str",
}

 # metamodel_version: 1.11.0
# version: 2026-05-26
class NamedElement(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Abstract base for any named, identifiable schema element.
    """

    _id_name : str =  'id' 
    id: str = pla.Field()
    """
    Stable identifier for a schema element.
    """
    
    name: str = pla.Field()
    """
    Human-readable name.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Narrative description of the element.
    """
    
    module_path: Optional[str] = pla.Field(nullable=True, )
    """
    Python module path where this element is defined.
    """
    
    source_file: Optional[str] = pla.Field(nullable=True, )
    """
    Source file relative to repository root.
    """
    
    package_kind: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('CORE','STDLIB','BACKENDS','FORMATTERS','HELPERS','PLUGINS','TELEMETRY','CLI','DOCS_EXAMPLES','TEST',)})
    """
    Package bucket.
    """
    
    element_kind: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('CLASS','ENUM','DATACLASS','TYPED_DICT','PYDANTIC_MODEL','PROTOCOL','FUNCTION','MIXIN',)})
    """
    Kind of Python declaration.
    """
    
    coverage_scope: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('SOURCE','API','CLI','EXAMPLE','TEST',)})
    """
    Where this element surfaces (source/API/CLI/example/test).
    """
    
    tags: Optional[str] = pla.Field(nullable=True, )
    """
    Free-form classification tags.
    """
    
    
class ModelElement(NamedElement):
    """
    Abstract base for concrete architectural elements.
    """

    _id_name : str =  'id' 
    pass
    
    
class RepositoryCatalog(NamedElement):
    """
    Top-level catalog rooting the analysed repository snapshot.
    """

    _id_name : str =  'id' 
    repository_root: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the repository root.
    """
    
    analyzed_on: Optional[Date] = pla.Field(nullable=True, )
    """
    Slot describing the analyzed on.
    """
    
    includes_path: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the includes path.
    """
    
    excludes_path: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the excludes path.
    """
    
    declares_element: Optional[List] = pla.Field(nullable=True, )
    """
    Slot describing the declares element.
    """
    
    
    @pla.check("declares_element")
    def check_nested_struct_declares_element(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ModelElement, pa_pl.ModelElementDict)
        
class PythonPackage(NamedElement):
    """
    A logical Python package (directory) inside the repository.
    """

    _id_name : str =  'id' 
    package_name: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the package name.
    """
    
    depends_on_package: Optional[List] = pla.Field(nullable=True, )
    """
    Slot describing the depends on package.
    """
    
    declares_element: Optional[List] = pla.Field(nullable=True, )
    """
    Slot describing the declares element.
    """
    
    
    @pla.check("depends_on_package")
    def check_nested_struct_depends_on_package(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PythonPackage, pa_pl.PythonPackageDict)
        
    @pla.check("declares_element")
    def check_nested_struct_declares_element(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ModelElement, pa_pl.ModelElementDict)
        
class ModelIdentifierSpec(NamedElement):
    """
    Cross-provider identifier table for a single model.
    """

    _id_name : str =  'id' 
    hf_model_name: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the hf model name.
    """
    
    ollama_name: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the ollama name.
    """
    
    watsonx_name: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the watsonx name.
    """
    
    openai_name: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the openai name.
    """
    
    bedrock_name: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the bedrock name.
    """
    
    provider_name: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the provider name.
    """
    
    
class BackendSpec(ModelElement):
    """
    Specification of a Mellea backend implementation.
    """

    _id_name : str =  'id' 
    backend_family: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('BEDROCK','DUMMY','HUGGINGFACE','LITELLM','OLLAMA','OPENAI','WATSONX',)})
    """
    Slot describing the backend family.
    """
    
    model_identifier: Optional[List] = pla.Field(nullable=True, )
    """
    Slot describing the model identifier.
    """
    
    default_formatter: Optional[ID_TYPES['FormatterSpec']] = pla.Field(nullable=True, )
    """
    Slot describing the default formatter.
    """
    
    model_options_key: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the model options key.
    """
    
    supports_streaming: Optional[bool] = pla.Field(nullable=True, )
    """
    Slot describing the supports streaming.
    """
    
    supports_tool_calls: Optional[bool] = pla.Field(nullable=True, )
    """
    Slot describing the supports tool calls.
    """
    
    supports_multimodal: Optional[bool] = pla.Field(nullable=True, )
    """
    Slot describing the supports multimodal.
    """
    
    
    @pla.check("model_identifier")
    def check_nested_struct_model_identifier(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ModelIdentifierSpec, pa_pl.ModelIdentifierSpecDict)
        
class MethodSpec(NamedElement):
    """
    Specification of a method exposed by a runtime class.
    """

    _id_name : str =  'id' 
    method_name: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the method name.
    """
    
    method_signature: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the method signature.
    """
    
    lifecycle_role: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the lifecycle role.
    """
    
    
class SessionSpec(ModelElement):
    """
    Specification of a Mellea session.
    """

    _id_name : str =  'id' 
    uses_backend: Optional[ID_TYPES['BackendSpec']] = pla.Field(nullable=True, )
    """
    Slot describing the uses backend.
    """
    
    uses_context: Optional[ID_TYPES['ContextSpec']] = pla.Field(nullable=True, )
    """
    Slot describing the uses context.
    """
    
    exposed_method: Optional[List] = pla.Field(nullable=True, )
    """
    Slot describing the exposed method.
    """
    
    
    @pla.check("exposed_method")
    def check_nested_struct_exposed_method(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, MethodSpec, pa_pl.MethodSpecDict)
        
class HookPayloadSpec(ModelElement):
    """
    Specification of a hook payload model.
    """

    _id_name : str =  'id' 
    hook_type: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('SESSION_PRE_INIT','SESSION_POST_INIT','SESSION_RESET','SESSION_CLEANUP','COMPONENT_PRE_EXECUTE','COMPONENT_POST_SUCCESS','COMPONENT_POST_ERROR','GENERATION_PRE_CALL','GENERATION_POST_CALL','GENERATION_ERROR','VALIDATION_PRE_CHECK','VALIDATION_POST_CHECK','SAMPLING_LOOP_START','SAMPLING_ITERATION','SAMPLING_REPAIR','SAMPLING_LOOP_END','TOOL_PRE_INVOKE','TOOL_POST_INVOKE',)})
    """
    Slot describing the hook type.
    """
    
    lifecycle_role: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the lifecycle role.
    """
    
    
class PluginSpec(ModelElement):
    """
    Specification of a Mellea plugin and the hooks it registers.
    """

    _id_name : str =  'id' 
    plugin_mode: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('SEQUENTIAL','TRANSFORM','CONCURRENT','AUDIT','FIRE_AND_FORGET',)})
    """
    Slot describing the plugin mode.
    """
    
    hook_type: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('SESSION_PRE_INIT','SESSION_POST_INIT','SESSION_RESET','SESSION_CLEANUP','COMPONENT_PRE_EXECUTE','COMPONENT_POST_SUCCESS','COMPONENT_POST_ERROR','GENERATION_PRE_CALL','GENERATION_POST_CALL','GENERATION_ERROR','VALIDATION_PRE_CHECK','VALIDATION_POST_CHECK','SAMPLING_LOOP_START','SAMPLING_ITERATION','SAMPLING_REPAIR','SAMPLING_LOOP_END','TOOL_PRE_INVOKE','TOOL_POST_INVOKE',)})
    """
    Slot describing the hook type.
    """
    
    payload_model: Optional[List] = pla.Field(nullable=True, )
    """
    Slot describing the payload model.
    """
    
    plugin_priority: Optional[int] = pla.Field(nullable=True, )
    """
    Slot describing the plugin priority.
    """
    
    
    @pla.check("payload_model")
    def check_nested_struct_payload_model(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, HookPayloadSpec, pa_pl.HookPayloadSpecDict)
        
class ApiFieldSpec(NamedElement):
    """
    Specification of a single field in an API model.
    """

    _id_name : str =  'id' 
    field_name: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the field name.
    """
    
    field_type: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the field type.
    """
    
    required_field: Optional[bool] = pla.Field(nullable=True, )
    """
    Slot describing the required field.
    """
    
    allows_null: Optional[bool] = pla.Field(nullable=True, )
    """
    Slot describing the allows null.
    """
    
    
class ApiModelSpec(ModelElement):
    """
    Specification of an HTTP API wire model.
    """

    _id_name : str =  'id' 
    request_or_response: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('REQUEST','RESPONSE','BOTH',)})
    """
    Slot describing the request or response.
    """
    
    openai_object_type: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the openai object type.
    """
    
    has_field: Optional[List] = pla.Field(nullable=True, )
    """
    Slot describing the has field.
    """
    
    
    @pla.check("has_field")
    def check_nested_struct_has_field(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ApiFieldSpec, pa_pl.ApiFieldSpecDict)
        
class CliCommandSpec(ModelElement):
    """
    Specification of a CLI command exposed under `m`.
    """

    _id_name : str =  'id' 
    command_group: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the command group.
    """
    
    command_path: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the command path.
    """
    
    command_purpose: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the command purpose.
    """
    
    input_model: Optional[List] = pla.Field(nullable=True, )
    """
    Slot describing the input model.
    """
    
    output_model: Optional[List] = pla.Field(nullable=True, )
    """
    Slot describing the output model.
    """
    
    
    @pla.check("input_model")
    def check_nested_struct_input_model(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ApiModelSpec, pa_pl.ApiModelSpecDict)
        
    @pla.check("output_model")
    def check_nested_struct_output_model(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ApiModelSpec, pa_pl.ApiModelSpecDict)
        
class FormatterSpec(ModelElement):
    """
    Specification of an output formatter for a backend.
    """

    _id_name : str =  'id' 
    pass
    
    
class ContextSpec(ModelElement):
    """
    Specification of a context implementation.
    """

    _id_name : str =  'id' 
    context_linearity: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('LINEAR','NON_LINEAR',)})
    """
    Slot describing the context linearity.
    """
    
    stores_component_history: Optional[bool] = pla.Field(nullable=True, )
    """
    Slot describing the stores component history.
    """
    
    accepts_message_attachments: Optional[bool] = pla.Field(nullable=True, )
    """
    Slot describing the accepts message attachments.
    """
    
    
class ComponentSpec(ModelElement):
    """
    Specification of a Mellea stdlib component type.
    """

    _id_name : str =  'id' 
    component_category: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('INSTRUCTION','MESSAGE','TOOL_MESSAGE','DOCUMENT','INTRINSIC','MOBJECT','QUERY','TRANSFORM','GENSTUB','REQUIREMENT','STREAM_EVENT',)})
    """
    Slot describing the component category.
    """
    
    input_modality: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the input modality.
    """
    
    parsed_output_type: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the parsed output type.
    """
    
    
class RequirementSpec(ModelElement):
    """
    Specification of a requirement validator.
    """

    _id_name : str =  'id' 
    validation_style: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the validation style.
    """
    
    may_trigger_repair: Optional[bool] = pla.Field(nullable=True, )
    """
    Slot describing the may trigger repair.
    """
    
    
class SamplingStrategySpec(ModelElement):
    """
    Specification of a sampling-loop strategy.
    """

    _id_name : str =  'id' 
    selection_policy: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the selection policy.
    """
    
    loop_budget_hint: Optional[int] = pla.Field(nullable=True, )
    """
    Slot describing the loop budget hint.
    """
    
    may_trigger_repair: Optional[bool] = pla.Field(nullable=True, )
    """
    Slot describing the may trigger repair.
    """
    
    
class TelemetryMetricSpec(ModelElement):
    """
    Specification of a telemetry metric emitted by Mellea.
    """

    _id_name : str =  'id' 
    metric_name: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the metric name.
    """
    
    
class IntrinsicAdapterSpec(NamedElement):
    """
    Specification of an intrinsic adapter (LoRA / aLoRA).
    """

    _id_name : str =  'id' 
    repo_id: Optional[str] = pla.Field(nullable=True, )
    """
    Slot describing the repo id.
    """
    
    adapter_type: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('LORA','ALORA',)})
    """
    Slot describing the adapter type.
    """
    
    

