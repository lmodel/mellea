from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "2026-05-26"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'analyzed_scope': {'tag': 'analyzed_scope',
                                        'value': 'mellea+cli (linkml/ excluded)'},
                     'coverage_inventory': {'tag': 'coverage_inventory',
                                            'value': 'cli: total=86 (CLASS=42 '
                                                     'DATACLASS=5 ENUM=4 '
                                                     'PYDANTIC_MODEL=20 '
                                                     'TYPED_DICT=15)\n'
                                                     'mellea/backends: total=28 '
                                                     '(CLASS=22 DATACLASS=2 ENUM=1 '
                                                     'MIXIN=1 PYDANTIC_MODEL=2)\n'
                                                     'mellea/core: total=27 '
                                                     '(CLASS=20 DATACLASS=5 ENUM=1 '
                                                     'PROTOCOL=1)\n'
                                                     'mellea/formatters: total=57 '
                                                     '(CLASS=39 ENUM=1 MIXIN=1 '
                                                     'PYDANTIC_MODEL=16)\n'
                                                     'mellea/helpers: total=6 '
                                                     '(CLASS=2 ENUM=1 '
                                                     'PYDANTIC_MODEL=1 '
                                                     'TYPED_DICT=2)\n'
                                                     'mellea/plugins: total=32 '
                                                     '(CLASS=28 DATACLASS=2 '
                                                     'ENUM=2)\n'
                                                     'mellea/stdlib: total=69 '
                                                     '(CLASS=50 DATACLASS=10 '
                                                     'ENUM=1 PROTOCOL=2 '
                                                     'PYDANTIC_MODEL=4 '
                                                     'TYPED_DICT=2)\n'
                                                     'mellea/telemetry: total=11 '
                                                     '(CLASS=11)\n'
                                                     'enum_total: 11'},
                     'coverage_target': {'tag': 'coverage_target',
                                         'value': 'core-library-and-cli'},
                     'generated_by': {'tag': 'generated_by',
                                      'value': 'linkml/scripts/schema_to_linkml.py'},
                     'generated_on': {'tag': 'generated_on',
                                      'value': '2026-05-26'}},
     'default_prefix': 'mellea',
     'default_range': 'string',
     'description': 'LinkML schema describing the Mellea codebase architecture and '
                    'public data models. Generated from Python sources by '
                    'linkml/scripts/schema_to_linkml.py.',
     'id': 'https://w3id.org/lmodel/mellea',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'mellea',
     'prefixes': {'attack': {'prefix_prefix': 'attack',
                             'prefix_reference': 'https://w3id.org/lmodel/attack/'},
                  'common_domain_model': {'prefix_prefix': 'common_domain_model',
                                          'prefix_reference': 'https://w3id.org/lmodel/common-domain-model/'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'iso27001': {'prefix_prefix': 'iso27001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso27001/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'mcp': {'prefix_prefix': 'mcp',
                          'prefix_reference': 'https://w3id.org/lmodel/mcp/'},
                  'mellea': {'prefix_prefix': 'mellea',
                             'prefix_reference': 'https://w3id.org/lmodel/mellea/'},
                  'nexus': {'prefix_prefix': 'nexus',
                            'prefix_reference': 'https://ibm.github.io/ai-atlas-nexus/ontology/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'spdx': {'prefix_prefix': 'spdx',
                           'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/'}},
     'see_also': ['https://github.com/lmodel/mellea',
                  'https://lmodel.github.io/mellea'],
     'source': 'https://github.com/lmodel/mellea',
     'source_file': 'src/mellea/schema/mellea.yaml',
     'subsets': {'core_runtime': {'description': 'Core runtime abstractions and '
                                                 'execution flow.',
                                  'from_schema': 'https://w3id.org/lmodel/mellea',
                                  'name': 'core_runtime'},
                 'interface_surface': {'description': 'API or CLI-facing '
                                                      'interfaces and wire models.',
                                       'from_schema': 'https://w3id.org/lmodel/mellea',
                                       'name': 'interface_surface'},
                 'observability': {'description': 'Telemetry, plugin hooks, and '
                                                  'instrumentation.',
                                   'from_schema': 'https://w3id.org/lmodel/mellea',
                                   'name': 'observability'}},
     'title': 'mellea',
     'types': {'PythonDottedPath': {'base': 'str',
                                    'description': 'Python import-style dotted '
                                                   'path.',
                                    'from_schema': 'https://w3id.org/lmodel/mellea',
                                    'name': 'PythonDottedPath',
                                    'pattern': '^[A-Za-z_][A-Za-z0-9_]*(\\.[A-Za-z_][A-Za-z0-9_]*)*$',
                                    'uri': 'xsd:string'},
               'RepositoryRelativePath': {'base': 'str',
                                          'description': 'Relative path from '
                                                         'repository root.',
                                          'from_schema': 'https://w3id.org/lmodel/mellea',
                                          'name': 'RepositoryRelativePath',
                                          'pattern': '^[^\\0]+$',
                                          'uri': 'xsd:string'}}} )

