-- ====================================================================
-- SQL Validation Queries
-- Generated from LinkML schema
-- LinkML v1.11.1
-- Generator: sqlvalidationgen.py v0.1.0
-- Dialect: sqlite
-- ====================================================================

SELECT 'RepositoryCatalog' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RepositoryCatalog" 
WHERE "RepositoryCatalog".id IS NULL

UNION ALL

SELECT 'RepositoryCatalog' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "RepositoryCatalog" 
WHERE "RepositoryCatalog".id IN (SELECT id 
FROM "RepositoryCatalog" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'RepositoryCatalog' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RepositoryCatalog" 
WHERE "RepositoryCatalog".name IS NULL

UNION ALL

SELECT 'RepositoryCatalog' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "RepositoryCatalog" 
WHERE "RepositoryCatalog".package_kind IS NOT NULL AND ("RepositoryCatalog".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'RepositoryCatalog' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "RepositoryCatalog" 
WHERE "RepositoryCatalog".element_kind IS NOT NULL AND ("RepositoryCatalog".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'RepositoryCatalog' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "RepositoryCatalog" 
WHERE "RepositoryCatalog".coverage_scope IS NOT NULL AND ("RepositoryCatalog".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'PythonPackage' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PythonPackage" 
WHERE "PythonPackage".id IS NULL

UNION ALL

SELECT 'PythonPackage' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "PythonPackage" 
WHERE "PythonPackage".id IN (SELECT id 
FROM "PythonPackage" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'PythonPackage' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PythonPackage" 
WHERE "PythonPackage".name IS NULL

UNION ALL

SELECT 'PythonPackage' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "PythonPackage" 
WHERE "PythonPackage".package_kind IS NOT NULL AND ("PythonPackage".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'PythonPackage' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "PythonPackage" 
WHERE "PythonPackage".element_kind IS NOT NULL AND ("PythonPackage".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'PythonPackage' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "PythonPackage" 
WHERE "PythonPackage".coverage_scope IS NOT NULL AND ("PythonPackage".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'BackendSpec' AS table_name, 'backend_family' AS column_name, 'enum' AS constraint_type, id AS record_id, backend_family AS invalid_value 
FROM "BackendSpec" 
WHERE "BackendSpec".backend_family IS NOT NULL AND ("BackendSpec".backend_family NOT IN ('BEDROCK', 'DUMMY', 'HUGGINGFACE', 'LITELLM', 'OLLAMA', 'OPENAI', 'WATSONX'))

UNION ALL

SELECT 'BackendSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "BackendSpec" 
WHERE "BackendSpec".id IS NULL

UNION ALL

SELECT 'BackendSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "BackendSpec" 
WHERE "BackendSpec".id IN (SELECT id 
FROM "BackendSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'BackendSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "BackendSpec" 
WHERE "BackendSpec".name IS NULL

UNION ALL

SELECT 'BackendSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "BackendSpec" 
WHERE "BackendSpec".package_kind IS NOT NULL AND ("BackendSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'BackendSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "BackendSpec" 
WHERE "BackendSpec".element_kind IS NOT NULL AND ("BackendSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'BackendSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "BackendSpec" 
WHERE "BackendSpec".coverage_scope IS NOT NULL AND ("BackendSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'FormatterSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "FormatterSpec" 
WHERE "FormatterSpec".id IS NULL

UNION ALL

SELECT 'FormatterSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "FormatterSpec" 
WHERE "FormatterSpec".id IN (SELECT id 
FROM "FormatterSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'FormatterSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "FormatterSpec" 
WHERE "FormatterSpec".name IS NULL

UNION ALL

SELECT 'FormatterSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "FormatterSpec" 
WHERE "FormatterSpec".package_kind IS NOT NULL AND ("FormatterSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'FormatterSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "FormatterSpec" 
WHERE "FormatterSpec".element_kind IS NOT NULL AND ("FormatterSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'FormatterSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "FormatterSpec" 
WHERE "FormatterSpec".coverage_scope IS NOT NULL AND ("FormatterSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'ContextSpec' AS table_name, 'context_linearity' AS column_name, 'enum' AS constraint_type, id AS record_id, context_linearity AS invalid_value 
FROM "ContextSpec" 
WHERE "ContextSpec".context_linearity IS NOT NULL AND ("ContextSpec".context_linearity NOT IN ('LINEAR', 'NON_LINEAR'))

UNION ALL

SELECT 'ContextSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ContextSpec" 
WHERE "ContextSpec".id IS NULL

UNION ALL

SELECT 'ContextSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "ContextSpec" 
WHERE "ContextSpec".id IN (SELECT id 
FROM "ContextSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'ContextSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ContextSpec" 
WHERE "ContextSpec".name IS NULL

UNION ALL

SELECT 'ContextSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "ContextSpec" 
WHERE "ContextSpec".package_kind IS NOT NULL AND ("ContextSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'ContextSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "ContextSpec" 
WHERE "ContextSpec".element_kind IS NOT NULL AND ("ContextSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'ContextSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "ContextSpec" 
WHERE "ContextSpec".coverage_scope IS NOT NULL AND ("ContextSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'SessionSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SessionSpec" 
WHERE "SessionSpec".id IS NULL

UNION ALL

SELECT 'SessionSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "SessionSpec" 
WHERE "SessionSpec".id IN (SELECT id 
FROM "SessionSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'SessionSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SessionSpec" 
WHERE "SessionSpec".name IS NULL

UNION ALL

SELECT 'SessionSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "SessionSpec" 
WHERE "SessionSpec".package_kind IS NOT NULL AND ("SessionSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'SessionSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "SessionSpec" 
WHERE "SessionSpec".element_kind IS NOT NULL AND ("SessionSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'SessionSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "SessionSpec" 
WHERE "SessionSpec".coverage_scope IS NOT NULL AND ("SessionSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'ComponentSpec' AS table_name, 'component_category' AS column_name, 'enum' AS constraint_type, id AS record_id, component_category AS invalid_value 
FROM "ComponentSpec" 
WHERE "ComponentSpec".component_category IS NOT NULL AND ("ComponentSpec".component_category NOT IN ('INSTRUCTION', 'MESSAGE', 'TOOL_MESSAGE', 'DOCUMENT', 'INTRINSIC', 'MOBJECT', 'QUERY', 'TRANSFORM', 'GENSTUB', 'REQUIREMENT', 'STREAM_EVENT'))

UNION ALL

SELECT 'ComponentSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ComponentSpec" 
WHERE "ComponentSpec".id IS NULL

UNION ALL

SELECT 'ComponentSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "ComponentSpec" 
WHERE "ComponentSpec".id IN (SELECT id 
FROM "ComponentSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'ComponentSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ComponentSpec" 
WHERE "ComponentSpec".name IS NULL

UNION ALL

SELECT 'ComponentSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "ComponentSpec" 
WHERE "ComponentSpec".package_kind IS NOT NULL AND ("ComponentSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'ComponentSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "ComponentSpec" 
WHERE "ComponentSpec".element_kind IS NOT NULL AND ("ComponentSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'ComponentSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "ComponentSpec" 
WHERE "ComponentSpec".coverage_scope IS NOT NULL AND ("ComponentSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'RequirementSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RequirementSpec" 
WHERE "RequirementSpec".id IS NULL

UNION ALL

SELECT 'RequirementSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "RequirementSpec" 
WHERE "RequirementSpec".id IN (SELECT id 
FROM "RequirementSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'RequirementSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RequirementSpec" 
WHERE "RequirementSpec".name IS NULL

UNION ALL

SELECT 'RequirementSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "RequirementSpec" 
WHERE "RequirementSpec".package_kind IS NOT NULL AND ("RequirementSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'RequirementSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "RequirementSpec" 
WHERE "RequirementSpec".element_kind IS NOT NULL AND ("RequirementSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'RequirementSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "RequirementSpec" 
WHERE "RequirementSpec".coverage_scope IS NOT NULL AND ("RequirementSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'SamplingStrategySpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SamplingStrategySpec" 
WHERE "SamplingStrategySpec".id IS NULL

UNION ALL

SELECT 'SamplingStrategySpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "SamplingStrategySpec" 
WHERE "SamplingStrategySpec".id IN (SELECT id 
FROM "SamplingStrategySpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'SamplingStrategySpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SamplingStrategySpec" 
WHERE "SamplingStrategySpec".name IS NULL

UNION ALL

SELECT 'SamplingStrategySpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "SamplingStrategySpec" 
WHERE "SamplingStrategySpec".package_kind IS NOT NULL AND ("SamplingStrategySpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'SamplingStrategySpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "SamplingStrategySpec" 
WHERE "SamplingStrategySpec".element_kind IS NOT NULL AND ("SamplingStrategySpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'SamplingStrategySpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "SamplingStrategySpec" 
WHERE "SamplingStrategySpec".coverage_scope IS NOT NULL AND ("SamplingStrategySpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'PluginSpec' AS table_name, 'plugin_mode' AS column_name, 'enum' AS constraint_type, id AS record_id, plugin_mode AS invalid_value 
FROM "PluginSpec" 
WHERE "PluginSpec".plugin_mode IS NOT NULL AND ("PluginSpec".plugin_mode NOT IN ('SEQUENTIAL', 'TRANSFORM', 'CONCURRENT', 'AUDIT', 'FIRE_AND_FORGET'))

UNION ALL

SELECT 'PluginSpec' AS table_name, 'hook_type' AS column_name, 'enum' AS constraint_type, id AS record_id, hook_type AS invalid_value 
FROM "PluginSpec" 
WHERE "PluginSpec".hook_type IS NOT NULL AND ("PluginSpec".hook_type NOT IN ('SESSION_PRE_INIT', 'SESSION_POST_INIT', 'SESSION_RESET', 'SESSION_CLEANUP', 'COMPONENT_PRE_EXECUTE', 'COMPONENT_POST_SUCCESS', 'COMPONENT_POST_ERROR', 'GENERATION_PRE_CALL', 'GENERATION_POST_CALL', 'GENERATION_ERROR', 'VALIDATION_PRE_CHECK', 'VALIDATION_POST_CHECK', 'SAMPLING_LOOP_START', 'SAMPLING_ITERATION', 'SAMPLING_REPAIR', 'SAMPLING_LOOP_END', 'TOOL_PRE_INVOKE', 'TOOL_POST_INVOKE'))

UNION ALL

SELECT 'PluginSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PluginSpec" 
WHERE "PluginSpec".id IS NULL

UNION ALL

SELECT 'PluginSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "PluginSpec" 
WHERE "PluginSpec".id IN (SELECT id 
FROM "PluginSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'PluginSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PluginSpec" 
WHERE "PluginSpec".name IS NULL

UNION ALL

SELECT 'PluginSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "PluginSpec" 
WHERE "PluginSpec".package_kind IS NOT NULL AND ("PluginSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'PluginSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "PluginSpec" 
WHERE "PluginSpec".element_kind IS NOT NULL AND ("PluginSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'PluginSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "PluginSpec" 
WHERE "PluginSpec".coverage_scope IS NOT NULL AND ("PluginSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'HookPayloadSpec' AS table_name, 'hook_type' AS column_name, 'enum' AS constraint_type, id AS record_id, hook_type AS invalid_value 
FROM "HookPayloadSpec" 
WHERE "HookPayloadSpec".hook_type IS NOT NULL AND ("HookPayloadSpec".hook_type NOT IN ('SESSION_PRE_INIT', 'SESSION_POST_INIT', 'SESSION_RESET', 'SESSION_CLEANUP', 'COMPONENT_PRE_EXECUTE', 'COMPONENT_POST_SUCCESS', 'COMPONENT_POST_ERROR', 'GENERATION_PRE_CALL', 'GENERATION_POST_CALL', 'GENERATION_ERROR', 'VALIDATION_PRE_CHECK', 'VALIDATION_POST_CHECK', 'SAMPLING_LOOP_START', 'SAMPLING_ITERATION', 'SAMPLING_REPAIR', 'SAMPLING_LOOP_END', 'TOOL_PRE_INVOKE', 'TOOL_POST_INVOKE'))

UNION ALL

SELECT 'HookPayloadSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "HookPayloadSpec" 
WHERE "HookPayloadSpec".id IS NULL

UNION ALL

SELECT 'HookPayloadSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "HookPayloadSpec" 
WHERE "HookPayloadSpec".id IN (SELECT id 
FROM "HookPayloadSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'HookPayloadSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "HookPayloadSpec" 
WHERE "HookPayloadSpec".name IS NULL

UNION ALL

SELECT 'HookPayloadSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "HookPayloadSpec" 
WHERE "HookPayloadSpec".package_kind IS NOT NULL AND ("HookPayloadSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'HookPayloadSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "HookPayloadSpec" 
WHERE "HookPayloadSpec".element_kind IS NOT NULL AND ("HookPayloadSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'HookPayloadSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "HookPayloadSpec" 
WHERE "HookPayloadSpec".coverage_scope IS NOT NULL AND ("HookPayloadSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'TelemetryMetricSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "TelemetryMetricSpec" 
WHERE "TelemetryMetricSpec".id IS NULL

UNION ALL

SELECT 'TelemetryMetricSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "TelemetryMetricSpec" 
WHERE "TelemetryMetricSpec".id IN (SELECT id 
FROM "TelemetryMetricSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'TelemetryMetricSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "TelemetryMetricSpec" 
WHERE "TelemetryMetricSpec".name IS NULL

UNION ALL

SELECT 'TelemetryMetricSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "TelemetryMetricSpec" 
WHERE "TelemetryMetricSpec".package_kind IS NOT NULL AND ("TelemetryMetricSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'TelemetryMetricSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "TelemetryMetricSpec" 
WHERE "TelemetryMetricSpec".element_kind IS NOT NULL AND ("TelemetryMetricSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'TelemetryMetricSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "TelemetryMetricSpec" 
WHERE "TelemetryMetricSpec".coverage_scope IS NOT NULL AND ("TelemetryMetricSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'CliCommandSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "CliCommandSpec" 
WHERE "CliCommandSpec".id IS NULL

UNION ALL

SELECT 'CliCommandSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "CliCommandSpec" 
WHERE "CliCommandSpec".id IN (SELECT id 
FROM "CliCommandSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'CliCommandSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "CliCommandSpec" 
WHERE "CliCommandSpec".name IS NULL

UNION ALL

SELECT 'CliCommandSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "CliCommandSpec" 
WHERE "CliCommandSpec".package_kind IS NOT NULL AND ("CliCommandSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'CliCommandSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "CliCommandSpec" 
WHERE "CliCommandSpec".element_kind IS NOT NULL AND ("CliCommandSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'CliCommandSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "CliCommandSpec" 
WHERE "CliCommandSpec".coverage_scope IS NOT NULL AND ("CliCommandSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'ApiModelSpec' AS table_name, 'request_or_response' AS column_name, 'enum' AS constraint_type, id AS record_id, request_or_response AS invalid_value 
FROM "ApiModelSpec" 
WHERE "ApiModelSpec".request_or_response IS NOT NULL AND ("ApiModelSpec".request_or_response NOT IN ('REQUEST', 'RESPONSE', 'BOTH'))

UNION ALL

SELECT 'ApiModelSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ApiModelSpec" 
WHERE "ApiModelSpec".id IS NULL

UNION ALL

SELECT 'ApiModelSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "ApiModelSpec" 
WHERE "ApiModelSpec".id IN (SELECT id 
FROM "ApiModelSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'ApiModelSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ApiModelSpec" 
WHERE "ApiModelSpec".name IS NULL

UNION ALL

SELECT 'ApiModelSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "ApiModelSpec" 
WHERE "ApiModelSpec".package_kind IS NOT NULL AND ("ApiModelSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'ApiModelSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "ApiModelSpec" 
WHERE "ApiModelSpec".element_kind IS NOT NULL AND ("ApiModelSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'ApiModelSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "ApiModelSpec" 
WHERE "ApiModelSpec".coverage_scope IS NOT NULL AND ("ApiModelSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'ApiFieldSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ApiFieldSpec" 
WHERE "ApiFieldSpec".id IS NULL

UNION ALL

SELECT 'ApiFieldSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "ApiFieldSpec" 
WHERE "ApiFieldSpec".id IN (SELECT id 
FROM "ApiFieldSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'ApiFieldSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ApiFieldSpec" 
WHERE "ApiFieldSpec".name IS NULL

UNION ALL

SELECT 'ApiFieldSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "ApiFieldSpec" 
WHERE "ApiFieldSpec".package_kind IS NOT NULL AND ("ApiFieldSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'ApiFieldSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "ApiFieldSpec" 
WHERE "ApiFieldSpec".element_kind IS NOT NULL AND ("ApiFieldSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'ApiFieldSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "ApiFieldSpec" 
WHERE "ApiFieldSpec".coverage_scope IS NOT NULL AND ("ApiFieldSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'MethodSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MethodSpec" 
WHERE "MethodSpec".id IS NULL

UNION ALL

SELECT 'MethodSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "MethodSpec" 
WHERE "MethodSpec".id IN (SELECT id 
FROM "MethodSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'MethodSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MethodSpec" 
WHERE "MethodSpec".name IS NULL

UNION ALL

SELECT 'MethodSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "MethodSpec" 
WHERE "MethodSpec".package_kind IS NOT NULL AND ("MethodSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'MethodSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "MethodSpec" 
WHERE "MethodSpec".element_kind IS NOT NULL AND ("MethodSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'MethodSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "MethodSpec" 
WHERE "MethodSpec".coverage_scope IS NOT NULL AND ("MethodSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'ModelIdentifierSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ModelIdentifierSpec" 
WHERE "ModelIdentifierSpec".id IS NULL

UNION ALL

SELECT 'ModelIdentifierSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "ModelIdentifierSpec" 
WHERE "ModelIdentifierSpec".id IN (SELECT id 
FROM "ModelIdentifierSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'ModelIdentifierSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ModelIdentifierSpec" 
WHERE "ModelIdentifierSpec".name IS NULL

UNION ALL

SELECT 'ModelIdentifierSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "ModelIdentifierSpec" 
WHERE "ModelIdentifierSpec".package_kind IS NOT NULL AND ("ModelIdentifierSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'ModelIdentifierSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "ModelIdentifierSpec" 
WHERE "ModelIdentifierSpec".element_kind IS NOT NULL AND ("ModelIdentifierSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'ModelIdentifierSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "ModelIdentifierSpec" 
WHERE "ModelIdentifierSpec".coverage_scope IS NOT NULL AND ("ModelIdentifierSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'))

UNION ALL

SELECT 'IntrinsicAdapterSpec' AS table_name, 'adapter_type' AS column_name, 'enum' AS constraint_type, id AS record_id, adapter_type AS invalid_value 
FROM "IntrinsicAdapterSpec" 
WHERE "IntrinsicAdapterSpec".adapter_type IS NOT NULL AND ("IntrinsicAdapterSpec".adapter_type NOT IN ('LORA', 'ALORA'))

UNION ALL

SELECT 'IntrinsicAdapterSpec' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "IntrinsicAdapterSpec" 
WHERE "IntrinsicAdapterSpec".id IS NULL

UNION ALL

SELECT 'IntrinsicAdapterSpec' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "IntrinsicAdapterSpec" 
WHERE "IntrinsicAdapterSpec".id IN (SELECT id 
FROM "IntrinsicAdapterSpec" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'IntrinsicAdapterSpec' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "IntrinsicAdapterSpec" 
WHERE "IntrinsicAdapterSpec".name IS NULL

UNION ALL

SELECT 'IntrinsicAdapterSpec' AS table_name, 'package_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, package_kind AS invalid_value 
FROM "IntrinsicAdapterSpec" 
WHERE "IntrinsicAdapterSpec".package_kind IS NOT NULL AND ("IntrinsicAdapterSpec".package_kind NOT IN ('CORE', 'STDLIB', 'BACKENDS', 'FORMATTERS', 'HELPERS', 'PLUGINS', 'TELEMETRY', 'CLI', 'DOCS_EXAMPLES', 'TEST'))

UNION ALL

SELECT 'IntrinsicAdapterSpec' AS table_name, 'element_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, element_kind AS invalid_value 
FROM "IntrinsicAdapterSpec" 
WHERE "IntrinsicAdapterSpec".element_kind IS NOT NULL AND ("IntrinsicAdapterSpec".element_kind NOT IN ('CLASS', 'ENUM', 'DATACLASS', 'TYPED_DICT', 'PYDANTIC_MODEL', 'PROTOCOL', 'FUNCTION', 'MIXIN'))

UNION ALL

SELECT 'IntrinsicAdapterSpec' AS table_name, 'coverage_scope' AS column_name, 'enum' AS constraint_type, id AS record_id, coverage_scope AS invalid_value 
FROM "IntrinsicAdapterSpec" 
WHERE "IntrinsicAdapterSpec".coverage_scope IS NOT NULL AND ("IntrinsicAdapterSpec".coverage_scope NOT IN ('SOURCE', 'API', 'CLI', 'EXAMPLE', 'TEST'));

