# Auto generated from mellea.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-26T21:03:11
# Schema: mellea
#
# id: https://w3id.org/lmodel/mellea
# description: LinkML schema describing the Mellea codebase architecture and public data models. Generated from Python sources by linkml/scripts/schema_to_linkml.py.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.11.0"
version = "2026-05-26"

# Namespaces
ATTACK = CurieNamespace('attack', 'https://w3id.org/lmodel/attack/')
COMMON_DOMAIN_MODEL = CurieNamespace('common_domain_model', 'https://w3id.org/lmodel/common-domain-model/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
GIST_LINKML = CurieNamespace('gist_linkml', 'https://w3id.org/lmodel/gist/')
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MCP = CurieNamespace('mcp', 'https://w3id.org/lmodel/mcp/')
MELLEA = CurieNamespace('mellea', 'https://w3id.org/lmodel/mellea/')
NEXUS = CurieNamespace('nexus', 'https://ibm.github.io/ai-atlas-nexus/ontology/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SPDX = CurieNamespace('spdx', 'https://spdx.org/rdf/3.0.1/terms/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MELLEA


# Types
class PythonDottedPath(str):
    """ Python import-style dotted path. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "PythonDottedPath"
    type_model_uri = MELLEA.PythonDottedPath


class RepositoryRelativePath(str):
    """ Relative path from repository root. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "RepositoryRelativePath"
    type_model_uri = MELLEA.RepositoryRelativePath


# Class references
class NamedElementId(URIorCURIE):
    pass


class RepositoryCatalogId(NamedElementId):
    pass


class PythonPackageId(NamedElementId):
    pass


class ModelElementId(NamedElementId):
    pass


class BackendSpecId(ModelElementId):
    pass


class FormatterSpecId(ModelElementId):
    pass


class ContextSpecId(ModelElementId):
    pass


class SessionSpecId(ModelElementId):
    pass


class ComponentSpecId(ModelElementId):
    pass


class RequirementSpecId(ModelElementId):
    pass


class SamplingStrategySpecId(ModelElementId):
    pass


class PluginSpecId(ModelElementId):
    pass


class HookPayloadSpecId(ModelElementId):
    pass


class TelemetryMetricSpecId(ModelElementId):
    pass


class CliCommandSpecId(ModelElementId):
    pass


class ApiModelSpecId(ModelElementId):
    pass


class ApiFieldSpecId(NamedElementId):
    pass


class MethodSpecId(NamedElementId):
    pass


class ModelIdentifierSpecId(NamedElementId):
    pass


class IntrinsicAdapterSpecId(NamedElementId):
    pass


@dataclass(repr=False)
class NamedElement(YAMLRoot):
    """
    Abstract base for any named, identifiable schema element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["NamedElement"]
    class_class_curie: ClassVar[str] = "mellea:NamedElement"
    class_name: ClassVar[str] = "NamedElement"
    class_model_uri: ClassVar[URIRef] = MELLEA.NamedElement

    id: Union[str, NamedElementId] = None
    name: str = None
    description: Optional[str] = None
    module_path: Optional[str] = None
    source_file: Optional[str] = None
    package_kind: Optional[Union[str, "PackageKindEnum"]] = None
    element_kind: Optional[Union[str, "ElementKindEnum"]] = None
    coverage_scope: Optional[Union[Union[str, "CoverageScopeEnum"], list[Union[str, "CoverageScopeEnum"]]]] = empty_list()
    tags: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedElementId):
            self.id = NamedElementId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.module_path is not None and not isinstance(self.module_path, str):
            self.module_path = str(self.module_path)

        if self.source_file is not None and not isinstance(self.source_file, str):
            self.source_file = str(self.source_file)

        if self.package_kind is not None and not isinstance(self.package_kind, PackageKindEnum):
            self.package_kind = PackageKindEnum(self.package_kind)

        if self.element_kind is not None and not isinstance(self.element_kind, ElementKindEnum):
            self.element_kind = ElementKindEnum(self.element_kind)

        if not isinstance(self.coverage_scope, list):
            self.coverage_scope = [self.coverage_scope] if self.coverage_scope is not None else []
        self.coverage_scope = [v if isinstance(v, CoverageScopeEnum) else CoverageScopeEnum(v) for v in self.coverage_scope]

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RepositoryCatalog(NamedElement):
    """
    Top-level catalog rooting the analysed repository snapshot.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["RepositoryCatalog"]
    class_class_curie: ClassVar[str] = "mellea:RepositoryCatalog"
    class_name: ClassVar[str] = "RepositoryCatalog"
    class_model_uri: ClassVar[URIRef] = MELLEA.RepositoryCatalog

    id: Union[str, RepositoryCatalogId] = None
    name: str = None
    repository_root: Optional[str] = None
    analyzed_on: Optional[Union[str, XSDDate]] = None
    includes_path: Optional[Union[str, list[str]]] = empty_list()
    excludes_path: Optional[Union[str, list[str]]] = empty_list()
    declares_element: Optional[Union[dict[Union[str, ModelElementId], Union[dict, "ModelElement"]], list[Union[dict, "ModelElement"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RepositoryCatalogId):
            self.id = RepositoryCatalogId(self.id)

        if self.repository_root is not None and not isinstance(self.repository_root, str):
            self.repository_root = str(self.repository_root)

        if self.analyzed_on is not None and not isinstance(self.analyzed_on, XSDDate):
            self.analyzed_on = XSDDate(self.analyzed_on)

        if not isinstance(self.includes_path, list):
            self.includes_path = [self.includes_path] if self.includes_path is not None else []
        self.includes_path = [v if isinstance(v, str) else str(v) for v in self.includes_path]

        if not isinstance(self.excludes_path, list):
            self.excludes_path = [self.excludes_path] if self.excludes_path is not None else []
        self.excludes_path = [v if isinstance(v, str) else str(v) for v in self.excludes_path]

        self._normalize_inlined_as_list(slot_name="declares_element", slot_type=ModelElement, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PythonPackage(NamedElement):
    """
    A logical Python package (directory) inside the repository.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["PythonPackage"]
    class_class_curie: ClassVar[str] = "mellea:PythonPackage"
    class_name: ClassVar[str] = "PythonPackage"
    class_model_uri: ClassVar[URIRef] = MELLEA.PythonPackage

    id: Union[str, PythonPackageId] = None
    name: str = None
    package_name: Optional[str] = None
    depends_on_package: Optional[Union[dict[Union[str, PythonPackageId], Union[dict, "PythonPackage"]], list[Union[dict, "PythonPackage"]]]] = empty_dict()
    declares_element: Optional[Union[dict[Union[str, ModelElementId], Union[dict, "ModelElement"]], list[Union[dict, "ModelElement"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PythonPackageId):
            self.id = PythonPackageId(self.id)

        if self.package_name is not None and not isinstance(self.package_name, str):
            self.package_name = str(self.package_name)

        self._normalize_inlined_as_list(slot_name="depends_on_package", slot_type=PythonPackage, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="declares_element", slot_type=ModelElement, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelElement(NamedElement):
    """
    Abstract base for concrete architectural elements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["ModelElement"]
    class_class_curie: ClassVar[str] = "mellea:ModelElement"
    class_name: ClassVar[str] = "ModelElement"
    class_model_uri: ClassVar[URIRef] = MELLEA.ModelElement

    id: Union[str, ModelElementId] = None
    name: str = None

@dataclass(repr=False)
class BackendSpec(ModelElement):
    """
    Specification of a Mellea backend implementation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["BackendSpec"]
    class_class_curie: ClassVar[str] = "mellea:BackendSpec"
    class_name: ClassVar[str] = "BackendSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.BackendSpec

    id: Union[str, BackendSpecId] = None
    name: str = None
    backend_family: Optional[Union[str, "BackendFamilyEnum"]] = None
    model_identifier: Optional[Union[dict[Union[str, ModelIdentifierSpecId], Union[dict, "ModelIdentifierSpec"]], list[Union[dict, "ModelIdentifierSpec"]]]] = empty_dict()
    default_formatter: Optional[Union[str, FormatterSpecId]] = None
    model_options_key: Optional[Union[str, list[str]]] = empty_list()
    supports_streaming: Optional[Union[bool, Bool]] = None
    supports_tool_calls: Optional[Union[bool, Bool]] = None
    supports_multimodal: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BackendSpecId):
            self.id = BackendSpecId(self.id)

        if self.backend_family is not None and not isinstance(self.backend_family, BackendFamilyEnum):
            self.backend_family = BackendFamilyEnum(self.backend_family)

        self._normalize_inlined_as_list(slot_name="model_identifier", slot_type=ModelIdentifierSpec, key_name="id", keyed=True)

        if self.default_formatter is not None and not isinstance(self.default_formatter, FormatterSpecId):
            self.default_formatter = FormatterSpecId(self.default_formatter)

        if not isinstance(self.model_options_key, list):
            self.model_options_key = [self.model_options_key] if self.model_options_key is not None else []
        self.model_options_key = [v if isinstance(v, str) else str(v) for v in self.model_options_key]

        if self.supports_streaming is not None and not isinstance(self.supports_streaming, Bool):
            self.supports_streaming = Bool(self.supports_streaming)

        if self.supports_tool_calls is not None and not isinstance(self.supports_tool_calls, Bool):
            self.supports_tool_calls = Bool(self.supports_tool_calls)

        if self.supports_multimodal is not None and not isinstance(self.supports_multimodal, Bool):
            self.supports_multimodal = Bool(self.supports_multimodal)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FormatterSpec(ModelElement):
    """
    Specification of an output formatter for a backend.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["FormatterSpec"]
    class_class_curie: ClassVar[str] = "mellea:FormatterSpec"
    class_name: ClassVar[str] = "FormatterSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.FormatterSpec

    id: Union[str, FormatterSpecId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FormatterSpecId):
            self.id = FormatterSpecId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContextSpec(ModelElement):
    """
    Specification of a context implementation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["ContextSpec"]
    class_class_curie: ClassVar[str] = "mellea:ContextSpec"
    class_name: ClassVar[str] = "ContextSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.ContextSpec

    id: Union[str, ContextSpecId] = None
    name: str = None
    context_linearity: Optional[Union[str, "ContextLinearityEnum"]] = None
    stores_component_history: Optional[Union[bool, Bool]] = None
    accepts_message_attachments: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContextSpecId):
            self.id = ContextSpecId(self.id)

        if self.context_linearity is not None and not isinstance(self.context_linearity, ContextLinearityEnum):
            self.context_linearity = ContextLinearityEnum(self.context_linearity)

        if self.stores_component_history is not None and not isinstance(self.stores_component_history, Bool):
            self.stores_component_history = Bool(self.stores_component_history)

        if self.accepts_message_attachments is not None and not isinstance(self.accepts_message_attachments, Bool):
            self.accepts_message_attachments = Bool(self.accepts_message_attachments)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SessionSpec(ModelElement):
    """
    Specification of a Mellea session.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["SessionSpec"]
    class_class_curie: ClassVar[str] = "mellea:SessionSpec"
    class_name: ClassVar[str] = "SessionSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.SessionSpec

    id: Union[str, SessionSpecId] = None
    name: str = None
    uses_backend: Optional[Union[str, BackendSpecId]] = None
    uses_context: Optional[Union[str, ContextSpecId]] = None
    exposed_method: Optional[Union[dict[Union[str, MethodSpecId], Union[dict, "MethodSpec"]], list[Union[dict, "MethodSpec"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SessionSpecId):
            self.id = SessionSpecId(self.id)

        if self.uses_backend is not None and not isinstance(self.uses_backend, BackendSpecId):
            self.uses_backend = BackendSpecId(self.uses_backend)

        if self.uses_context is not None and not isinstance(self.uses_context, ContextSpecId):
            self.uses_context = ContextSpecId(self.uses_context)

        self._normalize_inlined_as_list(slot_name="exposed_method", slot_type=MethodSpec, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComponentSpec(ModelElement):
    """
    Specification of a Mellea stdlib component type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["ComponentSpec"]
    class_class_curie: ClassVar[str] = "mellea:ComponentSpec"
    class_name: ClassVar[str] = "ComponentSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.ComponentSpec

    id: Union[str, ComponentSpecId] = None
    name: str = None
    component_category: Optional[Union[str, "ComponentCategoryEnum"]] = None
    input_modality: Optional[Union[str, list[str]]] = empty_list()
    parsed_output_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentSpecId):
            self.id = ComponentSpecId(self.id)

        if self.component_category is not None and not isinstance(self.component_category, ComponentCategoryEnum):
            self.component_category = ComponentCategoryEnum(self.component_category)

        if not isinstance(self.input_modality, list):
            self.input_modality = [self.input_modality] if self.input_modality is not None else []
        self.input_modality = [v if isinstance(v, str) else str(v) for v in self.input_modality]

        if self.parsed_output_type is not None and not isinstance(self.parsed_output_type, str):
            self.parsed_output_type = str(self.parsed_output_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequirementSpec(ModelElement):
    """
    Specification of a requirement validator.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["RequirementSpec"]
    class_class_curie: ClassVar[str] = "mellea:RequirementSpec"
    class_name: ClassVar[str] = "RequirementSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.RequirementSpec

    id: Union[str, RequirementSpecId] = None
    name: str = None
    validation_style: Optional[str] = None
    may_trigger_repair: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequirementSpecId):
            self.id = RequirementSpecId(self.id)

        if self.validation_style is not None and not isinstance(self.validation_style, str):
            self.validation_style = str(self.validation_style)

        if self.may_trigger_repair is not None and not isinstance(self.may_trigger_repair, Bool):
            self.may_trigger_repair = Bool(self.may_trigger_repair)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SamplingStrategySpec(ModelElement):
    """
    Specification of a sampling-loop strategy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["SamplingStrategySpec"]
    class_class_curie: ClassVar[str] = "mellea:SamplingStrategySpec"
    class_name: ClassVar[str] = "SamplingStrategySpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.SamplingStrategySpec

    id: Union[str, SamplingStrategySpecId] = None
    name: str = None
    selection_policy: Optional[str] = None
    loop_budget_hint: Optional[int] = None
    may_trigger_repair: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SamplingStrategySpecId):
            self.id = SamplingStrategySpecId(self.id)

        if self.selection_policy is not None and not isinstance(self.selection_policy, str):
            self.selection_policy = str(self.selection_policy)

        if self.loop_budget_hint is not None and not isinstance(self.loop_budget_hint, int):
            self.loop_budget_hint = int(self.loop_budget_hint)

        if self.may_trigger_repair is not None and not isinstance(self.may_trigger_repair, Bool):
            self.may_trigger_repair = Bool(self.may_trigger_repair)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PluginSpec(ModelElement):
    """
    Specification of a Mellea plugin and the hooks it registers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["PluginSpec"]
    class_class_curie: ClassVar[str] = "mellea:PluginSpec"
    class_name: ClassVar[str] = "PluginSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.PluginSpec

    id: Union[str, PluginSpecId] = None
    name: str = None
    plugin_mode: Optional[Union[str, "PluginModeEnum"]] = None
    hook_type: Optional[Union[Union[str, "HookTypeEnum"], list[Union[str, "HookTypeEnum"]]]] = empty_list()
    payload_model: Optional[Union[dict[Union[str, HookPayloadSpecId], Union[dict, "HookPayloadSpec"]], list[Union[dict, "HookPayloadSpec"]]]] = empty_dict()
    plugin_priority: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PluginSpecId):
            self.id = PluginSpecId(self.id)

        if self.plugin_mode is not None and not isinstance(self.plugin_mode, PluginModeEnum):
            self.plugin_mode = PluginModeEnum(self.plugin_mode)

        if not isinstance(self.hook_type, list):
            self.hook_type = [self.hook_type] if self.hook_type is not None else []
        self.hook_type = [v if isinstance(v, HookTypeEnum) else HookTypeEnum(v) for v in self.hook_type]

        self._normalize_inlined_as_list(slot_name="payload_model", slot_type=HookPayloadSpec, key_name="id", keyed=True)

        if self.plugin_priority is not None and not isinstance(self.plugin_priority, int):
            self.plugin_priority = int(self.plugin_priority)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HookPayloadSpec(ModelElement):
    """
    Specification of a hook payload model.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["HookPayloadSpec"]
    class_class_curie: ClassVar[str] = "mellea:HookPayloadSpec"
    class_name: ClassVar[str] = "HookPayloadSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.HookPayloadSpec

    id: Union[str, HookPayloadSpecId] = None
    name: str = None
    hook_type: Optional[Union[Union[str, "HookTypeEnum"], list[Union[str, "HookTypeEnum"]]]] = empty_list()
    lifecycle_role: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HookPayloadSpecId):
            self.id = HookPayloadSpecId(self.id)

        if not isinstance(self.hook_type, list):
            self.hook_type = [self.hook_type] if self.hook_type is not None else []
        self.hook_type = [v if isinstance(v, HookTypeEnum) else HookTypeEnum(v) for v in self.hook_type]

        if self.lifecycle_role is not None and not isinstance(self.lifecycle_role, str):
            self.lifecycle_role = str(self.lifecycle_role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TelemetryMetricSpec(ModelElement):
    """
    Specification of a telemetry metric emitted by Mellea.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["TelemetryMetricSpec"]
    class_class_curie: ClassVar[str] = "mellea:TelemetryMetricSpec"
    class_name: ClassVar[str] = "TelemetryMetricSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.TelemetryMetricSpec

    id: Union[str, TelemetryMetricSpecId] = None
    name: str = None
    metric_name: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TelemetryMetricSpecId):
            self.id = TelemetryMetricSpecId(self.id)

        if not isinstance(self.metric_name, list):
            self.metric_name = [self.metric_name] if self.metric_name is not None else []
        self.metric_name = [v if isinstance(v, str) else str(v) for v in self.metric_name]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CliCommandSpec(ModelElement):
    """
    Specification of a CLI command exposed under `m`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["CliCommandSpec"]
    class_class_curie: ClassVar[str] = "mellea:CliCommandSpec"
    class_name: ClassVar[str] = "CliCommandSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.CliCommandSpec

    id: Union[str, CliCommandSpecId] = None
    name: str = None
    command_group: Optional[str] = None
    command_path: Optional[str] = None
    command_purpose: Optional[str] = None
    input_model: Optional[Union[dict[Union[str, ApiModelSpecId], Union[dict, "ApiModelSpec"]], list[Union[dict, "ApiModelSpec"]]]] = empty_dict()
    output_model: Optional[Union[dict[Union[str, ApiModelSpecId], Union[dict, "ApiModelSpec"]], list[Union[dict, "ApiModelSpec"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CliCommandSpecId):
            self.id = CliCommandSpecId(self.id)

        if self.command_group is not None and not isinstance(self.command_group, str):
            self.command_group = str(self.command_group)

        if self.command_path is not None and not isinstance(self.command_path, str):
            self.command_path = str(self.command_path)

        if self.command_purpose is not None and not isinstance(self.command_purpose, str):
            self.command_purpose = str(self.command_purpose)

        self._normalize_inlined_as_list(slot_name="input_model", slot_type=ApiModelSpec, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="output_model", slot_type=ApiModelSpec, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ApiModelSpec(ModelElement):
    """
    Specification of an HTTP API wire model.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["ApiModelSpec"]
    class_class_curie: ClassVar[str] = "mellea:ApiModelSpec"
    class_name: ClassVar[str] = "ApiModelSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.ApiModelSpec

    id: Union[str, ApiModelSpecId] = None
    name: str = None
    request_or_response: Optional[Union[str, "RequestResponseEnum"]] = None
    openai_object_type: Optional[str] = None
    has_field: Optional[Union[dict[Union[str, ApiFieldSpecId], Union[dict, "ApiFieldSpec"]], list[Union[dict, "ApiFieldSpec"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ApiModelSpecId):
            self.id = ApiModelSpecId(self.id)

        if self.request_or_response is not None and not isinstance(self.request_or_response, RequestResponseEnum):
            self.request_or_response = RequestResponseEnum(self.request_or_response)

        if self.openai_object_type is not None and not isinstance(self.openai_object_type, str):
            self.openai_object_type = str(self.openai_object_type)

        self._normalize_inlined_as_list(slot_name="has_field", slot_type=ApiFieldSpec, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ApiFieldSpec(NamedElement):
    """
    Specification of a single field in an API model.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["ApiFieldSpec"]
    class_class_curie: ClassVar[str] = "mellea:ApiFieldSpec"
    class_name: ClassVar[str] = "ApiFieldSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.ApiFieldSpec

    id: Union[str, ApiFieldSpecId] = None
    name: str = None
    field_name: Optional[str] = None
    field_type: Optional[str] = None
    required_field: Optional[Union[bool, Bool]] = None
    allows_null: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ApiFieldSpecId):
            self.id = ApiFieldSpecId(self.id)

        if self.field_name is not None and not isinstance(self.field_name, str):
            self.field_name = str(self.field_name)

        if self.field_type is not None and not isinstance(self.field_type, str):
            self.field_type = str(self.field_type)

        if self.required_field is not None and not isinstance(self.required_field, Bool):
            self.required_field = Bool(self.required_field)

        if self.allows_null is not None and not isinstance(self.allows_null, Bool):
            self.allows_null = Bool(self.allows_null)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MethodSpec(NamedElement):
    """
    Specification of a method exposed by a runtime class.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["MethodSpec"]
    class_class_curie: ClassVar[str] = "mellea:MethodSpec"
    class_name: ClassVar[str] = "MethodSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.MethodSpec

    id: Union[str, MethodSpecId] = None
    name: str = None
    method_name: Optional[str] = None
    method_signature: Optional[str] = None
    lifecycle_role: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MethodSpecId):
            self.id = MethodSpecId(self.id)

        if self.method_name is not None and not isinstance(self.method_name, str):
            self.method_name = str(self.method_name)

        if self.method_signature is not None and not isinstance(self.method_signature, str):
            self.method_signature = str(self.method_signature)

        if self.lifecycle_role is not None and not isinstance(self.lifecycle_role, str):
            self.lifecycle_role = str(self.lifecycle_role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelIdentifierSpec(NamedElement):
    """
    Cross-provider identifier table for a single model.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["ModelIdentifierSpec"]
    class_class_curie: ClassVar[str] = "mellea:ModelIdentifierSpec"
    class_name: ClassVar[str] = "ModelIdentifierSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.ModelIdentifierSpec

    id: Union[str, ModelIdentifierSpecId] = None
    name: str = None
    hf_model_name: Optional[str] = None
    ollama_name: Optional[str] = None
    watsonx_name: Optional[str] = None
    openai_name: Optional[str] = None
    bedrock_name: Optional[str] = None
    provider_name: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelIdentifierSpecId):
            self.id = ModelIdentifierSpecId(self.id)

        if self.hf_model_name is not None and not isinstance(self.hf_model_name, str):
            self.hf_model_name = str(self.hf_model_name)

        if self.ollama_name is not None and not isinstance(self.ollama_name, str):
            self.ollama_name = str(self.ollama_name)

        if self.watsonx_name is not None and not isinstance(self.watsonx_name, str):
            self.watsonx_name = str(self.watsonx_name)

        if self.openai_name is not None and not isinstance(self.openai_name, str):
            self.openai_name = str(self.openai_name)

        if self.bedrock_name is not None and not isinstance(self.bedrock_name, str):
            self.bedrock_name = str(self.bedrock_name)

        if not isinstance(self.provider_name, list):
            self.provider_name = [self.provider_name] if self.provider_name is not None else []
        self.provider_name = [v if isinstance(v, str) else str(v) for v in self.provider_name]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntrinsicAdapterSpec(NamedElement):
    """
    Specification of an intrinsic adapter (LoRA / aLoRA).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MELLEA["IntrinsicAdapterSpec"]
    class_class_curie: ClassVar[str] = "mellea:IntrinsicAdapterSpec"
    class_name: ClassVar[str] = "IntrinsicAdapterSpec"
    class_model_uri: ClassVar[URIRef] = MELLEA.IntrinsicAdapterSpec

    id: Union[str, IntrinsicAdapterSpecId] = None
    name: str = None
    repo_id: Optional[str] = None
    adapter_type: Optional[Union[Union[str, "AdapterTypeEnum"], list[Union[str, "AdapterTypeEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntrinsicAdapterSpecId):
            self.id = IntrinsicAdapterSpecId(self.id)

        if self.repo_id is not None and not isinstance(self.repo_id, str):
            self.repo_id = str(self.repo_id)

        if not isinstance(self.adapter_type, list):
            self.adapter_type = [self.adapter_type] if self.adapter_type is not None else []
        self.adapter_type = [v if isinstance(v, AdapterTypeEnum) else AdapterTypeEnum(v) for v in self.adapter_type]

        super().__post_init__(**kwargs)


# Enumerations
class PackageKindEnum(EnumDefinitionImpl):
    """
    Logical package buckets used to classify Mellea source modules.
    """
    CORE = PermissibleValue(
        text="CORE",
        description="core")
    STDLIB = PermissibleValue(
        text="STDLIB",
        description="stdlib")
    BACKENDS = PermissibleValue(
        text="BACKENDS",
        description="backends")
    FORMATTERS = PermissibleValue(
        text="FORMATTERS",
        description="formatters")
    HELPERS = PermissibleValue(
        text="HELPERS",
        description="helpers")
    PLUGINS = PermissibleValue(
        text="PLUGINS",
        description="plugins")
    TELEMETRY = PermissibleValue(
        text="TELEMETRY",
        description="telemetry")
    CLI = PermissibleValue(
        text="CLI",
        description="cli")
    DOCS_EXAMPLES = PermissibleValue(
        text="DOCS_EXAMPLES",
        description="docs examples")
    TEST = PermissibleValue(
        text="TEST",
        description="test")

    _defn = EnumDefinition(
        name="PackageKindEnum",
        description="Logical package buckets used to classify Mellea source modules.",
    )

class ElementKindEnum(EnumDefinitionImpl):
    """
    Kind of Python declaration captured by a ModelElement entry.
    """
    CLASS = PermissibleValue(
        text="CLASS",
        description="class")
    ENUM = PermissibleValue(
        text="ENUM",
        description="enum")
    DATACLASS = PermissibleValue(
        text="DATACLASS",
        description="dataclass")
    TYPED_DICT = PermissibleValue(
        text="TYPED_DICT",
        description="typed dict")
    PYDANTIC_MODEL = PermissibleValue(
        text="PYDANTIC_MODEL",
        description="pydantic model")
    PROTOCOL = PermissibleValue(
        text="PROTOCOL",
        description="protocol")
    FUNCTION = PermissibleValue(
        text="FUNCTION",
        description="function")
    MIXIN = PermissibleValue(
        text="MIXIN",
        description="mixin")

    _defn = EnumDefinition(
        name="ElementKindEnum",
        description="Kind of Python declaration captured by a ModelElement entry.",
    )

class CoverageScopeEnum(EnumDefinitionImpl):
    """
    Where in the project an element surfaces (source, API, CLI, ...).
    """
    SOURCE = PermissibleValue(
        text="SOURCE",
        description="source")
    API = PermissibleValue(
        text="API",
        description="api")
    CLI = PermissibleValue(
        text="CLI",
        description="cli")
    EXAMPLE = PermissibleValue(
        text="EXAMPLE",
        description="example")
    TEST = PermissibleValue(
        text="TEST",
        description="test")

    _defn = EnumDefinition(
        name="CoverageScopeEnum",
        description="Where in the project an element surfaces (source, API, CLI, ...).",
    )

class ContextLinearityEnum(EnumDefinitionImpl):
    """
    Whether a Mellea context preserves linear ordering or not.
    """
    LINEAR = PermissibleValue(
        text="LINEAR",
        description="Sequential, ordered history.")
    NON_LINEAR = PermissibleValue(
        text="NON_LINEAR",
        description="Tree- or graph-shaped history.")

    _defn = EnumDefinition(
        name="ContextLinearityEnum",
        description="Whether a Mellea context preserves linear ordering or not.",
    )

class ComponentCategoryEnum(EnumDefinitionImpl):
    """
    High-level category of a Mellea stdlib component.
    """
    INSTRUCTION = PermissibleValue(
        text="INSTRUCTION",
        description="instruction")
    MESSAGE = PermissibleValue(
        text="MESSAGE",
        description="message")
    TOOL_MESSAGE = PermissibleValue(
        text="TOOL_MESSAGE",
        description="tool message")
    DOCUMENT = PermissibleValue(
        text="DOCUMENT",
        description="document")
    INTRINSIC = PermissibleValue(
        text="INTRINSIC",
        description="intrinsic")
    MOBJECT = PermissibleValue(
        text="MOBJECT",
        description="mobject")
    QUERY = PermissibleValue(
        text="QUERY",
        description="query")
    TRANSFORM = PermissibleValue(
        text="TRANSFORM",
        description="transform")
    GENSTUB = PermissibleValue(
        text="GENSTUB",
        description="genstub")
    REQUIREMENT = PermissibleValue(
        text="REQUIREMENT",
        description="requirement")
    STREAM_EVENT = PermissibleValue(
        text="STREAM_EVENT",
        description="stream event")

    _defn = EnumDefinition(
        name="ComponentCategoryEnum",
        description="High-level category of a Mellea stdlib component.",
    )

class RequestResponseEnum(EnumDefinitionImpl):
    """
    Direction of a wire model (HTTP request, response, or both).
    """
    REQUEST = PermissibleValue(
        text="REQUEST",
        description="Inbound request payload.")
    RESPONSE = PermissibleValue(
        text="RESPONSE",
        description="Outbound response payload.")
    BOTH = PermissibleValue(
        text="BOTH",
        description="Model used in both directions (rare).")

    _defn = EnumDefinition(
        name="RequestResponseEnum",
        description="Direction of a wire model (HTTP request, response, or both).",
    )

class BackendFamilyEnum(EnumDefinitionImpl):
    """
    Backend families discovered under mellea/backends/.
    """
    BEDROCK = PermissibleValue(
        text="BEDROCK",
        description="Backend family backed by mellea/backends/bedrock.py.")
    DUMMY = PermissibleValue(
        text="DUMMY",
        description="Backend family backed by mellea/backends/dummy.py.")
    HUGGINGFACE = PermissibleValue(
        text="HUGGINGFACE",
        description="Backend family backed by mellea/backends/huggingface.py.")
    LITELLM = PermissibleValue(
        text="LITELLM",
        description="Backend family backed by mellea/backends/litellm.py.")
    OLLAMA = PermissibleValue(
        text="OLLAMA",
        description="Backend family backed by mellea/backends/ollama.py.")
    OPENAI = PermissibleValue(
        text="OPENAI",
        description="Backend family backed by mellea/backends/openai.py.")
    WATSONX = PermissibleValue(
        text="WATSONX",
        description="Backend family backed by mellea/backends/watsonx.py.")

    _defn = EnumDefinition(
        name="BackendFamilyEnum",
        description="Backend families discovered under mellea/backends/.",
    )

class PluginModeEnum(EnumDefinitionImpl):
    """
    Execution mode of a Mellea plugin (derived from PluginMode).
    """
    SEQUENTIAL = PermissibleValue(
        text="SEQUENTIAL",
        description="sequential")
    TRANSFORM = PermissibleValue(
        text="TRANSFORM",
        description="transform")
    CONCURRENT = PermissibleValue(
        text="CONCURRENT",
        description="concurrent")
    AUDIT = PermissibleValue(
        text="AUDIT",
        description="audit")
    FIRE_AND_FORGET = PermissibleValue(
        text="FIRE_AND_FORGET",
        description="fire and forget")

    _defn = EnumDefinition(
        name="PluginModeEnum",
        description="Execution mode of a Mellea plugin (derived from PluginMode).",
    )

class HookTypeEnum(EnumDefinitionImpl):
    """
    Lifecycle hook stages (derived from HookType).
    """
    SESSION_PRE_INIT = PermissibleValue(
        text="SESSION_PRE_INIT",
        description="session pre init")
    SESSION_POST_INIT = PermissibleValue(
        text="SESSION_POST_INIT",
        description="session post init")
    SESSION_RESET = PermissibleValue(
        text="SESSION_RESET",
        description="session reset")
    SESSION_CLEANUP = PermissibleValue(
        text="SESSION_CLEANUP",
        description="session cleanup")
    COMPONENT_PRE_EXECUTE = PermissibleValue(
        text="COMPONENT_PRE_EXECUTE",
        description="component pre execute")
    COMPONENT_POST_SUCCESS = PermissibleValue(
        text="COMPONENT_POST_SUCCESS",
        description="component post success")
    COMPONENT_POST_ERROR = PermissibleValue(
        text="COMPONENT_POST_ERROR",
        description="component post error")
    GENERATION_PRE_CALL = PermissibleValue(
        text="GENERATION_PRE_CALL",
        description="generation pre call")
    GENERATION_POST_CALL = PermissibleValue(
        text="GENERATION_POST_CALL",
        description="generation post call")
    GENERATION_ERROR = PermissibleValue(
        text="GENERATION_ERROR",
        description="generation error")
    VALIDATION_PRE_CHECK = PermissibleValue(
        text="VALIDATION_PRE_CHECK",
        description="validation pre check")
    VALIDATION_POST_CHECK = PermissibleValue(
        text="VALIDATION_POST_CHECK",
        description="validation post check")
    SAMPLING_LOOP_START = PermissibleValue(
        text="SAMPLING_LOOP_START",
        description="sampling loop start")
    SAMPLING_ITERATION = PermissibleValue(
        text="SAMPLING_ITERATION",
        description="sampling iteration")
    SAMPLING_REPAIR = PermissibleValue(
        text="SAMPLING_REPAIR",
        description="sampling repair")
    SAMPLING_LOOP_END = PermissibleValue(
        text="SAMPLING_LOOP_END",
        description="sampling loop end")
    TOOL_PRE_INVOKE = PermissibleValue(
        text="TOOL_PRE_INVOKE",
        description="tool pre invoke")
    TOOL_POST_INVOKE = PermissibleValue(
        text="TOOL_POST_INVOKE",
        description="tool post invoke")

    _defn = EnumDefinition(
        name="HookTypeEnum",
        description="Lifecycle hook stages (derived from HookType).",
    )

class AdapterTypeEnum(EnumDefinitionImpl):
    """
    Adapter implementation type (derived from AdapterType).
    """
    LORA = PermissibleValue(
        text="LORA",
        description="lora")
    ALORA = PermissibleValue(
        text="ALORA",
        description="alora")

    _defn = EnumDefinition(
        name="AdapterTypeEnum",
        description="Adapter implementation type (derived from AdapterType).",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MELLEA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MELLEA.name, domain=None, range=str)

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MELLEA.description, domain=None, range=Optional[str])

slots.module_path = Slot(uri=MELLEA.module_path, name="module_path", curie=MELLEA.curie('module_path'),
                   model_uri=MELLEA.module_path, domain=None, range=Optional[str])

slots.source_file = Slot(uri=MELLEA.source_file, name="source_file", curie=MELLEA.curie('source_file'),
                   model_uri=MELLEA.source_file, domain=None, range=Optional[str])

slots.package_kind = Slot(uri=MELLEA.package_kind, name="package_kind", curie=MELLEA.curie('package_kind'),
                   model_uri=MELLEA.package_kind, domain=None, range=Optional[Union[str, "PackageKindEnum"]])

slots.element_kind = Slot(uri=MELLEA.element_kind, name="element_kind", curie=MELLEA.curie('element_kind'),
                   model_uri=MELLEA.element_kind, domain=None, range=Optional[Union[str, "ElementKindEnum"]])

slots.coverage_scope = Slot(uri=MELLEA.coverage_scope, name="coverage_scope", curie=MELLEA.curie('coverage_scope'),
                   model_uri=MELLEA.coverage_scope, domain=None, range=Optional[Union[Union[str, "CoverageScopeEnum"], list[Union[str, "CoverageScopeEnum"]]]])

slots.tags = Slot(uri=MELLEA.tags, name="tags", curie=MELLEA.curie('tags'),
                   model_uri=MELLEA.tags, domain=None, range=Optional[Union[str, list[str]]])

slots.repository_root = Slot(uri=MELLEA.repository_root, name="repository_root", curie=MELLEA.curie('repository_root'),
                   model_uri=MELLEA.repository_root, domain=None, range=Optional[str])

slots.analyzed_on = Slot(uri=MELLEA.analyzed_on, name="analyzed_on", curie=MELLEA.curie('analyzed_on'),
                   model_uri=MELLEA.analyzed_on, domain=None, range=Optional[Union[str, XSDDate]])

slots.includes_path = Slot(uri=MELLEA.includes_path, name="includes_path", curie=MELLEA.curie('includes_path'),
                   model_uri=MELLEA.includes_path, domain=None, range=Optional[Union[str, list[str]]])

slots.excludes_path = Slot(uri=MELLEA.excludes_path, name="excludes_path", curie=MELLEA.curie('excludes_path'),
                   model_uri=MELLEA.excludes_path, domain=None, range=Optional[Union[str, list[str]]])

slots.package_name = Slot(uri=MELLEA.package_name, name="package_name", curie=MELLEA.curie('package_name'),
                   model_uri=MELLEA.package_name, domain=None, range=Optional[str])

slots.depends_on_package = Slot(uri=MELLEA.depends_on_package, name="depends_on_package", curie=MELLEA.curie('depends_on_package'),
                   model_uri=MELLEA.depends_on_package, domain=None, range=Optional[Union[dict[Union[str, PythonPackageId], Union[dict, PythonPackage]], list[Union[dict, PythonPackage]]]])

slots.declares_element = Slot(uri=MELLEA.declares_element, name="declares_element", curie=MELLEA.curie('declares_element'),
                   model_uri=MELLEA.declares_element, domain=None, range=Optional[Union[dict[Union[str, ModelElementId], Union[dict, ModelElement]], list[Union[dict, ModelElement]]]])

slots.backend_family = Slot(uri=MELLEA.backend_family, name="backend_family", curie=MELLEA.curie('backend_family'),
                   model_uri=MELLEA.backend_family, domain=None, range=Optional[Union[str, "BackendFamilyEnum"]])

slots.model_identifier = Slot(uri=MELLEA.model_identifier, name="model_identifier", curie=MELLEA.curie('model_identifier'),
                   model_uri=MELLEA.model_identifier, domain=None, range=Optional[Union[dict[Union[str, ModelIdentifierSpecId], Union[dict, ModelIdentifierSpec]], list[Union[dict, ModelIdentifierSpec]]]])

slots.default_formatter = Slot(uri=MELLEA.default_formatter, name="default_formatter", curie=MELLEA.curie('default_formatter'),
                   model_uri=MELLEA.default_formatter, domain=None, range=Optional[Union[str, FormatterSpecId]])

slots.model_options_key = Slot(uri=MELLEA.model_options_key, name="model_options_key", curie=MELLEA.curie('model_options_key'),
                   model_uri=MELLEA.model_options_key, domain=None, range=Optional[Union[str, list[str]]])

slots.supports_streaming = Slot(uri=MELLEA.supports_streaming, name="supports_streaming", curie=MELLEA.curie('supports_streaming'),
                   model_uri=MELLEA.supports_streaming, domain=None, range=Optional[Union[bool, Bool]])

slots.supports_tool_calls = Slot(uri=MELLEA.supports_tool_calls, name="supports_tool_calls", curie=MELLEA.curie('supports_tool_calls'),
                   model_uri=MELLEA.supports_tool_calls, domain=None, range=Optional[Union[bool, Bool]])

slots.supports_multimodal = Slot(uri=MELLEA.supports_multimodal, name="supports_multimodal", curie=MELLEA.curie('supports_multimodal'),
                   model_uri=MELLEA.supports_multimodal, domain=None, range=Optional[Union[bool, Bool]])

slots.context_linearity = Slot(uri=MELLEA.context_linearity, name="context_linearity", curie=MELLEA.curie('context_linearity'),
                   model_uri=MELLEA.context_linearity, domain=None, range=Optional[Union[str, "ContextLinearityEnum"]])

slots.stores_component_history = Slot(uri=MELLEA.stores_component_history, name="stores_component_history", curie=MELLEA.curie('stores_component_history'),
                   model_uri=MELLEA.stores_component_history, domain=None, range=Optional[Union[bool, Bool]])

slots.accepts_message_attachments = Slot(uri=MELLEA.accepts_message_attachments, name="accepts_message_attachments", curie=MELLEA.curie('accepts_message_attachments'),
                   model_uri=MELLEA.accepts_message_attachments, domain=None, range=Optional[Union[bool, Bool]])

slots.uses_backend = Slot(uri=MELLEA.uses_backend, name="uses_backend", curie=MELLEA.curie('uses_backend'),
                   model_uri=MELLEA.uses_backend, domain=None, range=Optional[Union[str, BackendSpecId]])

slots.uses_context = Slot(uri=MELLEA.uses_context, name="uses_context", curie=MELLEA.curie('uses_context'),
                   model_uri=MELLEA.uses_context, domain=None, range=Optional[Union[str, ContextSpecId]])

slots.exposed_method = Slot(uri=MELLEA.exposed_method, name="exposed_method", curie=MELLEA.curie('exposed_method'),
                   model_uri=MELLEA.exposed_method, domain=None, range=Optional[Union[dict[Union[str, MethodSpecId], Union[dict, MethodSpec]], list[Union[dict, MethodSpec]]]])

slots.uses_component_type = Slot(uri=MELLEA.uses_component_type, name="uses_component_type", curie=MELLEA.curie('uses_component_type'),
                   model_uri=MELLEA.uses_component_type, domain=None, range=Optional[Union[dict[Union[str, ComponentSpecId], Union[dict, ComponentSpec]], list[Union[dict, ComponentSpec]]]])

slots.component_category = Slot(uri=MELLEA.component_category, name="component_category", curie=MELLEA.curie('component_category'),
                   model_uri=MELLEA.component_category, domain=None, range=Optional[Union[str, "ComponentCategoryEnum"]])

slots.input_modality = Slot(uri=MELLEA.input_modality, name="input_modality", curie=MELLEA.curie('input_modality'),
                   model_uri=MELLEA.input_modality, domain=None, range=Optional[Union[str, list[str]]])

slots.parsed_output_type = Slot(uri=MELLEA.parsed_output_type, name="parsed_output_type", curie=MELLEA.curie('parsed_output_type'),
                   model_uri=MELLEA.parsed_output_type, domain=None, range=Optional[str])

slots.validation_style = Slot(uri=MELLEA.validation_style, name="validation_style", curie=MELLEA.curie('validation_style'),
                   model_uri=MELLEA.validation_style, domain=None, range=Optional[str])

slots.may_trigger_repair = Slot(uri=MELLEA.may_trigger_repair, name="may_trigger_repair", curie=MELLEA.curie('may_trigger_repair'),
                   model_uri=MELLEA.may_trigger_repair, domain=None, range=Optional[Union[bool, Bool]])

slots.selection_policy = Slot(uri=MELLEA.selection_policy, name="selection_policy", curie=MELLEA.curie('selection_policy'),
                   model_uri=MELLEA.selection_policy, domain=None, range=Optional[str])

slots.loop_budget_hint = Slot(uri=MELLEA.loop_budget_hint, name="loop_budget_hint", curie=MELLEA.curie('loop_budget_hint'),
                   model_uri=MELLEA.loop_budget_hint, domain=None, range=Optional[int])

slots.plugin_mode = Slot(uri=MELLEA.plugin_mode, name="plugin_mode", curie=MELLEA.curie('plugin_mode'),
                   model_uri=MELLEA.plugin_mode, domain=None, range=Optional[Union[str, "PluginModeEnum"]])

slots.hook_type = Slot(uri=MELLEA.hook_type, name="hook_type", curie=MELLEA.curie('hook_type'),
                   model_uri=MELLEA.hook_type, domain=None, range=Optional[Union[Union[str, "HookTypeEnum"], list[Union[str, "HookTypeEnum"]]]])

slots.payload_model = Slot(uri=MELLEA.payload_model, name="payload_model", curie=MELLEA.curie('payload_model'),
                   model_uri=MELLEA.payload_model, domain=None, range=Optional[Union[dict[Union[str, HookPayloadSpecId], Union[dict, HookPayloadSpec]], list[Union[dict, HookPayloadSpec]]]])

slots.plugin_priority = Slot(uri=MELLEA.plugin_priority, name="plugin_priority", curie=MELLEA.curie('plugin_priority'),
                   model_uri=MELLEA.plugin_priority, domain=None, range=Optional[int])

slots.metric_name = Slot(uri=MELLEA.metric_name, name="metric_name", curie=MELLEA.curie('metric_name'),
                   model_uri=MELLEA.metric_name, domain=None, range=Optional[Union[str, list[str]]])

slots.command_group = Slot(uri=MELLEA.command_group, name="command_group", curie=MELLEA.curie('command_group'),
                   model_uri=MELLEA.command_group, domain=None, range=Optional[str])

slots.command_path = Slot(uri=MELLEA.command_path, name="command_path", curie=MELLEA.curie('command_path'),
                   model_uri=MELLEA.command_path, domain=None, range=Optional[str])

slots.command_purpose = Slot(uri=MELLEA.command_purpose, name="command_purpose", curie=MELLEA.curie('command_purpose'),
                   model_uri=MELLEA.command_purpose, domain=None, range=Optional[str])

slots.input_model = Slot(uri=MELLEA.input_model, name="input_model", curie=MELLEA.curie('input_model'),
                   model_uri=MELLEA.input_model, domain=None, range=Optional[Union[dict[Union[str, ApiModelSpecId], Union[dict, ApiModelSpec]], list[Union[dict, ApiModelSpec]]]])

slots.output_model = Slot(uri=MELLEA.output_model, name="output_model", curie=MELLEA.curie('output_model'),
                   model_uri=MELLEA.output_model, domain=None, range=Optional[Union[dict[Union[str, ApiModelSpecId], Union[dict, ApiModelSpec]], list[Union[dict, ApiModelSpec]]]])

slots.request_or_response = Slot(uri=MELLEA.request_or_response, name="request_or_response", curie=MELLEA.curie('request_or_response'),
                   model_uri=MELLEA.request_or_response, domain=None, range=Optional[Union[str, "RequestResponseEnum"]])

slots.openai_object_type = Slot(uri=MELLEA.openai_object_type, name="openai_object_type", curie=MELLEA.curie('openai_object_type'),
                   model_uri=MELLEA.openai_object_type, domain=None, range=Optional[str])

slots.has_field = Slot(uri=MELLEA.has_field, name="has_field", curie=MELLEA.curie('has_field'),
                   model_uri=MELLEA.has_field, domain=None, range=Optional[Union[dict[Union[str, ApiFieldSpecId], Union[dict, ApiFieldSpec]], list[Union[dict, ApiFieldSpec]]]])

slots.field_name = Slot(uri=MELLEA.field_name, name="field_name", curie=MELLEA.curie('field_name'),
                   model_uri=MELLEA.field_name, domain=None, range=Optional[str])

slots.field_type = Slot(uri=MELLEA.field_type, name="field_type", curie=MELLEA.curie('field_type'),
                   model_uri=MELLEA.field_type, domain=None, range=Optional[str])

slots.required_field = Slot(uri=MELLEA.required_field, name="required_field", curie=MELLEA.curie('required_field'),
                   model_uri=MELLEA.required_field, domain=None, range=Optional[Union[bool, Bool]])

slots.allows_null = Slot(uri=MELLEA.allows_null, name="allows_null", curie=MELLEA.curie('allows_null'),
                   model_uri=MELLEA.allows_null, domain=None, range=Optional[Union[bool, Bool]])

slots.method_name = Slot(uri=MELLEA.method_name, name="method_name", curie=MELLEA.curie('method_name'),
                   model_uri=MELLEA.method_name, domain=None, range=Optional[str])

slots.method_signature = Slot(uri=MELLEA.method_signature, name="method_signature", curie=MELLEA.curie('method_signature'),
                   model_uri=MELLEA.method_signature, domain=None, range=Optional[str])

slots.lifecycle_role = Slot(uri=MELLEA.lifecycle_role, name="lifecycle_role", curie=MELLEA.curie('lifecycle_role'),
                   model_uri=MELLEA.lifecycle_role, domain=None, range=Optional[str])

slots.adapter_type = Slot(uri=MELLEA.adapter_type, name="adapter_type", curie=MELLEA.curie('adapter_type'),
                   model_uri=MELLEA.adapter_type, domain=None, range=Optional[Union[Union[str, "AdapterTypeEnum"], list[Union[str, "AdapterTypeEnum"]]]])

slots.repo_id = Slot(uri=MELLEA.repo_id, name="repo_id", curie=MELLEA.curie('repo_id'),
                   model_uri=MELLEA.repo_id, domain=None, range=Optional[str])

slots.provider_name = Slot(uri=MELLEA.provider_name, name="provider_name", curie=MELLEA.curie('provider_name'),
                   model_uri=MELLEA.provider_name, domain=None, range=Optional[Union[str, list[str]]])

slots.hf_model_name = Slot(uri=MELLEA.hf_model_name, name="hf_model_name", curie=MELLEA.curie('hf_model_name'),
                   model_uri=MELLEA.hf_model_name, domain=None, range=Optional[str])

slots.ollama_name = Slot(uri=MELLEA.ollama_name, name="ollama_name", curie=MELLEA.curie('ollama_name'),
                   model_uri=MELLEA.ollama_name, domain=None, range=Optional[str])

slots.watsonx_name = Slot(uri=MELLEA.watsonx_name, name="watsonx_name", curie=MELLEA.curie('watsonx_name'),
                   model_uri=MELLEA.watsonx_name, domain=None, range=Optional[str])

slots.openai_name = Slot(uri=MELLEA.openai_name, name="openai_name", curie=MELLEA.curie('openai_name'),
                   model_uri=MELLEA.openai_name, domain=None, range=Optional[str])

slots.bedrock_name = Slot(uri=MELLEA.bedrock_name, name="bedrock_name", curie=MELLEA.curie('bedrock_name'),
                   model_uri=MELLEA.bedrock_name, domain=None, range=Optional[str])
