#![allow(non_camel_case_types)]

#[cfg(feature = "serde")]
mod serde_utils;
pub mod poly;
pub mod poly_containers;
#[cfg(feature = "stubgen")]
pub mod stub_utils;

#[cfg(feature = "serde")]
use serde_yml as _ ;
use chrono::NaiveDate;
#[cfg(feature = "pyo3")]
use pyo3::{FromPyObject,prelude::*};
#[cfg(feature = "stubgen")]
use pyo3_stub_gen::{define_stub_info_gatherer,derive::gen_stub_pyclass,derive::gen_stub_pymethods};
#[cfg(feature = "serde")]
use serde::{Deserialize,Serialize,de::IntoDeserializer};
use serde_value::Value;
#[cfg(feature = "serde")]
use serde_path_to_error;
use std::collections::HashMap;
use std::collections::BTreeMap;

// Types

pub type string = String;
pub type integer = String;
pub type boolean = String;
pub type float = f64;
pub type double = f64;
pub type decimal = String;
pub type time = String;
pub type date = String;
pub type datetime = String;
pub type date_or_datetime = String;
pub type uriorcurie = String;
pub type curie = String;
pub type uri = String;
pub type ncname = String;
pub type objectidentifier = String;
pub type nodeidentifier = String;
pub type jsonpointer = String;
pub type jsonpath = String;
pub type sparqlpath = String;
pub type PythonDottedPath = String;
pub type RepositoryRelativePath = String;

// Slots

pub type id = uriorcurie;
pub type name = String;
pub type description = String;
pub type module_path = String;
pub type source_file = String;
pub type package_kind = PackageKindEnum;
pub type element_kind = ElementKindEnum;
pub type coverage_scope = Vec<CoverageScopeEnum>;
pub type tags = Vec<String>;
pub type repository_root = String;
pub type analyzed_on = NaiveDate;
pub type includes_path = Vec<String>;
pub type excludes_path = Vec<String>;
pub type package_name = String;
pub type depends_on_package = Vec<PythonPackage>;
pub type declares_element = Vec<ModelElement>;
pub type backend_family = BackendFamilyEnum;
pub type model_identifier = Vec<ModelIdentifierSpec>;
pub type default_formatter = FormatterSpec;
pub type model_options_key = Vec<String>;
pub type supports_streaming = bool;
pub type supports_tool_calls = bool;
pub type supports_multimodal = bool;
pub type context_linearity = ContextLinearityEnum;
pub type stores_component_history = bool;
pub type accepts_message_attachments = bool;
pub type uses_backend = BackendSpec;
pub type uses_context = ContextSpec;
pub type exposed_method = Vec<MethodSpec>;
pub type uses_component_type = Vec<ComponentSpec>;
pub type component_category = ComponentCategoryEnum;
pub type input_modality = Vec<String>;
pub type parsed_output_type = String;
pub type validation_style = String;
pub type may_trigger_repair = bool;
pub type selection_policy = String;
pub type loop_budget_hint = isize;
pub type plugin_mode = PluginModeEnum;
pub type hook_type = Vec<HookTypeEnum>;
pub type payload_model = Vec<HookPayloadSpec>;
pub type plugin_priority = isize;
pub type metric_name = Vec<String>;
pub type command_group = String;
pub type command_path = String;
pub type command_purpose = String;
pub type input_model = Vec<ApiModelSpec>;
pub type output_model = Vec<ApiModelSpec>;
pub type request_or_response = RequestResponseEnum;
pub type openai_object_type = String;
pub type has_field = Vec<ApiFieldSpec>;
pub type field_name = String;
pub type field_type = String;
pub type required_field = bool;
pub type allows_null = bool;
pub type method_name = String;
pub type method_signature = String;
pub type lifecycle_role = String;
pub type adapter_type = Vec<AdapterTypeEnum>;
pub type repo_id = String;
pub type provider_name = Vec<String>;
pub type hf_model_name = String;
pub type ollama_name = String;
pub type watsonx_name = String;
pub type openai_name = String;
pub type bedrock_name = String;

// Enums

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum PackageKindEnum {
    CORE,
    STDLIB,
    BACKENDS,
    FORMATTERS,
    HELPERS,
    PLUGINS,
    TELEMETRY,
    CLI,
    DOCSEXAMPLES,
    TEST,
}