class PackageKindEnum(str, Enum):
    """
    Logical package buckets used to classify Mellea source modules.
    """
    CORE = "CORE"
    """
    core
    """
    STDLIB = "STDLIB"
    """
    stdlib
    """
    BACKENDS = "BACKENDS"
    """
    backends
    """
    FORMATTERS = "FORMATTERS"
    """
    formatters
    """
    HELPERS = "HELPERS"
    """
    helpers
    """
    PLUGINS = "PLUGINS"
    """
    plugins
    """
    TELEMETRY = "TELEMETRY"
    """
    telemetry
    """
    CLI = "CLI"
    """
    cli
    """
    DOCS_EXAMPLES = "DOCS_EXAMPLES"
    """
    docs examples
    """
    TEST = "TEST"
    """
    test
    """


class ElementKindEnum(str, Enum):
    """
    Kind of Python declaration captured by a ModelElement entry.
    """
    CLASS = "CLASS"
    """
    class
    """
    ENUM = "ENUM"
    """
    enum
    """
    DATACLASS = "DATACLASS"
    """
    dataclass
    """
    TYPED_DICT = "TYPED_DICT"
    """
    typed dict
    """
    PYDANTIC_MODEL = "PYDANTIC_MODEL"
    """
    pydantic model
    """
    PROTOCOL = "PROTOCOL"
    """
    protocol
    """
    FUNCTION = "FUNCTION"
    """
    function
    """
    MIXIN = "MIXIN"
    """
    mixin
    """


class CoverageScopeEnum(str, Enum):
    """
    Where in the project an element surfaces (source, API, CLI, ...).
    """
    SOURCE = "SOURCE"
    """
    source
    """
    API = "API"
    """
    api
    """
    CLI = "CLI"
    """
    cli
    """
    EXAMPLE = "EXAMPLE"
    """
    example
    """
    TEST = "TEST"
    """
    test
    """


class ContextLinearityEnum(str, Enum):
    """
    Whether a Mellea context preserves linear ordering or not.
    """
    LINEAR = "LINEAR"
    """
    Sequential, ordered history.
    """
    NON_LINEAR = "NON_LINEAR"
    """
    Tree- or graph-shaped history.
    """


class ComponentCategoryEnum(str, Enum):
    """
    High-level category of a Mellea stdlib component.
    """
    INSTRUCTION = "INSTRUCTION"
    """
    instruction
    """
    MESSAGE = "MESSAGE"
    """
    message
    """
    TOOL_MESSAGE = "TOOL_MESSAGE"
    """
    tool message
    """
    DOCUMENT = "DOCUMENT"
    """
    document
    """
    INTRINSIC = "INTRINSIC"
    """
    intrinsic
    """
    MOBJECT = "MOBJECT"
    """
    mobject
    """
    QUERY = "QUERY"
    """
    query
    """
    TRANSFORM = "TRANSFORM"
    """
    transform
    """
    GENSTUB = "GENSTUB"
    """
    genstub
    """
    REQUIREMENT = "REQUIREMENT"
    """
    requirement
    """
    STREAM_EVENT = "STREAM_EVENT"
    """
    stream event
    """


class RequestResponseEnum(str, Enum):
    """
    Direction of a wire model (HTTP request, response, or both).
    """
    REQUEST = "REQUEST"
    """
    Inbound request payload.
    """
    RESPONSE = "RESPONSE"
    """
    Outbound response payload.
    """
    BOTH = "BOTH"
    """
    Model used in both directions (rare).
    """


