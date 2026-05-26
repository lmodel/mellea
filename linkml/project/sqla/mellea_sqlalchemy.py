
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class NamedElement(Base):
    """
    Abstract base for any named, identifiable schema element.
    """
    __tablename__ = 'NamedElement'

    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    
    
    coverage_scope_rel = relationship( "NamedElementCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: NamedElementCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "NamedElementTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: NamedElementTags(tags=x_))
    

    def __repr__(self):
        return f"NamedElement(id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},)"



    


class NamedElementCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'NamedElement_coverage_scope'

    NamedElement_id = Column(Text(), ForeignKey('NamedElement.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"NamedElement_coverage_scope(NamedElement_id={self.NamedElement_id},coverage_scope={self.coverage_scope},)"



    


class NamedElementTags(Base):
    """
    None
    """
    __tablename__ = 'NamedElement_tags'

    NamedElement_id = Column(Text(), ForeignKey('NamedElement.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"NamedElement_tags(NamedElement_id={self.NamedElement_id},tags={self.tags},)"



    


class RepositoryCatalogIncludesPath(Base):
    """
    None
    """
    __tablename__ = 'RepositoryCatalog_includes_path'

    RepositoryCatalog_id = Column(Text(), ForeignKey('RepositoryCatalog.id'), primary_key=True)
    includes_path = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"RepositoryCatalog_includes_path(RepositoryCatalog_id={self.RepositoryCatalog_id},includes_path={self.includes_path},)"



    


class RepositoryCatalogExcludesPath(Base):
    """
    None
    """
    __tablename__ = 'RepositoryCatalog_excludes_path'

    RepositoryCatalog_id = Column(Text(), ForeignKey('RepositoryCatalog.id'), primary_key=True)
    excludes_path = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"RepositoryCatalog_excludes_path(RepositoryCatalog_id={self.RepositoryCatalog_id},excludes_path={self.excludes_path},)"



    


class RepositoryCatalogCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'RepositoryCatalog_coverage_scope'

    RepositoryCatalog_id = Column(Text(), ForeignKey('RepositoryCatalog.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"RepositoryCatalog_coverage_scope(RepositoryCatalog_id={self.RepositoryCatalog_id},coverage_scope={self.coverage_scope},)"



    


class RepositoryCatalogTags(Base):
    """
    None
    """
    __tablename__ = 'RepositoryCatalog_tags'

    RepositoryCatalog_id = Column(Text(), ForeignKey('RepositoryCatalog.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"RepositoryCatalog_tags(RepositoryCatalog_id={self.RepositoryCatalog_id},tags={self.tags},)"



    


class PythonPackageCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'PythonPackage_coverage_scope'

    PythonPackage_id = Column(Text(), ForeignKey('PythonPackage.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"PythonPackage_coverage_scope(PythonPackage_id={self.PythonPackage_id},coverage_scope={self.coverage_scope},)"



    


class PythonPackageTags(Base):
    """
    None
    """
    __tablename__ = 'PythonPackage_tags'

    PythonPackage_id = Column(Text(), ForeignKey('PythonPackage.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"PythonPackage_tags(PythonPackage_id={self.PythonPackage_id},tags={self.tags},)"



    


class ModelElementCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'ModelElement_coverage_scope'

    ModelElement_id = Column(Text(), ForeignKey('ModelElement.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"ModelElement_coverage_scope(ModelElement_id={self.ModelElement_id},coverage_scope={self.coverage_scope},)"



    


class ModelElementTags(Base):
    """
    None
    """
    __tablename__ = 'ModelElement_tags'

    ModelElement_id = Column(Text(), ForeignKey('ModelElement.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ModelElement_tags(ModelElement_id={self.ModelElement_id},tags={self.tags},)"



    


class BackendSpecModelOptionsKey(Base):
    """
    None
    """
    __tablename__ = 'BackendSpec_model_options_key'

    BackendSpec_id = Column(Text(), ForeignKey('BackendSpec.id'), primary_key=True)
    model_options_key = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"BackendSpec_model_options_key(BackendSpec_id={self.BackendSpec_id},model_options_key={self.model_options_key},)"



    


class BackendSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'BackendSpec_coverage_scope'

    BackendSpec_id = Column(Text(), ForeignKey('BackendSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"BackendSpec_coverage_scope(BackendSpec_id={self.BackendSpec_id},coverage_scope={self.coverage_scope},)"



    


class BackendSpecTags(Base):
    """
    None
    """
    __tablename__ = 'BackendSpec_tags'

    BackendSpec_id = Column(Text(), ForeignKey('BackendSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"BackendSpec_tags(BackendSpec_id={self.BackendSpec_id},tags={self.tags},)"



    


class FormatterSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'FormatterSpec_coverage_scope'

    FormatterSpec_id = Column(Text(), ForeignKey('FormatterSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"FormatterSpec_coverage_scope(FormatterSpec_id={self.FormatterSpec_id},coverage_scope={self.coverage_scope},)"



    


class FormatterSpecTags(Base):
    """
    None
    """
    __tablename__ = 'FormatterSpec_tags'

    FormatterSpec_id = Column(Text(), ForeignKey('FormatterSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"FormatterSpec_tags(FormatterSpec_id={self.FormatterSpec_id},tags={self.tags},)"



    


class ContextSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'ContextSpec_coverage_scope'

    ContextSpec_id = Column(Text(), ForeignKey('ContextSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"ContextSpec_coverage_scope(ContextSpec_id={self.ContextSpec_id},coverage_scope={self.coverage_scope},)"



    


class ContextSpecTags(Base):
    """
    None
    """
    __tablename__ = 'ContextSpec_tags'

    ContextSpec_id = Column(Text(), ForeignKey('ContextSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ContextSpec_tags(ContextSpec_id={self.ContextSpec_id},tags={self.tags},)"



    


class SessionSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'SessionSpec_coverage_scope'

    SessionSpec_id = Column(Text(), ForeignKey('SessionSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"SessionSpec_coverage_scope(SessionSpec_id={self.SessionSpec_id},coverage_scope={self.coverage_scope},)"



    


class SessionSpecTags(Base):
    """
    None
    """
    __tablename__ = 'SessionSpec_tags'

    SessionSpec_id = Column(Text(), ForeignKey('SessionSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SessionSpec_tags(SessionSpec_id={self.SessionSpec_id},tags={self.tags},)"



    


class ComponentSpecInputModality(Base):
    """
    None
    """
    __tablename__ = 'ComponentSpec_input_modality'

    ComponentSpec_id = Column(Text(), ForeignKey('ComponentSpec.id'), primary_key=True)
    input_modality = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ComponentSpec_input_modality(ComponentSpec_id={self.ComponentSpec_id},input_modality={self.input_modality},)"



    


class ComponentSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'ComponentSpec_coverage_scope'

    ComponentSpec_id = Column(Text(), ForeignKey('ComponentSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"ComponentSpec_coverage_scope(ComponentSpec_id={self.ComponentSpec_id},coverage_scope={self.coverage_scope},)"



    


class ComponentSpecTags(Base):
    """
    None
    """
    __tablename__ = 'ComponentSpec_tags'

    ComponentSpec_id = Column(Text(), ForeignKey('ComponentSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ComponentSpec_tags(ComponentSpec_id={self.ComponentSpec_id},tags={self.tags},)"



    


class RequirementSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'RequirementSpec_coverage_scope'

    RequirementSpec_id = Column(Text(), ForeignKey('RequirementSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"RequirementSpec_coverage_scope(RequirementSpec_id={self.RequirementSpec_id},coverage_scope={self.coverage_scope},)"



    


class RequirementSpecTags(Base):
    """
    None
    """
    __tablename__ = 'RequirementSpec_tags'

    RequirementSpec_id = Column(Text(), ForeignKey('RequirementSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"RequirementSpec_tags(RequirementSpec_id={self.RequirementSpec_id},tags={self.tags},)"



    


class SamplingStrategySpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'SamplingStrategySpec_coverage_scope'

    SamplingStrategySpec_id = Column(Text(), ForeignKey('SamplingStrategySpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"SamplingStrategySpec_coverage_scope(SamplingStrategySpec_id={self.SamplingStrategySpec_id},coverage_scope={self.coverage_scope},)"



    


class SamplingStrategySpecTags(Base):
    """
    None
    """
    __tablename__ = 'SamplingStrategySpec_tags'

    SamplingStrategySpec_id = Column(Text(), ForeignKey('SamplingStrategySpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SamplingStrategySpec_tags(SamplingStrategySpec_id={self.SamplingStrategySpec_id},tags={self.tags},)"



    


class PluginSpecHookType(Base):
    """
    None
    """
    __tablename__ = 'PluginSpec_hook_type'

    PluginSpec_id = Column(Text(), ForeignKey('PluginSpec.id'), primary_key=True)
    hook_type = Column(Enum('SESSION_PRE_INIT', 'SESSION_POST_INIT', 'SESSION_RESET', 'SESSION_CLEANUP', 'COMPONENT_PRE_EXECUTE', 'COMPONENT_POST_SUCCESS', 'COMPONENT_POST_ERROR', 'GENERATION_PRE_CALL', 'GENERATION_POST_CALL', 'GENERATION_ERROR', 'VALIDATION_PRE_CHECK', 'VALIDATION_POST_CHECK', 'SAMPLING_LOOP_START', 'SAMPLING_ITERATION', 'SAMPLING_REPAIR', 'SAMPLING_LOOP_END', 'TOOL_PRE_INVOKE', 'TOOL_POST_INVOKE', name='HookTypeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"PluginSpec_hook_type(PluginSpec_id={self.PluginSpec_id},hook_type={self.hook_type},)"



    


class PluginSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'PluginSpec_coverage_scope'

    PluginSpec_id = Column(Text(), ForeignKey('PluginSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"PluginSpec_coverage_scope(PluginSpec_id={self.PluginSpec_id},coverage_scope={self.coverage_scope},)"



    


class PluginSpecTags(Base):
    """
    None
    """
    __tablename__ = 'PluginSpec_tags'

    PluginSpec_id = Column(Text(), ForeignKey('PluginSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"PluginSpec_tags(PluginSpec_id={self.PluginSpec_id},tags={self.tags},)"



    


class HookPayloadSpecHookType(Base):
    """
    None
    """
    __tablename__ = 'HookPayloadSpec_hook_type'

    HookPayloadSpec_id = Column(Text(), ForeignKey('HookPayloadSpec.id'), primary_key=True)
    hook_type = Column(Enum('SESSION_PRE_INIT', 'SESSION_POST_INIT', 'SESSION_RESET', 'SESSION_CLEANUP', 'COMPONENT_PRE_EXECUTE', 'COMPONENT_POST_SUCCESS', 'COMPONENT_POST_ERROR', 'GENERATION_PRE_CALL', 'GENERATION_POST_CALL', 'GENERATION_ERROR', 'VALIDATION_PRE_CHECK', 'VALIDATION_POST_CHECK', 'SAMPLING_LOOP_START', 'SAMPLING_ITERATION', 'SAMPLING_REPAIR', 'SAMPLING_LOOP_END', 'TOOL_PRE_INVOKE', 'TOOL_POST_INVOKE', name='HookTypeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"HookPayloadSpec_hook_type(HookPayloadSpec_id={self.HookPayloadSpec_id},hook_type={self.hook_type},)"



    


class HookPayloadSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'HookPayloadSpec_coverage_scope'

    HookPayloadSpec_id = Column(Text(), ForeignKey('HookPayloadSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"HookPayloadSpec_coverage_scope(HookPayloadSpec_id={self.HookPayloadSpec_id},coverage_scope={self.coverage_scope},)"



    


class HookPayloadSpecTags(Base):
    """
    None
    """
    __tablename__ = 'HookPayloadSpec_tags'

    HookPayloadSpec_id = Column(Text(), ForeignKey('HookPayloadSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"HookPayloadSpec_tags(HookPayloadSpec_id={self.HookPayloadSpec_id},tags={self.tags},)"



    


class TelemetryMetricSpecMetricName(Base):
    """
    None
    """
    __tablename__ = 'TelemetryMetricSpec_metric_name'

    TelemetryMetricSpec_id = Column(Text(), ForeignKey('TelemetryMetricSpec.id'), primary_key=True)
    metric_name = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"TelemetryMetricSpec_metric_name(TelemetryMetricSpec_id={self.TelemetryMetricSpec_id},metric_name={self.metric_name},)"



    


class TelemetryMetricSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'TelemetryMetricSpec_coverage_scope'

    TelemetryMetricSpec_id = Column(Text(), ForeignKey('TelemetryMetricSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"TelemetryMetricSpec_coverage_scope(TelemetryMetricSpec_id={self.TelemetryMetricSpec_id},coverage_scope={self.coverage_scope},)"



    


class TelemetryMetricSpecTags(Base):
    """
    None
    """
    __tablename__ = 'TelemetryMetricSpec_tags'

    TelemetryMetricSpec_id = Column(Text(), ForeignKey('TelemetryMetricSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"TelemetryMetricSpec_tags(TelemetryMetricSpec_id={self.TelemetryMetricSpec_id},tags={self.tags},)"



    


class CliCommandSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'CliCommandSpec_coverage_scope'

    CliCommandSpec_id = Column(Text(), ForeignKey('CliCommandSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"CliCommandSpec_coverage_scope(CliCommandSpec_id={self.CliCommandSpec_id},coverage_scope={self.coverage_scope},)"



    


class CliCommandSpecTags(Base):
    """
    None
    """
    __tablename__ = 'CliCommandSpec_tags'

    CliCommandSpec_id = Column(Text(), ForeignKey('CliCommandSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"CliCommandSpec_tags(CliCommandSpec_id={self.CliCommandSpec_id},tags={self.tags},)"



    


class ApiModelSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'ApiModelSpec_coverage_scope'

    ApiModelSpec_id = Column(Text(), ForeignKey('ApiModelSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"ApiModelSpec_coverage_scope(ApiModelSpec_id={self.ApiModelSpec_id},coverage_scope={self.coverage_scope},)"



    


class ApiModelSpecTags(Base):
    """
    None
    """
    __tablename__ = 'ApiModelSpec_tags'

    ApiModelSpec_id = Column(Text(), ForeignKey('ApiModelSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ApiModelSpec_tags(ApiModelSpec_id={self.ApiModelSpec_id},tags={self.tags},)"



    


class ApiFieldSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'ApiFieldSpec_coverage_scope'

    ApiFieldSpec_id = Column(Text(), ForeignKey('ApiFieldSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"ApiFieldSpec_coverage_scope(ApiFieldSpec_id={self.ApiFieldSpec_id},coverage_scope={self.coverage_scope},)"



    


class ApiFieldSpecTags(Base):
    """
    None
    """
    __tablename__ = 'ApiFieldSpec_tags'

    ApiFieldSpec_id = Column(Text(), ForeignKey('ApiFieldSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ApiFieldSpec_tags(ApiFieldSpec_id={self.ApiFieldSpec_id},tags={self.tags},)"



    


class MethodSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'MethodSpec_coverage_scope'

    MethodSpec_id = Column(Text(), ForeignKey('MethodSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"MethodSpec_coverage_scope(MethodSpec_id={self.MethodSpec_id},coverage_scope={self.coverage_scope},)"



    


class MethodSpecTags(Base):
    """
    None
    """
    __tablename__ = 'MethodSpec_tags'

    MethodSpec_id = Column(Text(), ForeignKey('MethodSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"MethodSpec_tags(MethodSpec_id={self.MethodSpec_id},tags={self.tags},)"



    


class ModelIdentifierSpecProviderName(Base):
    """
    None
    """
    __tablename__ = 'ModelIdentifierSpec_provider_name'

    ModelIdentifierSpec_id = Column(Text(), ForeignKey('ModelIdentifierSpec.id'), primary_key=True)
    provider_name = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ModelIdentifierSpec_provider_name(ModelIdentifierSpec_id={self.ModelIdentifierSpec_id},provider_name={self.provider_name},)"



    


class ModelIdentifierSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'ModelIdentifierSpec_coverage_scope'

    ModelIdentifierSpec_id = Column(Text(), ForeignKey('ModelIdentifierSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"ModelIdentifierSpec_coverage_scope(ModelIdentifierSpec_id={self.ModelIdentifierSpec_id},coverage_scope={self.coverage_scope},)"



    


class ModelIdentifierSpecTags(Base):
    """
    None
    """
    __tablename__ = 'ModelIdentifierSpec_tags'

    ModelIdentifierSpec_id = Column(Text(), ForeignKey('ModelIdentifierSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ModelIdentifierSpec_tags(ModelIdentifierSpec_id={self.ModelIdentifierSpec_id},tags={self.tags},)"



    


class IntrinsicAdapterSpecAdapterType(Base):
    """
    None
    """
    __tablename__ = 'IntrinsicAdapterSpec_adapter_type'

    IntrinsicAdapterSpec_id = Column(Text(), ForeignKey('IntrinsicAdapterSpec.id'), primary_key=True)
    adapter_type = Column(Enum('LORA', 'ALORA', name='AdapterTypeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"IntrinsicAdapterSpec_adapter_type(IntrinsicAdapterSpec_id={self.IntrinsicAdapterSpec_id},adapter_type={self.adapter_type},)"



    


class IntrinsicAdapterSpecCoverageScope(Base):
    """
    None
    """
    __tablename__ = 'IntrinsicAdapterSpec_coverage_scope'

    IntrinsicAdapterSpec_id = Column(Text(), ForeignKey('IntrinsicAdapterSpec.id'), primary_key=True)
    coverage_scope = Column(Enum('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST', name='CoverageScopeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"IntrinsicAdapterSpec_coverage_scope(IntrinsicAdapterSpec_id={self.IntrinsicAdapterSpec_id},coverage_scope={self.coverage_scope},)"



    


class IntrinsicAdapterSpecTags(Base):
    """
    None
    """
    __tablename__ = 'IntrinsicAdapterSpec_tags'

    IntrinsicAdapterSpec_id = Column(Text(), ForeignKey('IntrinsicAdapterSpec.id'), primary_key=True)
    tags = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"IntrinsicAdapterSpec_tags(IntrinsicAdapterSpec_id={self.IntrinsicAdapterSpec_id},tags={self.tags},)"



    


class RepositoryCatalog(NamedElement):
    """
    Top-level catalog rooting the analysed repository snapshot.
    """
    __tablename__ = 'RepositoryCatalog'

    repository_root = Column(Text())
    analyzed_on = Column(Date())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    
    
    includes_path_rel = relationship( "RepositoryCatalogIncludesPath" )
    includes_path = association_proxy("includes_path_rel", "includes_path",
                                  creator=lambda x_: RepositoryCatalogIncludesPath(includes_path=x_))
    
    
    excludes_path_rel = relationship( "RepositoryCatalogExcludesPath" )
    excludes_path = association_proxy("excludes_path_rel", "excludes_path",
                                  creator=lambda x_: RepositoryCatalogExcludesPath(excludes_path=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='RepositoryCatalog', source_slot='declares_element', mapping_type=None, target_class='ModelElement', target_slot='RepositoryCatalog_id', join_class=None, uses_join_table=None, multivalued=False)
    declares_element = relationship( "ModelElement", foreign_keys="[ModelElement.RepositoryCatalog_id]")
    
    
    coverage_scope_rel = relationship( "RepositoryCatalogCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: RepositoryCatalogCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "RepositoryCatalogTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: RepositoryCatalogTags(tags=x_))
    

    def __repr__(self):
        return f"RepositoryCatalog(repository_root={self.repository_root},analyzed_on={self.analyzed_on},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PythonPackage(NamedElement):
    """
    A logical Python package (directory) inside the repository.
    """
    __tablename__ = 'PythonPackage'

    package_name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    PythonPackage_id = Column(Text(), ForeignKey('PythonPackage.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PythonPackage', source_slot='depends_on_package', mapping_type=None, target_class='PythonPackage', target_slot='PythonPackage_id', join_class=None, uses_join_table=None, multivalued=False)
    depends_on_package = relationship( "PythonPackage", foreign_keys="[PythonPackage.PythonPackage_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PythonPackage', source_slot='declares_element', mapping_type=None, target_class='ModelElement', target_slot='PythonPackage_id', join_class=None, uses_join_table=None, multivalued=False)
    declares_element = relationship( "ModelElement", foreign_keys="[ModelElement.PythonPackage_id]")
    
    
    coverage_scope_rel = relationship( "PythonPackageCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: PythonPackageCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "PythonPackageTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: PythonPackageTags(tags=x_))
    

    def __repr__(self):
        return f"PythonPackage(package_name={self.package_name},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},PythonPackage_id={self.PythonPackage_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ModelElement(NamedElement):
    """
    Abstract base for concrete architectural elements.
    """
    __tablename__ = 'ModelElement'

    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    RepositoryCatalog_id = Column(Text(), ForeignKey('RepositoryCatalog.id'))
    PythonPackage_id = Column(Text(), ForeignKey('PythonPackage.id'))
    
    
    coverage_scope_rel = relationship( "ModelElementCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: ModelElementCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "ModelElementTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: ModelElementTags(tags=x_))
    

    def __repr__(self):
        return f"ModelElement(id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},RepositoryCatalog_id={self.RepositoryCatalog_id},PythonPackage_id={self.PythonPackage_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ApiFieldSpec(NamedElement):
    """
    Specification of a single field in an API model.
    """
    __tablename__ = 'ApiFieldSpec'

    field_name = Column(Text())
    field_type = Column(Text())
    required_field = Column(Boolean())
    allows_null = Column(Boolean())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    ApiModelSpec_id = Column(Text(), ForeignKey('ApiModelSpec.id'))
    
    
    coverage_scope_rel = relationship( "ApiFieldSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: ApiFieldSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "ApiFieldSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: ApiFieldSpecTags(tags=x_))
    

    def __repr__(self):
        return f"ApiFieldSpec(field_name={self.field_name},field_type={self.field_type},required_field={self.required_field},allows_null={self.allows_null},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},ApiModelSpec_id={self.ApiModelSpec_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MethodSpec(NamedElement):
    """
    Specification of a method exposed by a runtime class.
    """
    __tablename__ = 'MethodSpec'

    method_name = Column(Text())
    method_signature = Column(Text())
    lifecycle_role = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    SessionSpec_id = Column(Text(), ForeignKey('SessionSpec.id'))
    
    
    coverage_scope_rel = relationship( "MethodSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: MethodSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "MethodSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: MethodSpecTags(tags=x_))
    

    def __repr__(self):
        return f"MethodSpec(method_name={self.method_name},method_signature={self.method_signature},lifecycle_role={self.lifecycle_role},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},SessionSpec_id={self.SessionSpec_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ModelIdentifierSpec(NamedElement):
    """
    Cross-provider identifier table for a single model.
    """
    __tablename__ = 'ModelIdentifierSpec'

    hf_model_name = Column(Text())
    ollama_name = Column(Text())
    watsonx_name = Column(Text())
    openai_name = Column(Text())
    bedrock_name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    BackendSpec_id = Column(Text(), ForeignKey('BackendSpec.id'))
    
    
    provider_name_rel = relationship( "ModelIdentifierSpecProviderName" )
    provider_name = association_proxy("provider_name_rel", "provider_name",
                                  creator=lambda x_: ModelIdentifierSpecProviderName(provider_name=x_))
    
    
    coverage_scope_rel = relationship( "ModelIdentifierSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: ModelIdentifierSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "ModelIdentifierSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: ModelIdentifierSpecTags(tags=x_))
    

    def __repr__(self):
        return f"ModelIdentifierSpec(hf_model_name={self.hf_model_name},ollama_name={self.ollama_name},watsonx_name={self.watsonx_name},openai_name={self.openai_name},bedrock_name={self.bedrock_name},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},BackendSpec_id={self.BackendSpec_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class IntrinsicAdapterSpec(NamedElement):
    """
    Specification of an intrinsic adapter (LoRA / aLoRA).
    """
    __tablename__ = 'IntrinsicAdapterSpec'

    repo_id = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    
    
    adapter_type_rel = relationship( "IntrinsicAdapterSpecAdapterType" )
    adapter_type = association_proxy("adapter_type_rel", "adapter_type",
                                  creator=lambda x_: IntrinsicAdapterSpecAdapterType(adapter_type=x_))
    
    
    coverage_scope_rel = relationship( "IntrinsicAdapterSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: IntrinsicAdapterSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "IntrinsicAdapterSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: IntrinsicAdapterSpecTags(tags=x_))
    

    def __repr__(self):
        return f"IntrinsicAdapterSpec(repo_id={self.repo_id},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class BackendSpec(ModelElement):
    """
    Specification of a Mellea backend implementation.
    """
    __tablename__ = 'BackendSpec'

    backend_family = Column(Enum('BEDROCK', 'DUMMY', 'HUGGINGFACE', 'LITELLM', 'OLLAMA', 'OPENAI', 'WATSONX', name='BackendFamilyEnum'))
    default_formatter = Column(Text(), ForeignKey('FormatterSpec.id'))
    supports_streaming = Column(Boolean())
    supports_tool_calls = Column(Boolean())
    supports_multimodal = Column(Boolean())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='BackendSpec', source_slot='model_identifier', mapping_type=None, target_class='ModelIdentifierSpec', target_slot='BackendSpec_id', join_class=None, uses_join_table=None, multivalued=False)
    model_identifier = relationship( "ModelIdentifierSpec", foreign_keys="[ModelIdentifierSpec.BackendSpec_id]")
    
    
    model_options_key_rel = relationship( "BackendSpecModelOptionsKey" )
    model_options_key = association_proxy("model_options_key_rel", "model_options_key",
                                  creator=lambda x_: BackendSpecModelOptionsKey(model_options_key=x_))
    
    
    coverage_scope_rel = relationship( "BackendSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: BackendSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "BackendSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: BackendSpecTags(tags=x_))
    

    def __repr__(self):
        return f"BackendSpec(backend_family={self.backend_family},default_formatter={self.default_formatter},supports_streaming={self.supports_streaming},supports_tool_calls={self.supports_tool_calls},supports_multimodal={self.supports_multimodal},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class FormatterSpec(ModelElement):
    """
    Specification of an output formatter for a backend.
    """
    __tablename__ = 'FormatterSpec'

    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    
    
    coverage_scope_rel = relationship( "FormatterSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: FormatterSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "FormatterSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: FormatterSpecTags(tags=x_))
    

    def __repr__(self):
        return f"FormatterSpec(id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ContextSpec(ModelElement):
    """
    Specification of a context implementation.
    """
    __tablename__ = 'ContextSpec'

    context_linearity = Column(Enum('LINEAR', 'NON_LINEAR', name='ContextLinearityEnum'))
    stores_component_history = Column(Boolean())
    accepts_message_attachments = Column(Boolean())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    
    
    coverage_scope_rel = relationship( "ContextSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: ContextSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "ContextSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: ContextSpecTags(tags=x_))
    

    def __repr__(self):
        return f"ContextSpec(context_linearity={self.context_linearity},stores_component_history={self.stores_component_history},accepts_message_attachments={self.accepts_message_attachments},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SessionSpec(ModelElement):
    """
    Specification of a Mellea session.
    """
    __tablename__ = 'SessionSpec'

    uses_backend = Column(Text(), ForeignKey('BackendSpec.id'))
    uses_context = Column(Text(), ForeignKey('ContextSpec.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='SessionSpec', source_slot='exposed_method', mapping_type=None, target_class='MethodSpec', target_slot='SessionSpec_id', join_class=None, uses_join_table=None, multivalued=False)
    exposed_method = relationship( "MethodSpec", foreign_keys="[MethodSpec.SessionSpec_id]")
    
    
    coverage_scope_rel = relationship( "SessionSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: SessionSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "SessionSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: SessionSpecTags(tags=x_))
    

    def __repr__(self):
        return f"SessionSpec(uses_backend={self.uses_backend},uses_context={self.uses_context},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ComponentSpec(ModelElement):
    """
    Specification of a Mellea stdlib component type.
    """
    __tablename__ = 'ComponentSpec'

    component_category = Column(Enum('INSTRUCTION', 'MESSAGE', 'TOOL_MESSAGE', 'DOCUMENT', 'INTRINSIC', 'MOBJECT', 'QUERY', 'TRANSFORM', 'GENSTUB', 'REQUIREMENT', 'STREAM_EVENT', name='ComponentCategoryEnum'))
    parsed_output_type = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    
    
    input_modality_rel = relationship( "ComponentSpecInputModality" )
    input_modality = association_proxy("input_modality_rel", "input_modality",
                                  creator=lambda x_: ComponentSpecInputModality(input_modality=x_))
    
    
    coverage_scope_rel = relationship( "ComponentSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: ComponentSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "ComponentSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: ComponentSpecTags(tags=x_))
    

    def __repr__(self):
        return f"ComponentSpec(component_category={self.component_category},parsed_output_type={self.parsed_output_type},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class RequirementSpec(ModelElement):
    """
    Specification of a requirement validator.
    """
    __tablename__ = 'RequirementSpec'

    validation_style = Column(Text())
    may_trigger_repair = Column(Boolean())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    
    
    coverage_scope_rel = relationship( "RequirementSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: RequirementSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "RequirementSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: RequirementSpecTags(tags=x_))
    

    def __repr__(self):
        return f"RequirementSpec(validation_style={self.validation_style},may_trigger_repair={self.may_trigger_repair},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SamplingStrategySpec(ModelElement):
    """
    Specification of a sampling-loop strategy.
    """
    __tablename__ = 'SamplingStrategySpec'

    selection_policy = Column(Text())
    loop_budget_hint = Column(Integer())
    may_trigger_repair = Column(Boolean())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    
    
    coverage_scope_rel = relationship( "SamplingStrategySpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: SamplingStrategySpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "SamplingStrategySpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: SamplingStrategySpecTags(tags=x_))
    

    def __repr__(self):
        return f"SamplingStrategySpec(selection_policy={self.selection_policy},loop_budget_hint={self.loop_budget_hint},may_trigger_repair={self.may_trigger_repair},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PluginSpec(ModelElement):
    """
    Specification of a Mellea plugin and the hooks it registers.
    """
    __tablename__ = 'PluginSpec'

    plugin_mode = Column(Enum('SEQUENTIAL', 'TRANSFORM', 'CONCURRENT', 'AUDIT', 'FIRE_AND_FORGET', name='PluginModeEnum'))
    plugin_priority = Column(Integer())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    
    
    hook_type_rel = relationship( "PluginSpecHookType" )
    hook_type = association_proxy("hook_type_rel", "hook_type",
                                  creator=lambda x_: PluginSpecHookType(hook_type=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PluginSpec', source_slot='payload_model', mapping_type=None, target_class='HookPayloadSpec', target_slot='PluginSpec_id', join_class=None, uses_join_table=None, multivalued=False)
    payload_model = relationship( "HookPayloadSpec", foreign_keys="[HookPayloadSpec.PluginSpec_id]")
    
    
    coverage_scope_rel = relationship( "PluginSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: PluginSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "PluginSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: PluginSpecTags(tags=x_))
    

    def __repr__(self):
        return f"PluginSpec(plugin_mode={self.plugin_mode},plugin_priority={self.plugin_priority},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class HookPayloadSpec(ModelElement):
    """
    Specification of a hook payload model.
    """
    __tablename__ = 'HookPayloadSpec'

    lifecycle_role = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    PluginSpec_id = Column(Text(), ForeignKey('PluginSpec.id'))
    
    
    hook_type_rel = relationship( "HookPayloadSpecHookType" )
    hook_type = association_proxy("hook_type_rel", "hook_type",
                                  creator=lambda x_: HookPayloadSpecHookType(hook_type=x_))
    
    
    coverage_scope_rel = relationship( "HookPayloadSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: HookPayloadSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "HookPayloadSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: HookPayloadSpecTags(tags=x_))
    

    def __repr__(self):
        return f"HookPayloadSpec(lifecycle_role={self.lifecycle_role},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},PluginSpec_id={self.PluginSpec_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class TelemetryMetricSpec(ModelElement):
    """
    Specification of a telemetry metric emitted by Mellea.
    """
    __tablename__ = 'TelemetryMetricSpec'

    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    
    
    metric_name_rel = relationship( "TelemetryMetricSpecMetricName" )
    metric_name = association_proxy("metric_name_rel", "metric_name",
                                  creator=lambda x_: TelemetryMetricSpecMetricName(metric_name=x_))
    
    
    coverage_scope_rel = relationship( "TelemetryMetricSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: TelemetryMetricSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "TelemetryMetricSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: TelemetryMetricSpecTags(tags=x_))
    

    def __repr__(self):
        return f"TelemetryMetricSpec(id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CliCommandSpec(ModelElement):
    """
    Specification of a CLI command exposed under `m`.
    """
    __tablename__ = 'CliCommandSpec'

    command_group = Column(Text())
    command_path = Column(Text())
    command_purpose = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='CliCommandSpec', source_slot='input_model', mapping_type=None, target_class='ApiModelSpec', target_slot='CliCommandSpec_id', join_class=None, uses_join_table=None, multivalued=False)
    input_model = relationship( "ApiModelSpec", foreign_keys="[ApiModelSpec.CliCommandSpec_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='CliCommandSpec', source_slot='output_model', mapping_type=None, target_class='ApiModelSpec', target_slot='CliCommandSpec_id', join_class=None, uses_join_table=None, multivalued=False)
    output_model = relationship( "ApiModelSpec", foreign_keys="[ApiModelSpec.CliCommandSpec_id]")
    
    
    coverage_scope_rel = relationship( "CliCommandSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: CliCommandSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "CliCommandSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: CliCommandSpecTags(tags=x_))
    

    def __repr__(self):
        return f"CliCommandSpec(command_group={self.command_group},command_path={self.command_path},command_purpose={self.command_purpose},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ApiModelSpec(ModelElement):
    """
    Specification of an HTTP API wire model.
    """
    __tablename__ = 'ApiModelSpec'

    request_or_response = Column(Enum('REQUEST', 'RESPONSE', 'BOTH', name='RequestResponseEnum'))
    openai_object_type = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    module_path = Column(Text())
    source_file = Column(Text())
    package_kind = Column(Enum('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST', name='PackageKindEnum'))
    element_kind = Column(Enum('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN', name='ElementKindEnum'))
    CliCommandSpec_id = Column(Text(), ForeignKey('CliCommandSpec.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ApiModelSpec', source_slot='has_field', mapping_type=None, target_class='ApiFieldSpec', target_slot='ApiModelSpec_id', join_class=None, uses_join_table=None, multivalued=False)
    has_field = relationship( "ApiFieldSpec", foreign_keys="[ApiFieldSpec.ApiModelSpec_id]")
    
    
    coverage_scope_rel = relationship( "ApiModelSpecCoverageScope" )
    coverage_scope = association_proxy("coverage_scope_rel", "coverage_scope",
                                  creator=lambda x_: ApiModelSpecCoverageScope(coverage_scope=x_))
    
    
    tags_rel = relationship( "ApiModelSpecTags" )
    tags = association_proxy("tags_rel", "tags",
                                  creator=lambda x_: ApiModelSpecTags(tags=x_))
    

    def __repr__(self):
        return f"ApiModelSpec(request_or_response={self.request_or_response},openai_object_type={self.openai_object_type},id={self.id},name={self.name},description={self.description},module_path={self.module_path},source_file={self.source_file},package_kind={self.package_kind},element_kind={self.element_kind},CliCommandSpec_id={self.CliCommandSpec_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