impl core::fmt::Display for PackageKindEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            PackageKindEnum::CORE => f.write_str("CORE"),
            PackageKindEnum::STDLIB => f.write_str("STDLIB"),
            PackageKindEnum::BACKENDS => f.write_str("BACKENDS"),
            PackageKindEnum::FORMATTERS => f.write_str("FORMATTERS"),
            PackageKindEnum::HELPERS => f.write_str("HELPERS"),
            PackageKindEnum::PLUGINS => f.write_str("PLUGINS"),
            PackageKindEnum::TELEMETRY => f.write_str("TELEMETRY"),
            PackageKindEnum::CLI => f.write_str("CLI"),
            PackageKindEnum::DOCSEXAMPLES => f.write_str("DOCS_EXAMPLES"),
            PackageKindEnum::TEST => f.write_str("TEST"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for PackageKindEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            PackageKindEnum::CORE => "CORE",
            PackageKindEnum::STDLIB => "STDLIB",
            PackageKindEnum::BACKENDS => "BACKENDS",
            PackageKindEnum::FORMATTERS => "FORMATTERS",
            PackageKindEnum::HELPERS => "HELPERS",
            PackageKindEnum::PLUGINS => "PLUGINS",
            PackageKindEnum::TELEMETRY => "TELEMETRY",
            PackageKindEnum::CLI => "CLI",
            PackageKindEnum::DOCSEXAMPLES => "DOCS_EXAMPLES",
            PackageKindEnum::TEST => "TEST",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for PackageKindEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "CORE" => Ok(PackageKindEnum::CORE),
                "STDLIB" => Ok(PackageKindEnum::STDLIB),
                "BACKENDS" => Ok(PackageKindEnum::BACKENDS),
                "FORMATTERS" => Ok(PackageKindEnum::FORMATTERS),
                "HELPERS" => Ok(PackageKindEnum::HELPERS),
                "PLUGINS" => Ok(PackageKindEnum::PLUGINS),
                "TELEMETRY" => Ok(PackageKindEnum::TELEMETRY),
                "CLI" => Ok(PackageKindEnum::CLI),
                "DOCS_EXAMPLES" | "DOCSEXAMPLES" => Ok(PackageKindEnum::DOCSEXAMPLES),
                "TEST" => Ok(PackageKindEnum::TEST),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for PackageKindEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(PackageKindEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for PackageKindEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ElementKindEnum {
    CLASS,
    ENUM,
    DATACLASS,
    TYPEDDICT,
    PYDANTICMODEL,
    PROTOCOL,
    FUNCTION,
    MIXIN,
}

impl core::fmt::Display for ElementKindEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ElementKindEnum::CLASS => f.write_str("CLASS"),
            ElementKindEnum::ENUM => f.write_str("ENUM"),
            ElementKindEnum::DATACLASS => f.write_str("DATACLASS"),
            ElementKindEnum::TYPEDDICT => f.write_str("TYPED_DICT"),
            ElementKindEnum::PYDANTICMODEL => f.write_str("PYDANTIC_MODEL"),
            ElementKindEnum::PROTOCOL => f.write_str("PROTOCOL"),
            ElementKindEnum::FUNCTION => f.write_str("FUNCTION"),
            ElementKindEnum::MIXIN => f.write_str("MIXIN"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ElementKindEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ElementKindEnum::CLASS => "CLASS",
            ElementKindEnum::ENUM => "ENUM",
            ElementKindEnum::DATACLASS => "DATACLASS",
            ElementKindEnum::TYPEDDICT => "TYPED_DICT",
            ElementKindEnum::PYDANTICMODEL => "PYDANTIC_MODEL",
            ElementKindEnum::PROTOCOL => "PROTOCOL",
            ElementKindEnum::FUNCTION => "FUNCTION",
            ElementKindEnum::MIXIN => "MIXIN",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ElementKindEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "CLASS" => Ok(ElementKindEnum::CLASS),
                "ENUM" => Ok(ElementKindEnum::ENUM),
                "DATACLASS" => Ok(ElementKindEnum::DATACLASS),
                "TYPED_DICT" | "TYPEDDICT" => Ok(ElementKindEnum::TYPEDDICT),
                "PYDANTIC_MODEL" | "PYDANTICMODEL" => Ok(ElementKindEnum::PYDANTICMODEL),
                "PROTOCOL" => Ok(ElementKindEnum::PROTOCOL),
                "FUNCTION" => Ok(ElementKindEnum::FUNCTION),
                "MIXIN" => Ok(ElementKindEnum::MIXIN),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ElementKindEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ElementKindEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ElementKindEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum CoverageScopeEnum {
    SOURCE,
    API,
    CLI,
    EXAMPLE,
    TEST,
}

impl core::fmt::Display for CoverageScopeEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            CoverageScopeEnum::SOURCE => f.write_str("SOURCE"),
            CoverageScopeEnum::API => f.write_str("API"),
            CoverageScopeEnum::CLI => f.write_str("CLI"),
            CoverageScopeEnum::EXAMPLE => f.write_str("EXAMPLE"),
            CoverageScopeEnum::TEST => f.write_str("TEST"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for CoverageScopeEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            CoverageScopeEnum::SOURCE => "SOURCE",
            CoverageScopeEnum::API => "API",
            CoverageScopeEnum::CLI => "CLI",
            CoverageScopeEnum::EXAMPLE => "EXAMPLE",
            CoverageScopeEnum::TEST => "TEST",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for CoverageScopeEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "SOURCE" => Ok(CoverageScopeEnum::SOURCE),
                "API" => Ok(CoverageScopeEnum::API),
                "CLI" => Ok(CoverageScopeEnum::CLI),
                "EXAMPLE" => Ok(CoverageScopeEnum::EXAMPLE),
                "TEST" => Ok(CoverageScopeEnum::TEST),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for CoverageScopeEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(CoverageScopeEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for CoverageScopeEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ContextLinearityEnum {
    LINEAR,
    NONLINEAR,
}

impl core::fmt::Display for ContextLinearityEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ContextLinearityEnum::LINEAR => f.write_str("LINEAR"),
            ContextLinearityEnum::NONLINEAR => f.write_str("NON_LINEAR"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ContextLinearityEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ContextLinearityEnum::LINEAR => "LINEAR",
            ContextLinearityEnum::NONLINEAR => "NON_LINEAR",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ContextLinearityEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "LINEAR" => Ok(ContextLinearityEnum::LINEAR),
                "NON_LINEAR" | "NONLINEAR" => Ok(ContextLinearityEnum::NONLINEAR),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ContextLinearityEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ContextLinearityEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ContextLinearityEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['LINEAR', 'NON_LINEAR']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ComponentCategoryEnum {
    INSTRUCTION,
    MESSAGE,
    TOOLMESSAGE,
    DOCUMENT,
    INTRINSIC,
    MOBJECT,
    QUERY,
    TRANSFORM,
    GENSTUB,
    REQUIREMENT,
    STREAMEVENT,
}

impl core::fmt::Display for ComponentCategoryEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ComponentCategoryEnum::INSTRUCTION => f.write_str("INSTRUCTION"),
            ComponentCategoryEnum::MESSAGE => f.write_str("MESSAGE"),
            ComponentCategoryEnum::TOOLMESSAGE => f.write_str("TOOL_MESSAGE"),
            ComponentCategoryEnum::DOCUMENT => f.write_str("DOCUMENT"),
            ComponentCategoryEnum::INTRINSIC => f.write_str("INTRINSIC"),
            ComponentCategoryEnum::MOBJECT => f.write_str("MOBJECT"),
            ComponentCategoryEnum::QUERY => f.write_str("QUERY"),
            ComponentCategoryEnum::TRANSFORM => f.write_str("TRANSFORM"),
            ComponentCategoryEnum::GENSTUB => f.write_str("GENSTUB"),
            ComponentCategoryEnum::REQUIREMENT => f.write_str("REQUIREMENT"),
            ComponentCategoryEnum::STREAMEVENT => f.write_str("STREAM_EVENT"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ComponentCategoryEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ComponentCategoryEnum::INSTRUCTION => "INSTRUCTION",
            ComponentCategoryEnum::MESSAGE => "MESSAGE",
            ComponentCategoryEnum::TOOLMESSAGE => "TOOL_MESSAGE",
            ComponentCategoryEnum::DOCUMENT => "DOCUMENT",
            ComponentCategoryEnum::INTRINSIC => "INTRINSIC",
            ComponentCategoryEnum::MOBJECT => "MOBJECT",
            ComponentCategoryEnum::QUERY => "QUERY",
            ComponentCategoryEnum::TRANSFORM => "TRANSFORM",
            ComponentCategoryEnum::GENSTUB => "GENSTUB",
            ComponentCategoryEnum::REQUIREMENT => "REQUIREMENT",
            ComponentCategoryEnum::STREAMEVENT => "STREAM_EVENT",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ComponentCategoryEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "INSTRUCTION" => Ok(ComponentCategoryEnum::INSTRUCTION),
                "MESSAGE" => Ok(ComponentCategoryEnum::MESSAGE),
                "TOOL_MESSAGE" | "TOOLMESSAGE" => Ok(ComponentCategoryEnum::TOOLMESSAGE),
                "DOCUMENT" => Ok(ComponentCategoryEnum::DOCUMENT),
                "INTRINSIC" => Ok(ComponentCategoryEnum::INTRINSIC),
                "MOBJECT" => Ok(ComponentCategoryEnum::MOBJECT),
                "QUERY" => Ok(ComponentCategoryEnum::QUERY),
                "TRANSFORM" => Ok(ComponentCategoryEnum::TRANSFORM),
                "GENSTUB" => Ok(ComponentCategoryEnum::GENSTUB),
                "REQUIREMENT" => Ok(ComponentCategoryEnum::REQUIREMENT),
                "STREAM_EVENT" | "STREAMEVENT" => Ok(ComponentCategoryEnum::STREAMEVENT),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ComponentCategoryEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ComponentCategoryEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ComponentCategoryEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['INSTRUCTION', 'MESSAGE', 'TOOL_MESSAGE', 'DOCUMENT', 'INTRINSIC', 'MOBJECT', 'QUERY', 'TRANSFORM', 'GENSTUB', 'REQUIREMENT', 'STREAM_EVENT']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum RequestResponseEnum {
    REQUEST,
    RESPONSE,
    BOTH,
}

impl core::fmt::Display for RequestResponseEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            RequestResponseEnum::REQUEST => f.write_str("REQUEST"),
            RequestResponseEnum::RESPONSE => f.write_str("RESPONSE"),
            RequestResponseEnum::BOTH => f.write_str("BOTH"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for RequestResponseEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            RequestResponseEnum::REQUEST => "REQUEST",
            RequestResponseEnum::RESPONSE => "RESPONSE",
            RequestResponseEnum::BOTH => "BOTH",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for RequestResponseEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "REQUEST" => Ok(RequestResponseEnum::REQUEST),
                "RESPONSE" => Ok(RequestResponseEnum::RESPONSE),
                "BOTH" => Ok(RequestResponseEnum::BOTH),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for RequestResponseEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(RequestResponseEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for RequestResponseEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['REQUEST', 'RESPONSE', 'BOTH']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum BackendFamilyEnum {
    BEDROCK,
    DUMMY,
    HUGGINGFACE,
    LITELLM,
    OLLAMA,
    OPENAI,
    WATSONX,
}

impl core::fmt::Display for BackendFamilyEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            BackendFamilyEnum::BEDROCK => f.write_str("BEDROCK"),
            BackendFamilyEnum::DUMMY => f.write_str("DUMMY"),
            BackendFamilyEnum::HUGGINGFACE => f.write_str("HUGGINGFACE"),
            BackendFamilyEnum::LITELLM => f.write_str("LITELLM"),
            BackendFamilyEnum::OLLAMA => f.write_str("OLLAMA"),
            BackendFamilyEnum::OPENAI => f.write_str("OPENAI"),
            BackendFamilyEnum::WATSONX => f.write_str("WATSONX"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for BackendFamilyEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            BackendFamilyEnum::BEDROCK => "BEDROCK",
            BackendFamilyEnum::DUMMY => "DUMMY",
            BackendFamilyEnum::HUGGINGFACE => "HUGGINGFACE",
            BackendFamilyEnum::LITELLM => "LITELLM",
            BackendFamilyEnum::OLLAMA => "OLLAMA",
            BackendFamilyEnum::OPENAI => "OPENAI",
            BackendFamilyEnum::WATSONX => "WATSONX",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for BackendFamilyEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "BEDROCK" => Ok(BackendFamilyEnum::BEDROCK),
                "DUMMY" => Ok(BackendFamilyEnum::DUMMY),
                "HUGGINGFACE" => Ok(BackendFamilyEnum::HUGGINGFACE),
                "LITELLM" => Ok(BackendFamilyEnum::LITELLM),
                "OLLAMA" => Ok(BackendFamilyEnum::OLLAMA),
                "OPENAI" => Ok(BackendFamilyEnum::OPENAI),
                "WATSONX" => Ok(BackendFamilyEnum::WATSONX),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for BackendFamilyEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(BackendFamilyEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for BackendFamilyEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['BEDROCK', 'DUMMY', 'HUGGINGFACE', 'LITELLM', 'OLLAMA', 'OPENAI', 'WATSONX']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum PluginModeEnum {
    SEQUENTIAL,
    TRANSFORM,
    CONCURRENT,
    AUDIT,
    FIREANDFORGET,
}

impl core::fmt::Display for PluginModeEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            PluginModeEnum::SEQUENTIAL => f.write_str("SEQUENTIAL"),
            PluginModeEnum::TRANSFORM => f.write_str("TRANSFORM"),
            PluginModeEnum::CONCURRENT => f.write_str("CONCURRENT"),
            PluginModeEnum::AUDIT => f.write_str("AUDIT"),
            PluginModeEnum::FIREANDFORGET => f.write_str("FIRE_AND_FORGET"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for PluginModeEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            PluginModeEnum::SEQUENTIAL => "SEQUENTIAL",
            PluginModeEnum::TRANSFORM => "TRANSFORM",
            PluginModeEnum::CONCURRENT => "CONCURRENT",
            PluginModeEnum::AUDIT => "AUDIT",
            PluginModeEnum::FIREANDFORGET => "FIRE_AND_FORGET",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for PluginModeEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "SEQUENTIAL" => Ok(PluginModeEnum::SEQUENTIAL),
                "TRANSFORM" => Ok(PluginModeEnum::TRANSFORM),
                "CONCURRENT" => Ok(PluginModeEnum::CONCURRENT),
                "AUDIT" => Ok(PluginModeEnum::AUDIT),
                "FIRE_AND_FORGET" | "FIREANDFORGET" => Ok(PluginModeEnum::FIREANDFORGET),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for PluginModeEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(PluginModeEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for PluginModeEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['SEQUENTIAL', 'TRANSFORM', 'CONCURRENT', 'AUDIT', 'FIRE_AND_FORGET']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum HookTypeEnum {
    SESSIONPREINIT,
    SESSIONPOSTINIT,
    SESSIONRESET,
    SESSIONCLEANUP,
    COMPONENTPREEXECUTE,
    COMPONENTPOSTSUCCESS,
    COMPONENTPOSTERROR,
    GENERATIONPRECALL,
    GENERATIONPOSTCALL,
    GENERATIONERROR,
    VALIDATIONPRECHECK,
    VALIDATIONPOSTCHECK,
    SAMPLINGLOOPSTART,
    SAMPLINGITERATION,
    SAMPLINGREPAIR,
    SAMPLINGLOOPEND,
    TOOLPREINVOKE,
    TOOLPOSTINVOKE,
}

impl core::fmt::Display for HookTypeEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            HookTypeEnum::SESSIONPREINIT => f.write_str("SESSION_PRE_INIT"),
            HookTypeEnum::SESSIONPOSTINIT => f.write_str("SESSION_POST_INIT"),
            HookTypeEnum::SESSIONRESET => f.write_str("SESSION_RESET"),
            HookTypeEnum::SESSIONCLEANUP => f.write_str("SESSION_CLEANUP"),
            HookTypeEnum::COMPONENTPREEXECUTE => f.write_str("COMPONENT_PRE_EXECUTE"),
            HookTypeEnum::COMPONENTPOSTSUCCESS => f.write_str("COMPONENT_POST_SUCCESS"),
            HookTypeEnum::COMPONENTPOSTERROR => f.write_str("COMPONENT_POST_ERROR"),
            HookTypeEnum::GENERATIONPRECALL => f.write_str("GENERATION_PRE_CALL"),
            HookTypeEnum::GENERATIONPOSTCALL => f.write_str("GENERATION_POST_CALL"),
            HookTypeEnum::GENERATIONERROR => f.write_str("GENERATION_ERROR"),
            HookTypeEnum::VALIDATIONPRECHECK => f.write_str("VALIDATION_PRE_CHECK"),
            HookTypeEnum::VALIDATIONPOSTCHECK => f.write_str("VALIDATION_POST_CHECK"),
            HookTypeEnum::SAMPLINGLOOPSTART => f.write_str("SAMPLING_LOOP_START"),
            HookTypeEnum::SAMPLINGITERATION => f.write_str("SAMPLING_ITERATION"),
            HookTypeEnum::SAMPLINGREPAIR => f.write_str("SAMPLING_REPAIR"),
            HookTypeEnum::SAMPLINGLOOPEND => f.write_str("SAMPLING_LOOP_END"),
            HookTypeEnum::TOOLPREINVOKE => f.write_str("TOOL_PRE_INVOKE"),
            HookTypeEnum::TOOLPOSTINVOKE => f.write_str("TOOL_POST_INVOKE"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for HookTypeEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            HookTypeEnum::SESSIONPREINIT => "SESSION_PRE_INIT",
            HookTypeEnum::SESSIONPOSTINIT => "SESSION_POST_INIT",
            HookTypeEnum::SESSIONRESET => "SESSION_RESET",
            HookTypeEnum::SESSIONCLEANUP => "SESSION_CLEANUP",
            HookTypeEnum::COMPONENTPREEXECUTE => "COMPONENT_PRE_EXECUTE",
            HookTypeEnum::COMPONENTPOSTSUCCESS => "COMPONENT_POST_SUCCESS",
            HookTypeEnum::COMPONENTPOSTERROR => "COMPONENT_POST_ERROR",
            HookTypeEnum::GENERATIONPRECALL => "GENERATION_PRE_CALL",
            HookTypeEnum::GENERATIONPOSTCALL => "GENERATION_POST_CALL",
            HookTypeEnum::GENERATIONERROR => "GENERATION_ERROR",
            HookTypeEnum::VALIDATIONPRECHECK => "VALIDATION_PRE_CHECK",
            HookTypeEnum::VALIDATIONPOSTCHECK => "VALIDATION_POST_CHECK",
            HookTypeEnum::SAMPLINGLOOPSTART => "SAMPLING_LOOP_START",
            HookTypeEnum::SAMPLINGITERATION => "SAMPLING_ITERATION",
            HookTypeEnum::SAMPLINGREPAIR => "SAMPLING_REPAIR",
            HookTypeEnum::SAMPLINGLOOPEND => "SAMPLING_LOOP_END",
            HookTypeEnum::TOOLPREINVOKE => "TOOL_PRE_INVOKE",
            HookTypeEnum::TOOLPOSTINVOKE => "TOOL_POST_INVOKE",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for HookTypeEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "SESSION_PRE_INIT" | "SESSIONPREINIT" => Ok(HookTypeEnum::SESSIONPREINIT),
                "SESSION_POST_INIT" | "SESSIONPOSTINIT" => Ok(HookTypeEnum::SESSIONPOSTINIT),
                "SESSION_RESET" | "SESSIONRESET" => Ok(HookTypeEnum::SESSIONRESET),
                "SESSION_CLEANUP" | "SESSIONCLEANUP" => Ok(HookTypeEnum::SESSIONCLEANUP),
                "COMPONENT_PRE_EXECUTE" | "COMPONENTPREEXECUTE" => Ok(HookTypeEnum::COMPONENTPREEXECUTE),
                "COMPONENT_POST_SUCCESS" | "COMPONENTPOSTSUCCESS" => Ok(HookTypeEnum::COMPONENTPOSTSUCCESS),
                "COMPONENT_POST_ERROR" | "COMPONENTPOSTERROR" => Ok(HookTypeEnum::COMPONENTPOSTERROR),
                "GENERATION_PRE_CALL" | "GENERATIONPRECALL" => Ok(HookTypeEnum::GENERATIONPRECALL),
                "GENERATION_POST_CALL" | "GENERATIONPOSTCALL" => Ok(HookTypeEnum::GENERATIONPOSTCALL),
                "GENERATION_ERROR" | "GENERATIONERROR" => Ok(HookTypeEnum::GENERATIONERROR),
                "VALIDATION_PRE_CHECK" | "VALIDATIONPRECHECK" => Ok(HookTypeEnum::VALIDATIONPRECHECK),
                "VALIDATION_POST_CHECK" | "VALIDATIONPOSTCHECK" => Ok(HookTypeEnum::VALIDATIONPOSTCHECK),
                "SAMPLING_LOOP_START" | "SAMPLINGLOOPSTART" => Ok(HookTypeEnum::SAMPLINGLOOPSTART),
                "SAMPLING_ITERATION" | "SAMPLINGITERATION" => Ok(HookTypeEnum::SAMPLINGITERATION),
                "SAMPLING_REPAIR" | "SAMPLINGREPAIR" => Ok(HookTypeEnum::SAMPLINGREPAIR),
                "SAMPLING_LOOP_END" | "SAMPLINGLOOPEND" => Ok(HookTypeEnum::SAMPLINGLOOPEND),
                "TOOL_PRE_INVOKE" | "TOOLPREINVOKE" => Ok(HookTypeEnum::TOOLPREINVOKE),
                "TOOL_POST_INVOKE" | "TOOLPOSTINVOKE" => Ok(HookTypeEnum::TOOLPOSTINVOKE),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for HookTypeEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(HookTypeEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for HookTypeEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['SESSION_PRE_INIT', 'SESSION_POST_INIT', 'SESSION_RESET', 'SESSION_CLEANUP', 'COMPONENT_PRE_EXECUTE', 'COMPONENT_POST_SUCCESS', 'COMPONENT_POST_ERROR', 'GENERATION_PRE_CALL', 'GENERATION_POST_CALL', 'GENERATION_ERROR', 'VALIDATION_PRE_CHECK', 'VALIDATION_POST_CHECK', 'SAMPLING_LOOP_START', 'SAMPLING_ITERATION', 'SAMPLING_REPAIR', 'SAMPLING_LOOP_END', 'TOOL_PRE_INVOKE', 'TOOL_POST_INVOKE']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum AdapterTypeEnum {
    LORA,
    ALORA,
}

impl core::fmt::Display for AdapterTypeEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            AdapterTypeEnum::LORA => f.write_str("LORA"),
            AdapterTypeEnum::ALORA => f.write_str("ALORA"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for AdapterTypeEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            AdapterTypeEnum::LORA => "LORA",
            AdapterTypeEnum::ALORA => "ALORA",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for AdapterTypeEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "LORA" => Ok(AdapterTypeEnum::LORA),
                "ALORA" => Ok(AdapterTypeEnum::ALORA),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for AdapterTypeEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(AdapterTypeEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for AdapterTypeEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['LORA', 'ALORA']",
            "typing".into(),
        )
    }
}

// Classes

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct NamedElement {
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl NamedElement {
    #[new]
    #[pyo3(signature = (id, name, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        NamedElement{id, name, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<NamedElement>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<NamedElement> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<NamedElement>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid NamedElement",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for NamedElement {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a NamedElement from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature="serde", serde(untagged))]
pub enum NamedElementOrSubtype {    RepositoryCatalog(RepositoryCatalog),     PythonPackage(PythonPackage),     ModelElement(ModelElement),     ApiFieldSpec(ApiFieldSpec),     MethodSpec(MethodSpec),     ModelIdentifierSpec(ModelIdentifierSpec),     IntrinsicAdapterSpec(IntrinsicAdapterSpec),     BackendSpec(BackendSpec),     FormatterSpec(FormatterSpec),     ContextSpec(ContextSpec),     SessionSpec(SessionSpec),     ComponentSpec(ComponentSpec),     RequirementSpec(RequirementSpec),     SamplingStrategySpec(SamplingStrategySpec),     PluginSpec(PluginSpec),     HookPayloadSpec(HookPayloadSpec),     TelemetryMetricSpec(TelemetryMetricSpec),     CliCommandSpec(CliCommandSpec),     ApiModelSpec(ApiModelSpec)}

impl From<RepositoryCatalog>   for NamedElementOrSubtype { fn from(x: RepositoryCatalog)   -> Self { Self::RepositoryCatalog(x) } }
impl From<PythonPackage>   for NamedElementOrSubtype { fn from(x: PythonPackage)   -> Self { Self::PythonPackage(x) } }
impl From<ModelElement>   for NamedElementOrSubtype { fn from(x: ModelElement)   -> Self { Self::ModelElement(x) } }
impl From<ApiFieldSpec>   for NamedElementOrSubtype { fn from(x: ApiFieldSpec)   -> Self { Self::ApiFieldSpec(x) } }
impl From<MethodSpec>   for NamedElementOrSubtype { fn from(x: MethodSpec)   -> Self { Self::MethodSpec(x) } }
impl From<ModelIdentifierSpec>   for NamedElementOrSubtype { fn from(x: ModelIdentifierSpec)   -> Self { Self::ModelIdentifierSpec(x) } }
impl From<IntrinsicAdapterSpec>   for NamedElementOrSubtype { fn from(x: IntrinsicAdapterSpec)   -> Self { Self::IntrinsicAdapterSpec(x) } }
impl From<BackendSpec>   for NamedElementOrSubtype { fn from(x: BackendSpec)   -> Self { Self::BackendSpec(x) } }
impl From<FormatterSpec>   for NamedElementOrSubtype { fn from(x: FormatterSpec)   -> Self { Self::FormatterSpec(x) } }
impl From<ContextSpec>   for NamedElementOrSubtype { fn from(x: ContextSpec)   -> Self { Self::ContextSpec(x) } }
impl From<SessionSpec>   for NamedElementOrSubtype { fn from(x: SessionSpec)   -> Self { Self::SessionSpec(x) } }
impl From<ComponentSpec>   for NamedElementOrSubtype { fn from(x: ComponentSpec)   -> Self { Self::ComponentSpec(x) } }
impl From<RequirementSpec>   for NamedElementOrSubtype { fn from(x: RequirementSpec)   -> Self { Self::RequirementSpec(x) } }
impl From<SamplingStrategySpec>   for NamedElementOrSubtype { fn from(x: SamplingStrategySpec)   -> Self { Self::SamplingStrategySpec(x) } }
impl From<PluginSpec>   for NamedElementOrSubtype { fn from(x: PluginSpec)   -> Self { Self::PluginSpec(x) } }
impl From<HookPayloadSpec>   for NamedElementOrSubtype { fn from(x: HookPayloadSpec)   -> Self { Self::HookPayloadSpec(x) } }
impl From<TelemetryMetricSpec>   for NamedElementOrSubtype { fn from(x: TelemetryMetricSpec)   -> Self { Self::TelemetryMetricSpec(x) } }
impl From<CliCommandSpec>   for NamedElementOrSubtype { fn from(x: CliCommandSpec)   -> Self { Self::CliCommandSpec(x) } }
impl From<ApiModelSpec>   for NamedElementOrSubtype { fn from(x: ApiModelSpec)   -> Self { Self::ApiModelSpec(x) } }

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for NamedElementOrSubtype {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<RepositoryCatalog>() {
            return Ok(NamedElementOrSubtype::RepositoryCatalog(val));
        }        if let Ok(val) = ob.extract::<PythonPackage>() {
            return Ok(NamedElementOrSubtype::PythonPackage(val));
        }        if let Ok(val) = ob.extract::<ModelElement>() {
            return Ok(NamedElementOrSubtype::ModelElement(val));
        }        if let Ok(val) = ob.extract::<ApiFieldSpec>() {
            return Ok(NamedElementOrSubtype::ApiFieldSpec(val));
        }        if let Ok(val) = ob.extract::<MethodSpec>() {
            return Ok(NamedElementOrSubtype::MethodSpec(val));
        }        if let Ok(val) = ob.extract::<ModelIdentifierSpec>() {
            return Ok(NamedElementOrSubtype::ModelIdentifierSpec(val));
        }        if let Ok(val) = ob.extract::<IntrinsicAdapterSpec>() {
            return Ok(NamedElementOrSubtype::IntrinsicAdapterSpec(val));
        }        if let Ok(val) = ob.extract::<BackendSpec>() {
            return Ok(NamedElementOrSubtype::BackendSpec(val));
        }        if let Ok(val) = ob.extract::<FormatterSpec>() {
            return Ok(NamedElementOrSubtype::FormatterSpec(val));
        }        if let Ok(val) = ob.extract::<ContextSpec>() {
            return Ok(NamedElementOrSubtype::ContextSpec(val));
        }        if let Ok(val) = ob.extract::<SessionSpec>() {
            return Ok(NamedElementOrSubtype::SessionSpec(val));
        }        if let Ok(val) = ob.extract::<ComponentSpec>() {
            return Ok(NamedElementOrSubtype::ComponentSpec(val));
        }        if let Ok(val) = ob.extract::<RequirementSpec>() {
            return Ok(NamedElementOrSubtype::RequirementSpec(val));
        }        if let Ok(val) = ob.extract::<SamplingStrategySpec>() {
            return Ok(NamedElementOrSubtype::SamplingStrategySpec(val));
        }        if let Ok(val) = ob.extract::<PluginSpec>() {
            return Ok(NamedElementOrSubtype::PluginSpec(val));
        }        if let Ok(val) = ob.extract::<HookPayloadSpec>() {
            return Ok(NamedElementOrSubtype::HookPayloadSpec(val));
        }        if let Ok(val) = ob.extract::<TelemetryMetricSpec>() {
            return Ok(NamedElementOrSubtype::TelemetryMetricSpec(val));
        }        if let Ok(val) = ob.extract::<CliCommandSpec>() {
            return Ok(NamedElementOrSubtype::CliCommandSpec(val));
        }        if let Ok(val) = ob.extract::<ApiModelSpec>() {
            return Ok(NamedElementOrSubtype::ApiModelSpec(val));
        }Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid NamedElementOrSubtype",
        ))
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for NamedElementOrSubtype {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;

    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        match self {
            NamedElementOrSubtype::RepositoryCatalog(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::PythonPackage(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::ModelElement(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::ApiFieldSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::MethodSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::ModelIdentifierSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::IntrinsicAdapterSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::BackendSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::FormatterSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::ContextSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::SessionSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::ComponentSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::RequirementSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::SamplingStrategySpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::PluginSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::HookPayloadSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::TelemetryMetricSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::CliCommandSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            NamedElementOrSubtype::ApiModelSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
        }
    }
}


#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<NamedElementOrSubtype>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<NamedElementOrSubtype> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<NamedElementOrSubtype>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid NamedElementOrSubtype",
        ))
    }
}

#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for NamedElementOrSubtype {
    type Key       = uriorcurie;
    type Value     = serde_value::Value;
    type Error     = String;

    fn from_pair_mapping(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = RepositoryCatalog::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::RepositoryCatalog(x));
        }
        if let Ok(x) = PythonPackage::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::PythonPackage(x));
        }
        if let Ok(x) = ModelElement::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::ModelElement(x));
        }
        if let Ok(x) = ApiFieldSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::ApiFieldSpec(x));
        }
        if let Ok(x) = MethodSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::MethodSpec(x));
        }
        if let Ok(x) = ModelIdentifierSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::ModelIdentifierSpec(x));
        }
        if let Ok(x) = IntrinsicAdapterSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::IntrinsicAdapterSpec(x));
        }
        if let Ok(x) = BackendSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::BackendSpec(x));
        }
        if let Ok(x) = FormatterSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::FormatterSpec(x));
        }
        if let Ok(x) = ContextSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::ContextSpec(x));
        }
        if let Ok(x) = SessionSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::SessionSpec(x));
        }
        if let Ok(x) = ComponentSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::ComponentSpec(x));
        }
        if let Ok(x) = RequirementSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::RequirementSpec(x));
        }
        if let Ok(x) = SamplingStrategySpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::SamplingStrategySpec(x));
        }
        if let Ok(x) = PluginSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::PluginSpec(x));
        }
        if let Ok(x) = HookPayloadSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::HookPayloadSpec(x));
        }
        if let Ok(x) = TelemetryMetricSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::TelemetryMetricSpec(x));
        }
        if let Ok(x) = CliCommandSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::CliCommandSpec(x));
        }
        if let Ok(x) = ApiModelSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::ApiModelSpec(x));
        }
        Err("none of the variants matched the mapping form".into())
    }

    fn from_pair_simple(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = RepositoryCatalog::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::RepositoryCatalog(x));
        }
        if let Ok(x) = PythonPackage::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::PythonPackage(x));
        }
        if let Ok(x) = ModelElement::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::ModelElement(x));
        }
        if let Ok(x) = ApiFieldSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::ApiFieldSpec(x));
        }
        if let Ok(x) = MethodSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::MethodSpec(x));
        }
        if let Ok(x) = ModelIdentifierSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::ModelIdentifierSpec(x));
        }
        if let Ok(x) = IntrinsicAdapterSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::IntrinsicAdapterSpec(x));
        }
        if let Ok(x) = BackendSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::BackendSpec(x));
        }
        if let Ok(x) = FormatterSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::FormatterSpec(x));
        }
        if let Ok(x) = ContextSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::ContextSpec(x));
        }
        if let Ok(x) = SessionSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::SessionSpec(x));
        }
        if let Ok(x) = ComponentSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::ComponentSpec(x));
        }
        if let Ok(x) = RequirementSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::RequirementSpec(x));
        }
        if let Ok(x) = SamplingStrategySpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::SamplingStrategySpec(x));
        }
        if let Ok(x) = PluginSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::PluginSpec(x));
        }
        if let Ok(x) = HookPayloadSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::HookPayloadSpec(x));
        }
        if let Ok(x) = TelemetryMetricSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::TelemetryMetricSpec(x));
        }
        if let Ok(x) = CliCommandSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::CliCommandSpec(x));
        }
        if let Ok(x) = ApiModelSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NamedElementOrSubtype::ApiModelSpec(x));
        }
        Err("none of the variants support the primitive form".into())
    }

    fn extract_key(&self) -> &Self::Key {
        match self {
            NamedElementOrSubtype::RepositoryCatalog(inner) => inner.extract_key(),
            NamedElementOrSubtype::PythonPackage(inner) => inner.extract_key(),
            NamedElementOrSubtype::ModelElement(inner) => inner.extract_key(),
            NamedElementOrSubtype::ApiFieldSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::MethodSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::ModelIdentifierSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::IntrinsicAdapterSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::BackendSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::FormatterSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::ContextSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::SessionSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::ComponentSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::RequirementSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::SamplingStrategySpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::PluginSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::HookPayloadSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::TelemetryMetricSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::CliCommandSpec(inner) => inner.extract_key(),
            NamedElementOrSubtype::ApiModelSpec(inner) => inner.extract_key(),
        }
    }
}