class BackendFamilyEnum(str, Enum):
    """
    Backend families discovered under mellea/backends/.
    """
    BEDROCK = "BEDROCK"
    """
    Backend family backed by mellea/backends/bedrock.py.
    """
    DUMMY = "DUMMY"
    """
    Backend family backed by mellea/backends/dummy.py.
    """
    HUGGINGFACE = "HUGGINGFACE"
    """
    Backend family backed by mellea/backends/huggingface.py.
    """
    LITELLM = "LITELLM"
    """
    Backend family backed by mellea/backends/litellm.py.
    """
    OLLAMA = "OLLAMA"
    """
    Backend family backed by mellea/backends/ollama.py.
    """
    OPENAI = "OPENAI"
    """
    Backend family backed by mellea/backends/openai.py.
    """
    WATSONX = "WATSONX"
    """
    Backend family backed by mellea/backends/watsonx.py.
    """


class PluginModeEnum(str, Enum):
    """
    Execution mode of a Mellea plugin (derived from PluginMode).
    """
    SEQUENTIAL = "SEQUENTIAL"
    """
    sequential
    """
    TRANSFORM = "TRANSFORM"
    """
    transform
    """
    CONCURRENT = "CONCURRENT"
    """
    concurrent
    """
    AUDIT = "AUDIT"
    """
    audit
    """
    FIRE_AND_FORGET = "FIRE_AND_FORGET"
    """
    fire and forget
    """


class HookTypeEnum(str, Enum):
    """
    Lifecycle hook stages (derived from HookType).
    """
    SESSION_PRE_INIT = "SESSION_PRE_INIT"
    """
    session pre init
    """
    SESSION_POST_INIT = "SESSION_POST_INIT"
    """
    session post init
    """
    SESSION_RESET = "SESSION_RESET"
    """
    session reset
    """
    SESSION_CLEANUP = "SESSION_CLEANUP"
    """
    session cleanup
    """
    COMPONENT_PRE_EXECUTE = "COMPONENT_PRE_EXECUTE"
    """
    component pre execute
    """
    COMPONENT_POST_SUCCESS = "COMPONENT_POST_SUCCESS"
    """
    component post success
    """
    COMPONENT_POST_ERROR = "COMPONENT_POST_ERROR"
    """
    component post error
    """
    GENERATION_PRE_CALL = "GENERATION_PRE_CALL"
    """
    generation pre call
    """
    GENERATION_POST_CALL = "GENERATION_POST_CALL"
    """
    generation post call
    """
    GENERATION_ERROR = "GENERATION_ERROR"
    """
    generation error
    """
    VALIDATION_PRE_CHECK = "VALIDATION_PRE_CHECK"
    """
    validation pre check
    """
    VALIDATION_POST_CHECK = "VALIDATION_POST_CHECK"
    """
    validation post check
    """
    SAMPLING_LOOP_START = "SAMPLING_LOOP_START"
    """
    sampling loop start
    """
    SAMPLING_ITERATION = "SAMPLING_ITERATION"
    """
    sampling iteration
    """
    SAMPLING_REPAIR = "SAMPLING_REPAIR"
    """
    sampling repair
    """
    SAMPLING_LOOP_END = "SAMPLING_LOOP_END"
    """
    sampling loop end
    """
    TOOL_PRE_INVOKE = "TOOL_PRE_INVOKE"
    """
    tool pre invoke
    """
    TOOL_POST_INVOKE = "TOOL_POST_INVOKE"
    """
    tool post invoke
    """


class AdapterTypeEnum(str, Enum):
    """
    Adapter implementation type (derived from AdapterType).
    """
    LORA = "LORA"
    """
    lora
    """
    ALORA = "ALORA"
    """
    alora
    """



class NamedElement(ConfiguredBaseModel):
    """
    Abstract base for any named, identifiable schema element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'close_mappings': ['nexus:Entity', 'iso27001:NamedEntity', 'spdx:Element'],
         'from_schema': 'https://w3id.org/lmodel/mellea',
         'related_mappings': ['attack:StixEntity',
                              'common_domain_model:InventoryRecord',
                              'mcp:HasName']})

    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class RepositoryCatalog(NamedElement):
    """
    Top-level catalog rooting the analysed repository snapshot.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['spdx:Sbom'],
         'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['interface_surface'],
         'related_mappings': ['nexus:Container',
                              'attack:AttackBundle',
                              'common_domain_model:Portfolio',
                              'common_domain_model:PortfolioState',
                              'iso27001:DocumentedInformation',
                              'spdx:SpdxDocument'],
         'tree_root': True})

    repository_root: Optional[str] = Field(default=None, description="""Slot describing the repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RepositoryCatalog']} })
    analyzed_on: Optional[date] = Field(default=None, description="""Slot describing the analyzed on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RepositoryCatalog']} })
    includes_path: Optional[list[str]] = Field(default=None, description="""Slot describing the includes path.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RepositoryCatalog']} })
    excludes_path: Optional[list[str]] = Field(default=None, description="""Slot describing the excludes path.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RepositoryCatalog']} })
    declares_element: Optional[list[ModelElement]] = Field(default=None, description="""Slot describing the declares element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RepositoryCatalog', 'PythonPackage']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class PythonPackage(NamedElement):
    """
    A logical Python package (directory) inside the repository.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['spdx:Package'],
         'from_schema': 'https://w3id.org/lmodel/mellea',
         'narrow_mappings': ['nexus:Entity'],
         'related_mappings': ['common_domain_model:Position']})

    package_name: Optional[str] = Field(default=None, description="""Slot describing the package name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PythonPackage']} })
    depends_on_package: Optional[list[PythonPackage]] = Field(default=None, description="""Slot describing the depends on package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PythonPackage']} })
    declares_element: Optional[list[ModelElement]] = Field(default=None, description="""Slot describing the declares element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RepositoryCatalog', 'PythonPackage']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class ModelElement(NamedElement):
    """
    Abstract base for concrete architectural elements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/mellea',
         'related_mappings': ['common_domain_model:ContractBase', 'spdx:Element']})

    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class BackendSpec(ModelElement):
    """
    Specification of a Mellea backend implementation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nexus:AiProvider'],
         'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['core_runtime', 'interface_surface'],
         'related_mappings': ['nexus:AiSystem', 'mcp:Implementation']})

    backend_family: Optional[BackendFamilyEnum] = Field(default=None, description="""Slot describing the backend family.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BackendSpec']} })
    model_identifier: Optional[list[ModelIdentifierSpec]] = Field(default=None, description="""Slot describing the model identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BackendSpec']} })
    default_formatter: Optional[str] = Field(default=None, description="""Slot describing the default formatter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BackendSpec']} })
    model_options_key: Optional[list[str]] = Field(default=None, description="""Slot describing the model options key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BackendSpec']} })
    supports_streaming: Optional[bool] = Field(default=None, description="""Slot describing the supports streaming.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BackendSpec']} })
    supports_tool_calls: Optional[bool] = Field(default=None, description="""Slot describing the supports tool calls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BackendSpec']} })
    supports_multimodal: Optional[bool] = Field(default=None, description="""Slot describing the supports multimodal.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BackendSpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class FormatterSpec(ModelElement):
    """
    Specification of an output formatter for a backend.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['core_runtime'],
         'related_mappings': ['nexus:Modality', 'mcp:ContentBlock']})

    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class ContextSpec(ModelElement):
    """
    Specification of a context implementation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['core_runtime'],
         'related_mappings': ['nexus:AiLifecyclePhase']})

    context_linearity: Optional[ContextLinearityEnum] = Field(default=None, description="""Slot describing the context linearity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContextSpec']} })
    stores_component_history: Optional[bool] = Field(default=None, description="""Slot describing the stores component history.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContextSpec']} })
    accepts_message_attachments: Optional[bool] = Field(default=None, description="""Slot describing the accepts message attachments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContextSpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class SessionSpec(ModelElement):
    """
    Specification of a Mellea session.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['core_runtime'],
         'related_mappings': ['nexus:AiTask',
                              'iso27001:RiskAssessmentProcess',
                              'mcp:Task']})

    uses_backend: Optional[str] = Field(default=None, description="""Slot describing the uses backend.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SessionSpec']} })
    uses_context: Optional[str] = Field(default=None, description="""Slot describing the uses context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SessionSpec']} })
    exposed_method: Optional[list[MethodSpec]] = Field(default=None, description="""Slot describing the exposed method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SessionSpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class ComponentSpec(ModelElement):
    """
    Specification of a Mellea stdlib component type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nexus:AIComponent', 'mcp:Tool'],
         'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['core_runtime']})

    component_category: Optional[ComponentCategoryEnum] = Field(default=None, description="""Slot describing the component category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentSpec']} })
    input_modality: Optional[list[str]] = Field(default=None, description="""Slot describing the input modality.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentSpec']} })
    parsed_output_type: Optional[str] = Field(default=None, description="""Slot describing the parsed output type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentSpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class RequirementSpec(ModelElement):
    """
    Specification of a requirement validator.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['core_runtime'],
         'related_mappings': ['nexus:Requirement',
                              'nexus:Rule',
                              'iso27001:SecurityControl',
                              'iso27001:InformationSecurityObjective']})

    validation_style: Optional[str] = Field(default=None, description="""Slot describing the validation style.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequirementSpec']} })
    may_trigger_repair: Optional[bool] = Field(default=None, description="""Slot describing the may trigger repair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequirementSpec', 'SamplingStrategySpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class SamplingStrategySpec(ModelElement):
    """
    Specification of a sampling-loop strategy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['mcp:SamplingCapability'],
         'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['core_runtime'],
         'related_mappings': ['nexus:Action', 'mcp:ModelPreferences']})

    selection_policy: Optional[str] = Field(default=None, description="""Slot describing the selection policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SamplingStrategySpec']} })
    loop_budget_hint: Optional[int] = Field(default=None, description="""Slot describing the loop budget hint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SamplingStrategySpec']} })
    may_trigger_repair: Optional[bool] = Field(default=None, description="""Slot describing the may trigger repair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequirementSpec', 'SamplingStrategySpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class PluginSpec(ModelElement):
    """
    Specification of a Mellea plugin and the hooks it registers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['spdx:Extension'],
         'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['observability'],
         'related_mappings': ['nexus:AIComponent',
                              'attack:Analytic',
                              'iso27001:OperationalProcedure',
                              'mcp:ExtensionAppCapability']})

    plugin_mode: Optional[PluginModeEnum] = Field(default=None, description="""Slot describing the plugin mode.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PluginSpec']} })
    hook_type: Optional[list[HookTypeEnum]] = Field(default=None, description="""Slot describing the hook type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PluginSpec', 'HookPayloadSpec']} })
    payload_model: Optional[list[HookPayloadSpec]] = Field(default=None, description="""Slot describing the payload model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PluginSpec']} })
    plugin_priority: Optional[int] = Field(default=None, description="""Slot describing the plugin priority.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PluginSpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class HookPayloadSpec(ModelElement):
    """
    Specification of a hook payload model.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['observability'],
         'related_mappings': ['nexus:Fact',
                              'attack:DataComponent',
                              'iso27001:InformationSecurityEvent',
                              'mcp:MetaObject',
                              'spdx:Annotation']})

    hook_type: Optional[list[HookTypeEnum]] = Field(default=None, description="""Slot describing the hook type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PluginSpec', 'HookPayloadSpec']} })
    lifecycle_role: Optional[str] = Field(default=None, description="""Slot describing the lifecycle role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HookPayloadSpec', 'MethodSpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class TelemetryMetricSpec(ModelElement):
    """
    Specification of a telemetry metric emitted by Mellea.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nexus:MetricConfig', 'iso27001:MonitoringItem'],
         'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['observability'],
         'related_mappings': ['nexus:AiEval',
                              'attack:DataSource',
                              'iso27001:MonitoringProgram',
                              'spdx:AIPackage']})

    metric_name: Optional[list[str]] = Field(default=None, description="""Slot describing the metric name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TelemetryMetricSpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class CliCommandSpec(ModelElement):
    """
    Specification of a CLI command exposed under `m`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['interface_surface'],
         'related_mappings': ['attack:Tool',
                              'iso27001:OperationalProcedure',
                              'spdx:Tool']})

    command_group: Optional[str] = Field(default=None, description="""Slot describing the command group.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CliCommandSpec']} })
    command_path: Optional[str] = Field(default=None, description="""Slot describing the command path.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CliCommandSpec']} })
    command_purpose: Optional[str] = Field(default=None, description="""Slot describing the command purpose.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CliCommandSpec']} })
    input_model: Optional[list[ApiModelSpec]] = Field(default=None, description="""Slot describing the input model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CliCommandSpec']} })
    output_model: Optional[list[ApiModelSpec]] = Field(default=None, description="""Slot describing the output model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CliCommandSpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class ApiModelSpec(ModelElement):
    """
    Specification of an HTTP API wire model.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['interface_surface'],
         'related_mappings': ['nexus:Input',
                              'mcp:JSONRPCRequest',
                              'mcp:JSONRPCResponse']})

    request_or_response: Optional[RequestResponseEnum] = Field(default=None, description="""Slot describing the request or response.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ApiModelSpec']} })
    openai_object_type: Optional[str] = Field(default=None, description="""Slot describing the openai object type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ApiModelSpec']} })
    has_field: Optional[list[ApiFieldSpec]] = Field(default=None, description="""Slot describing the has field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ApiModelSpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class ApiFieldSpec(NamedElement):
    """
    Specification of a single field in an API model.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['interface_surface'],
         'related_mappings': ['spdx:DictionaryEntry']})

    field_name: Optional[str] = Field(default=None, description="""Slot describing the field name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ApiFieldSpec']} })
    field_type: Optional[str] = Field(default=None, description="""Slot describing the field type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ApiFieldSpec']} })
    required_field: Optional[bool] = Field(default=None, description="""Slot describing the required field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ApiFieldSpec']} })
    allows_null: Optional[bool] = Field(default=None, description="""Slot describing the allows null.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ApiFieldSpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class MethodSpec(NamedElement):
    """
    Specification of a method exposed by a runtime class.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/mellea', 'in_subset': ['core_runtime']})

    method_name: Optional[str] = Field(default=None, description="""Slot describing the method name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MethodSpec']} })
    method_signature: Optional[str] = Field(default=None, description="""Slot describing the method signature.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MethodSpec']} })
    lifecycle_role: Optional[str] = Field(default=None, description="""Slot describing the lifecycle role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HookPayloadSpec', 'MethodSpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class ModelIdentifierSpec(NamedElement):
    """
    Cross-provider identifier table for a single model.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nexus:AiModel',
                            'nexus:LargeLanguageModel',
                            'spdx:AIPackage'],
         'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['interface_surface'],
         'related_mappings': ['nexus:ModelInfo',
                              'common_domain_model:positionIdentifier',
                              'mcp:ModelHint']})

    hf_model_name: Optional[str] = Field(default=None, description="""Slot describing the hf model name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelIdentifierSpec']} })
    ollama_name: Optional[str] = Field(default=None, description="""Slot describing the ollama name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelIdentifierSpec']} })
    watsonx_name: Optional[str] = Field(default=None, description="""Slot describing the watsonx name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelIdentifierSpec']} })
    openai_name: Optional[str] = Field(default=None, description="""Slot describing the openai name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelIdentifierSpec']} })
    bedrock_name: Optional[str] = Field(default=None, description="""Slot describing the bedrock name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelIdentifierSpec']} })
    provider_name: Optional[list[str]] = Field(default=None, description="""Slot describing the provider name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelIdentifierSpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


class IntrinsicAdapterSpec(NamedElement):
    """
    Specification of an intrinsic adapter (LoRA / aLoRA).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nexus:Adapter', 'nexus:LLMIntrinsic', 'spdx:AIPackage'],
         'from_schema': 'https://w3id.org/lmodel/mellea',
         'in_subset': ['interface_surface'],
         'related_mappings': ['spdx:Relationship']})

    repo_id: Optional[str] = Field(default=None, description="""Slot describing the repo id.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IntrinsicAdapterSpec']} })
    adapter_type: Optional[list[AdapterTypeEnum]] = Field(default=None, description="""Slot describing the adapter type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IntrinsicAdapterSpec']} })
    id: str = Field(default=..., description="""Stable identifier for a schema element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement'], 'slot_uri': 'schema:description'} })
    module_path: Optional[str] = Field(default=None, description="""Python module path where this element is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    source_file: Optional[str] = Field(default=None, description="""Source file relative to repository root.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    package_kind: Optional[PackageKindEnum] = Field(default=None, description="""Package bucket.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    element_kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind of Python declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    coverage_scope: Optional[list[CoverageScopeEnum]] = Field(default=None, description="""Where this element surfaces (source/API/CLI/example/test).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })
    tags: Optional[list[str]] = Field(default=None, description="""Free-form classification tags.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedElement']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedElement.model_rebuild()
RepositoryCatalog.model_rebuild()
PythonPackage.model_rebuild()
ModelElement.model_rebuild()
BackendSpec.model_rebuild()
FormatterSpec.model_rebuild()
ContextSpec.model_rebuild()
SessionSpec.model_rebuild()
ComponentSpec.model_rebuild()
RequirementSpec.model_rebuild()
SamplingStrategySpec.model_rebuild()
PluginSpec.model_rebuild()
HookPayloadSpec.model_rebuild()
TelemetryMetricSpec.model_rebuild()
CliCommandSpec.model_rebuild()
ApiModelSpec.model_rebuild()
ApiFieldSpec.model_rebuild()
MethodSpec.model_rebuild()
ModelIdentifierSpec.model_rebuild()
IntrinsicAdapterSpec.model_rebuild()