#[cfg(feature = "stubgen")]
::pyo3_stub_gen::impl_stub_type!(NamedElementOrSubtype = RepositoryCatalog | PythonPackage | ModelElement | ApiFieldSpec | MethodSpec | ModelIdentifierSpec | IntrinsicAdapterSpec | BackendSpec | FormatterSpec | ContextSpec | SessionSpec | ComponentSpec | RequirementSpec | SamplingStrategySpec | PluginSpec | HookPayloadSpec | TelemetryMetricSpec | CliCommandSpec | ApiModelSpec);

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct RepositoryCatalog {
    #[cfg_attr(feature = "serde", serde(default))]
    pub repository_root: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub analyzed_on: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub includes_path: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub excludes_path: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub declares_element: Option<Vec<ModelElementOrSubtype>>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl RepositoryCatalog {
    #[new]
    #[pyo3(signature = (id, name, repository_root=None, analyzed_on=None, includes_path=None, excludes_path=None, declares_element=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, repository_root: Option<String>, analyzed_on: Option<NaiveDate>, includes_path: Option<Vec<String>>, excludes_path: Option<Vec<String>>, declares_element: Option<serde_utils::PyValue<Vec<ModelElementOrSubtype>>>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        let declares_element = declares_element.map(|v| v.into_inner());
        RepositoryCatalog{id, name, repository_root, analyzed_on, includes_path, excludes_path, declares_element, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<RepositoryCatalog>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<RepositoryCatalog> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<RepositoryCatalog>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid RepositoryCatalog",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for RepositoryCatalog {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a RepositoryCatalog from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PythonPackage {
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub depends_on_package: Option<Vec<Box<PythonPackage>>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub declares_element: Option<Vec<ModelElementOrSubtype>>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PythonPackage {
    #[new]
    #[pyo3(signature = (id, name, package_name=None, depends_on_package=None, declares_element=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, package_name: Option<String>, depends_on_package: Option<serde_utils::PyValue<Vec<Box<PythonPackage>>>>, declares_element: Option<serde_utils::PyValue<Vec<ModelElementOrSubtype>>>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        let depends_on_package = depends_on_package.map(|v| v.into_inner());
        let declares_element = declares_element.map(|v| v.into_inner());
        PythonPackage{id, name, package_name, depends_on_package, declares_element, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PythonPackage>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PythonPackage> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PythonPackage>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PythonPackage",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PythonPackage {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a PythonPackage from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ModelElement {
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ModelElement {
    #[new]
    #[pyo3(signature = (id, name, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        ModelElement{id, name, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ModelElement>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ModelElement> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ModelElement>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ModelElement",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for ModelElement {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a ModelElement from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature="serde", serde(untagged))]
pub enum ModelElementOrSubtype {    BackendSpec(BackendSpec),     FormatterSpec(FormatterSpec),     ContextSpec(ContextSpec),     SessionSpec(SessionSpec),     ComponentSpec(ComponentSpec),     RequirementSpec(RequirementSpec),     SamplingStrategySpec(SamplingStrategySpec),     PluginSpec(PluginSpec),     HookPayloadSpec(HookPayloadSpec),     TelemetryMetricSpec(TelemetryMetricSpec),     CliCommandSpec(CliCommandSpec),     ApiModelSpec(ApiModelSpec)}

impl From<BackendSpec>   for ModelElementOrSubtype { fn from(x: BackendSpec)   -> Self { Self::BackendSpec(x) } }
impl From<FormatterSpec>   for ModelElementOrSubtype { fn from(x: FormatterSpec)   -> Self { Self::FormatterSpec(x) } }
impl From<ContextSpec>   for ModelElementOrSubtype { fn from(x: ContextSpec)   -> Self { Self::ContextSpec(x) } }
impl From<SessionSpec>   for ModelElementOrSubtype { fn from(x: SessionSpec)   -> Self { Self::SessionSpec(x) } }
impl From<ComponentSpec>   for ModelElementOrSubtype { fn from(x: ComponentSpec)   -> Self { Self::ComponentSpec(x) } }
impl From<RequirementSpec>   for ModelElementOrSubtype { fn from(x: RequirementSpec)   -> Self { Self::RequirementSpec(x) } }
impl From<SamplingStrategySpec>   for ModelElementOrSubtype { fn from(x: SamplingStrategySpec)   -> Self { Self::SamplingStrategySpec(x) } }
impl From<PluginSpec>   for ModelElementOrSubtype { fn from(x: PluginSpec)   -> Self { Self::PluginSpec(x) } }
impl From<HookPayloadSpec>   for ModelElementOrSubtype { fn from(x: HookPayloadSpec)   -> Self { Self::HookPayloadSpec(x) } }
impl From<TelemetryMetricSpec>   for ModelElementOrSubtype { fn from(x: TelemetryMetricSpec)   -> Self { Self::TelemetryMetricSpec(x) } }
impl From<CliCommandSpec>   for ModelElementOrSubtype { fn from(x: CliCommandSpec)   -> Self { Self::CliCommandSpec(x) } }
impl From<ApiModelSpec>   for ModelElementOrSubtype { fn from(x: ApiModelSpec)   -> Self { Self::ApiModelSpec(x) } }

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ModelElementOrSubtype {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<BackendSpec>() {
            return Ok(ModelElementOrSubtype::BackendSpec(val));
        }        if let Ok(val) = ob.extract::<FormatterSpec>() {
            return Ok(ModelElementOrSubtype::FormatterSpec(val));
        }        if let Ok(val) = ob.extract::<ContextSpec>() {
            return Ok(ModelElementOrSubtype::ContextSpec(val));
        }        if let Ok(val) = ob.extract::<SessionSpec>() {
            return Ok(ModelElementOrSubtype::SessionSpec(val));
        }        if let Ok(val) = ob.extract::<ComponentSpec>() {
            return Ok(ModelElementOrSubtype::ComponentSpec(val));
        }        if let Ok(val) = ob.extract::<RequirementSpec>() {
            return Ok(ModelElementOrSubtype::RequirementSpec(val));
        }        if let Ok(val) = ob.extract::<SamplingStrategySpec>() {
            return Ok(ModelElementOrSubtype::SamplingStrategySpec(val));
        }        if let Ok(val) = ob.extract::<PluginSpec>() {
            return Ok(ModelElementOrSubtype::PluginSpec(val));
        }        if let Ok(val) = ob.extract::<HookPayloadSpec>() {
            return Ok(ModelElementOrSubtype::HookPayloadSpec(val));
        }        if let Ok(val) = ob.extract::<TelemetryMetricSpec>() {
            return Ok(ModelElementOrSubtype::TelemetryMetricSpec(val));
        }        if let Ok(val) = ob.extract::<CliCommandSpec>() {
            return Ok(ModelElementOrSubtype::CliCommandSpec(val));
        }        if let Ok(val) = ob.extract::<ApiModelSpec>() {
            return Ok(ModelElementOrSubtype::ApiModelSpec(val));
        }Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ModelElementOrSubtype",
        ))
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ModelElementOrSubtype {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;

    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        match self {
            ModelElementOrSubtype::BackendSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            ModelElementOrSubtype::FormatterSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            ModelElementOrSubtype::ContextSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            ModelElementOrSubtype::SessionSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            ModelElementOrSubtype::ComponentSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            ModelElementOrSubtype::RequirementSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            ModelElementOrSubtype::SamplingStrategySpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            ModelElementOrSubtype::PluginSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            ModelElementOrSubtype::HookPayloadSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            ModelElementOrSubtype::TelemetryMetricSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            ModelElementOrSubtype::CliCommandSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            ModelElementOrSubtype::ApiModelSpec(val) => val.into_pyobject(py).map(move |b| b.into_any()),
        }
    }
}


#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ModelElementOrSubtype>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ModelElementOrSubtype> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ModelElementOrSubtype>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ModelElementOrSubtype",
        ))
    }
}

#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for ModelElementOrSubtype {
    type Key       = uriorcurie;
    type Value     = serde_value::Value;
    type Error     = String;

    fn from_pair_mapping(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = BackendSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::BackendSpec(x));
        }
        if let Ok(x) = FormatterSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::FormatterSpec(x));
        }
        if let Ok(x) = ContextSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::ContextSpec(x));
        }
        if let Ok(x) = SessionSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::SessionSpec(x));
        }
        if let Ok(x) = ComponentSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::ComponentSpec(x));
        }
        if let Ok(x) = RequirementSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::RequirementSpec(x));
        }
        if let Ok(x) = SamplingStrategySpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::SamplingStrategySpec(x));
        }
        if let Ok(x) = PluginSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::PluginSpec(x));
        }
        if let Ok(x) = HookPayloadSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::HookPayloadSpec(x));
        }
        if let Ok(x) = TelemetryMetricSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::TelemetryMetricSpec(x));
        }
        if let Ok(x) = CliCommandSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::CliCommandSpec(x));
        }
        if let Ok(x) = ApiModelSpec::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::ApiModelSpec(x));
        }
        Err("none of the variants matched the mapping form".into())
    }

    fn from_pair_simple(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = BackendSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::BackendSpec(x));
        }
        if let Ok(x) = FormatterSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::FormatterSpec(x));
        }
        if let Ok(x) = ContextSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::ContextSpec(x));
        }
        if let Ok(x) = SessionSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::SessionSpec(x));
        }
        if let Ok(x) = ComponentSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::ComponentSpec(x));
        }
        if let Ok(x) = RequirementSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::RequirementSpec(x));
        }
        if let Ok(x) = SamplingStrategySpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::SamplingStrategySpec(x));
        }
        if let Ok(x) = PluginSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::PluginSpec(x));
        }
        if let Ok(x) = HookPayloadSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::HookPayloadSpec(x));
        }
        if let Ok(x) = TelemetryMetricSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::TelemetryMetricSpec(x));
        }
        if let Ok(x) = CliCommandSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::CliCommandSpec(x));
        }
        if let Ok(x) = ApiModelSpec::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ModelElementOrSubtype::ApiModelSpec(x));
        }
        Err("none of the variants support the primitive form".into())
    }

    fn extract_key(&self) -> &Self::Key {
        match self {
            ModelElementOrSubtype::BackendSpec(inner) => inner.extract_key(),
            ModelElementOrSubtype::FormatterSpec(inner) => inner.extract_key(),
            ModelElementOrSubtype::ContextSpec(inner) => inner.extract_key(),
            ModelElementOrSubtype::SessionSpec(inner) => inner.extract_key(),
            ModelElementOrSubtype::ComponentSpec(inner) => inner.extract_key(),
            ModelElementOrSubtype::RequirementSpec(inner) => inner.extract_key(),
            ModelElementOrSubtype::SamplingStrategySpec(inner) => inner.extract_key(),
            ModelElementOrSubtype::PluginSpec(inner) => inner.extract_key(),
            ModelElementOrSubtype::HookPayloadSpec(inner) => inner.extract_key(),
            ModelElementOrSubtype::TelemetryMetricSpec(inner) => inner.extract_key(),
            ModelElementOrSubtype::CliCommandSpec(inner) => inner.extract_key(),
            ModelElementOrSubtype::ApiModelSpec(inner) => inner.extract_key(),
        }
    }
}

#[cfg(feature = "stubgen")]
::pyo3_stub_gen::impl_stub_type!(ModelElementOrSubtype = BackendSpec | FormatterSpec | ContextSpec | SessionSpec | ComponentSpec | RequirementSpec | SamplingStrategySpec | PluginSpec | HookPayloadSpec | TelemetryMetricSpec | CliCommandSpec | ApiModelSpec);

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct BackendSpec {
    #[cfg_attr(feature = "serde", serde(default))]
    pub backend_family: Option<BackendFamilyEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub model_identifier: Option<Vec<ModelIdentifierSpec>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub default_formatter: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub model_options_key: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub supports_streaming: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub supports_tool_calls: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub supports_multimodal: Option<bool>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl BackendSpec {
    #[new]
    #[pyo3(signature = (id, name, backend_family=None, model_identifier=None, default_formatter=None, model_options_key=None, supports_streaming=None, supports_tool_calls=None, supports_multimodal=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, backend_family: Option<BackendFamilyEnum>, model_identifier: Option<serde_utils::PyValue<Vec<ModelIdentifierSpec>>>, default_formatter: Option<String>, model_options_key: Option<Vec<String>>, supports_streaming: Option<bool>, supports_tool_calls: Option<bool>, supports_multimodal: Option<bool>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        let model_identifier = model_identifier.map(|v| v.into_inner());
        BackendSpec{id, name, backend_family, model_identifier, default_formatter, model_options_key, supports_streaming, supports_tool_calls, supports_multimodal, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<BackendSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<BackendSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<BackendSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid BackendSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for BackendSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a BackendSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct FormatterSpec {
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl FormatterSpec {
    #[new]
    #[pyo3(signature = (id, name, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        FormatterSpec{id, name, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<FormatterSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<FormatterSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<FormatterSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid FormatterSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for FormatterSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a FormatterSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ContextSpec {
    #[cfg_attr(feature = "serde", serde(default))]
    pub context_linearity: Option<ContextLinearityEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub stores_component_history: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub accepts_message_attachments: Option<bool>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ContextSpec {
    #[new]
    #[pyo3(signature = (id, name, context_linearity=None, stores_component_history=None, accepts_message_attachments=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, context_linearity: Option<ContextLinearityEnum>, stores_component_history: Option<bool>, accepts_message_attachments: Option<bool>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        ContextSpec{id, name, context_linearity, stores_component_history, accepts_message_attachments, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ContextSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ContextSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ContextSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ContextSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for ContextSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a ContextSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct SessionSpec {
    #[cfg_attr(feature = "serde", serde(default))]
    pub uses_backend: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub uses_context: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub exposed_method: Option<Vec<MethodSpec>>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl SessionSpec {
    #[new]
    #[pyo3(signature = (id, name, uses_backend=None, uses_context=None, exposed_method=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, uses_backend: Option<String>, uses_context: Option<String>, exposed_method: Option<serde_utils::PyValue<Vec<MethodSpec>>>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        let exposed_method = exposed_method.map(|v| v.into_inner());
        SessionSpec{id, name, uses_backend, uses_context, exposed_method, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<SessionSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<SessionSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<SessionSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid SessionSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for SessionSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a SessionSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ComponentSpec {
    #[cfg_attr(feature = "serde", serde(default))]
    pub component_category: Option<ComponentCategoryEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub input_modality: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub parsed_output_type: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ComponentSpec {
    #[new]
    #[pyo3(signature = (id, name, component_category=None, input_modality=None, parsed_output_type=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, component_category: Option<ComponentCategoryEnum>, input_modality: Option<Vec<String>>, parsed_output_type: Option<String>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        ComponentSpec{id, name, component_category, input_modality, parsed_output_type, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ComponentSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ComponentSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ComponentSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ComponentSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for ComponentSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a ComponentSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct RequirementSpec {
    #[cfg_attr(feature = "serde", serde(default))]
    pub validation_style: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub may_trigger_repair: Option<bool>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl RequirementSpec {
    #[new]
    #[pyo3(signature = (id, name, validation_style=None, may_trigger_repair=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, validation_style: Option<String>, may_trigger_repair: Option<bool>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        RequirementSpec{id, name, validation_style, may_trigger_repair, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<RequirementSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<RequirementSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<RequirementSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid RequirementSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for RequirementSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a RequirementSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct SamplingStrategySpec {
    #[cfg_attr(feature = "serde", serde(default))]
    pub selection_policy: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub loop_budget_hint: Option<isize>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub may_trigger_repair: Option<bool>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl SamplingStrategySpec {
    #[new]
    #[pyo3(signature = (id, name, selection_policy=None, loop_budget_hint=None, may_trigger_repair=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, selection_policy: Option<String>, loop_budget_hint: Option<isize>, may_trigger_repair: Option<bool>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        SamplingStrategySpec{id, name, selection_policy, loop_budget_hint, may_trigger_repair, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<SamplingStrategySpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<SamplingStrategySpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<SamplingStrategySpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid SamplingStrategySpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for SamplingStrategySpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a SamplingStrategySpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PluginSpec {
    #[cfg_attr(feature = "serde", serde(default))]
    pub plugin_mode: Option<PluginModeEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub hook_type: Option<Vec<HookTypeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub payload_model: Option<Vec<HookPayloadSpec>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub plugin_priority: Option<isize>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PluginSpec {
    #[new]
    #[pyo3(signature = (id, name, plugin_mode=None, hook_type=None, payload_model=None, plugin_priority=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, plugin_mode: Option<PluginModeEnum>, hook_type: Option<Vec<HookTypeEnum>>, payload_model: Option<serde_utils::PyValue<Vec<HookPayloadSpec>>>, plugin_priority: Option<isize>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        let payload_model = payload_model.map(|v| v.into_inner());
        PluginSpec{id, name, plugin_mode, hook_type, payload_model, plugin_priority, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PluginSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PluginSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PluginSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PluginSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PluginSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a PluginSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct HookPayloadSpec {
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub hook_type: Option<Vec<HookTypeEnum>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub lifecycle_role: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl HookPayloadSpec {
    #[new]
    #[pyo3(signature = (id, name, hook_type=None, lifecycle_role=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, hook_type: Option<Vec<HookTypeEnum>>, lifecycle_role: Option<String>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        HookPayloadSpec{id, name, hook_type, lifecycle_role, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<HookPayloadSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<HookPayloadSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<HookPayloadSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid HookPayloadSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for HookPayloadSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a HookPayloadSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TelemetryMetricSpec {
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub metric_name: Option<Vec<String>>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TelemetryMetricSpec {
    #[new]
    #[pyo3(signature = (id, name, metric_name=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, metric_name: Option<Vec<String>>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        TelemetryMetricSpec{id, name, metric_name, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TelemetryMetricSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TelemetryMetricSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TelemetryMetricSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TelemetryMetricSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TelemetryMetricSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a TelemetryMetricSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct CliCommandSpec {
    #[cfg_attr(feature = "serde", serde(default))]
    pub command_group: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub command_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub command_purpose: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub input_model: Option<Vec<ApiModelSpec>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub output_model: Option<Vec<ApiModelSpec>>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl CliCommandSpec {
    #[new]
    #[pyo3(signature = (id, name, command_group=None, command_path=None, command_purpose=None, input_model=None, output_model=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, command_group: Option<String>, command_path: Option<String>, command_purpose: Option<String>, input_model: Option<serde_utils::PyValue<Vec<ApiModelSpec>>>, output_model: Option<serde_utils::PyValue<Vec<ApiModelSpec>>>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        let input_model = input_model.map(|v| v.into_inner());
        let output_model = output_model.map(|v| v.into_inner());
        CliCommandSpec{id, name, command_group, command_path, command_purpose, input_model, output_model, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<CliCommandSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<CliCommandSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<CliCommandSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid CliCommandSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for CliCommandSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a CliCommandSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ApiModelSpec {
    #[cfg_attr(feature = "serde", serde(default))]
    pub request_or_response: Option<RequestResponseEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub openai_object_type: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub has_field: Option<Vec<ApiFieldSpec>>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ApiModelSpec {
    #[new]
    #[pyo3(signature = (id, name, request_or_response=None, openai_object_type=None, has_field=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, request_or_response: Option<RequestResponseEnum>, openai_object_type: Option<String>, has_field: Option<serde_utils::PyValue<Vec<ApiFieldSpec>>>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        let has_field = has_field.map(|v| v.into_inner());
        ApiModelSpec{id, name, request_or_response, openai_object_type, has_field, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ApiModelSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ApiModelSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ApiModelSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ApiModelSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for ApiModelSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a ApiModelSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ApiFieldSpec {
    #[cfg_attr(feature = "serde", serde(default))]
    pub field_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub field_type: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub required_field: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub allows_null: Option<bool>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ApiFieldSpec {
    #[new]
    #[pyo3(signature = (id, name, field_name=None, field_type=None, required_field=None, allows_null=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, field_name: Option<String>, field_type: Option<String>, required_field: Option<bool>, allows_null: Option<bool>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        ApiFieldSpec{id, name, field_name, field_type, required_field, allows_null, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ApiFieldSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ApiFieldSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ApiFieldSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ApiFieldSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for ApiFieldSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a ApiFieldSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct MethodSpec {
    #[cfg_attr(feature = "serde", serde(default))]
    pub method_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub method_signature: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub lifecycle_role: Option<String>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl MethodSpec {
    #[new]
    #[pyo3(signature = (id, name, method_name=None, method_signature=None, lifecycle_role=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, method_name: Option<String>, method_signature: Option<String>, lifecycle_role: Option<String>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        MethodSpec{id, name, method_name, method_signature, lifecycle_role, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<MethodSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<MethodSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<MethodSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid MethodSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for MethodSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a MethodSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ModelIdentifierSpec {
    #[cfg_attr(feature = "serde", serde(default))]
    pub hf_model_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub ollama_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub watsonx_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub openai_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub bedrock_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub provider_name: Option<Vec<String>>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ModelIdentifierSpec {
    #[new]
    #[pyo3(signature = (id, name, hf_model_name=None, ollama_name=None, watsonx_name=None, openai_name=None, bedrock_name=None, provider_name=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, hf_model_name: Option<String>, ollama_name: Option<String>, watsonx_name: Option<String>, openai_name: Option<String>, bedrock_name: Option<String>, provider_name: Option<Vec<String>>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        ModelIdentifierSpec{id, name, hf_model_name, ollama_name, watsonx_name, openai_name, bedrock_name, provider_name, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ModelIdentifierSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ModelIdentifierSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ModelIdentifierSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ModelIdentifierSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for ModelIdentifierSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a ModelIdentifierSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct IntrinsicAdapterSpec {
    #[cfg_attr(feature = "serde", serde(default))]
    pub repo_id: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub adapter_type: Option<Vec<AdapterTypeEnum>>,
    pub id: uriorcurie,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub module_path: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub source_file: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub package_kind: Option<PackageKindEnum>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub element_kind: Option<ElementKindEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub coverage_scope: Option<Vec<CoverageScopeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub tags: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl IntrinsicAdapterSpec {
    #[new]
    #[pyo3(signature = (id, name, repo_id=None, adapter_type=None, description=None, module_path=None, source_file=None, package_kind=None, element_kind=None, coverage_scope=None, tags=None))]
    pub fn new(id: uriorcurie, name: String, repo_id: Option<String>, adapter_type: Option<Vec<AdapterTypeEnum>>, description: Option<String>, module_path: Option<String>, source_file: Option<String>, package_kind: Option<PackageKindEnum>, element_kind: Option<ElementKindEnum>, coverage_scope: Option<Vec<CoverageScopeEnum>>, tags: Option<Vec<String>>) -> Self {
        IntrinsicAdapterSpec{id, name, repo_id, adapter_type, description, module_path, source_file, package_kind, element_kind, coverage_scope, tags}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<IntrinsicAdapterSpec>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<IntrinsicAdapterSpec> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<IntrinsicAdapterSpec>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid IntrinsicAdapterSpec",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for IntrinsicAdapterSpec {
    type Key   = uriorcurie;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a IntrinsicAdapterSpec from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}




#[cfg(feature = "stubgen")]
define_stub_info_gatherer!(stub_info);
