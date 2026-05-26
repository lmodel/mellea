#![allow(non_camel_case_types)]

use crate::*;
use crate::poly_containers::*;


pub trait NamedElement   {

    fn id<'a>(&'a self) -> &'a crate::uriorcurie;
    // fn id_mut(&mut self) -> &mut &'a crate::uriorcurie;
    // fn set_id(&mut self, value: uriorcurie);

    fn name<'a>(&'a self) -> &'a str;
    // fn name_mut(&mut self) -> &mut &'a str;
    // fn set_name(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn module_path<'a>(&'a self) -> Option<&'a str>;
    // fn module_path_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_module_path(&mut self, value: Option<&'a str>);

    fn source_file<'a>(&'a self) -> Option<&'a str>;
    // fn source_file_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_source_file(&mut self, value: Option<&'a str>);

    fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum>;
    // fn package_kind_mut(&mut self) -> &mut Option<&'a crate::PackageKindEnum>;
    // fn set_package_kind(&mut self, value: Option<&'a PackageKindEnum>);

    fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum>;
    // fn element_kind_mut(&mut self) -> &mut Option<&'a crate::ElementKindEnum>;
    // fn set_element_kind(&mut self, value: Option<&'a ElementKindEnum>);

    fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>>;
    // fn coverage_scope_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>>;
    // fn set_coverage_scope(&mut self, value: Option<&Vec<CoverageScopeEnum>>);

    fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn tags_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_tags(&mut self, value: Option<&Vec<String>>);


}

impl NamedElement for crate::NamedElement {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::RepositoryCatalog {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::PythonPackage {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::ModelElement {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::ApiFieldSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::MethodSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::ModelIdentifierSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::IntrinsicAdapterSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::BackendSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::FormatterSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::ContextSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::SessionSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::ComponentSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::RequirementSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::SamplingStrategySpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::PluginSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::HookPayloadSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::TelemetryMetricSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::CliCommandSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}
impl NamedElement for crate::ApiModelSpec {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        return &self.id;
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        return self.module_path.as_deref();
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        return self.source_file.as_deref();
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        return self.package_kind.as_ref();
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        return self.element_kind.as_ref();
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        return self.coverage_scope.as_ref();
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.tags.as_ref();
    }
}

impl NamedElement for crate::NamedElementOrSubtype {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        match self {
                NamedElementOrSubtype::RepositoryCatalog(val) => val.id(),
                NamedElementOrSubtype::PythonPackage(val) => val.id(),
                NamedElementOrSubtype::ModelElement(val) => val.id(),
                NamedElementOrSubtype::ApiFieldSpec(val) => val.id(),
                NamedElementOrSubtype::MethodSpec(val) => val.id(),
                NamedElementOrSubtype::ModelIdentifierSpec(val) => val.id(),
                NamedElementOrSubtype::IntrinsicAdapterSpec(val) => val.id(),
                NamedElementOrSubtype::BackendSpec(val) => val.id(),
                NamedElementOrSubtype::FormatterSpec(val) => val.id(),
                NamedElementOrSubtype::ContextSpec(val) => val.id(),
                NamedElementOrSubtype::SessionSpec(val) => val.id(),
                NamedElementOrSubtype::ComponentSpec(val) => val.id(),
                NamedElementOrSubtype::RequirementSpec(val) => val.id(),
                NamedElementOrSubtype::SamplingStrategySpec(val) => val.id(),
                NamedElementOrSubtype::PluginSpec(val) => val.id(),
                NamedElementOrSubtype::HookPayloadSpec(val) => val.id(),
                NamedElementOrSubtype::TelemetryMetricSpec(val) => val.id(),
                NamedElementOrSubtype::CliCommandSpec(val) => val.id(),
                NamedElementOrSubtype::ApiModelSpec(val) => val.id(),

        }
    }
        fn name<'a>(&'a self) -> &'a str {
        match self {
                NamedElementOrSubtype::RepositoryCatalog(val) => val.name(),
                NamedElementOrSubtype::PythonPackage(val) => val.name(),
                NamedElementOrSubtype::ModelElement(val) => val.name(),
                NamedElementOrSubtype::ApiFieldSpec(val) => val.name(),
                NamedElementOrSubtype::MethodSpec(val) => val.name(),
                NamedElementOrSubtype::ModelIdentifierSpec(val) => val.name(),
                NamedElementOrSubtype::IntrinsicAdapterSpec(val) => val.name(),
                NamedElementOrSubtype::BackendSpec(val) => val.name(),
                NamedElementOrSubtype::FormatterSpec(val) => val.name(),
                NamedElementOrSubtype::ContextSpec(val) => val.name(),
                NamedElementOrSubtype::SessionSpec(val) => val.name(),
                NamedElementOrSubtype::ComponentSpec(val) => val.name(),
                NamedElementOrSubtype::RequirementSpec(val) => val.name(),
                NamedElementOrSubtype::SamplingStrategySpec(val) => val.name(),
                NamedElementOrSubtype::PluginSpec(val) => val.name(),
                NamedElementOrSubtype::HookPayloadSpec(val) => val.name(),
                NamedElementOrSubtype::TelemetryMetricSpec(val) => val.name(),
                NamedElementOrSubtype::CliCommandSpec(val) => val.name(),
                NamedElementOrSubtype::ApiModelSpec(val) => val.name(),

        }
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        match self {
                NamedElementOrSubtype::RepositoryCatalog(val) => val.description(),
                NamedElementOrSubtype::PythonPackage(val) => val.description(),
                NamedElementOrSubtype::ModelElement(val) => val.description(),
                NamedElementOrSubtype::ApiFieldSpec(val) => val.description(),
                NamedElementOrSubtype::MethodSpec(val) => val.description(),
                NamedElementOrSubtype::ModelIdentifierSpec(val) => val.description(),
                NamedElementOrSubtype::IntrinsicAdapterSpec(val) => val.description(),
                NamedElementOrSubtype::BackendSpec(val) => val.description(),
                NamedElementOrSubtype::FormatterSpec(val) => val.description(),
                NamedElementOrSubtype::ContextSpec(val) => val.description(),
                NamedElementOrSubtype::SessionSpec(val) => val.description(),
                NamedElementOrSubtype::ComponentSpec(val) => val.description(),
                NamedElementOrSubtype::RequirementSpec(val) => val.description(),
                NamedElementOrSubtype::SamplingStrategySpec(val) => val.description(),
                NamedElementOrSubtype::PluginSpec(val) => val.description(),
                NamedElementOrSubtype::HookPayloadSpec(val) => val.description(),
                NamedElementOrSubtype::TelemetryMetricSpec(val) => val.description(),
                NamedElementOrSubtype::CliCommandSpec(val) => val.description(),
                NamedElementOrSubtype::ApiModelSpec(val) => val.description(),

        }
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        match self {
                NamedElementOrSubtype::RepositoryCatalog(val) => val.module_path(),
                NamedElementOrSubtype::PythonPackage(val) => val.module_path(),
                NamedElementOrSubtype::ModelElement(val) => val.module_path(),
                NamedElementOrSubtype::ApiFieldSpec(val) => val.module_path(),
                NamedElementOrSubtype::MethodSpec(val) => val.module_path(),
                NamedElementOrSubtype::ModelIdentifierSpec(val) => val.module_path(),
                NamedElementOrSubtype::IntrinsicAdapterSpec(val) => val.module_path(),
                NamedElementOrSubtype::BackendSpec(val) => val.module_path(),
                NamedElementOrSubtype::FormatterSpec(val) => val.module_path(),
                NamedElementOrSubtype::ContextSpec(val) => val.module_path(),
                NamedElementOrSubtype::SessionSpec(val) => val.module_path(),
                NamedElementOrSubtype::ComponentSpec(val) => val.module_path(),
                NamedElementOrSubtype::RequirementSpec(val) => val.module_path(),
                NamedElementOrSubtype::SamplingStrategySpec(val) => val.module_path(),
                NamedElementOrSubtype::PluginSpec(val) => val.module_path(),
                NamedElementOrSubtype::HookPayloadSpec(val) => val.module_path(),
                NamedElementOrSubtype::TelemetryMetricSpec(val) => val.module_path(),
                NamedElementOrSubtype::CliCommandSpec(val) => val.module_path(),
                NamedElementOrSubtype::ApiModelSpec(val) => val.module_path(),

        }
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        match self {
                NamedElementOrSubtype::RepositoryCatalog(val) => val.source_file(),
                NamedElementOrSubtype::PythonPackage(val) => val.source_file(),
                NamedElementOrSubtype::ModelElement(val) => val.source_file(),
                NamedElementOrSubtype::ApiFieldSpec(val) => val.source_file(),
                NamedElementOrSubtype::MethodSpec(val) => val.source_file(),
                NamedElementOrSubtype::ModelIdentifierSpec(val) => val.source_file(),
                NamedElementOrSubtype::IntrinsicAdapterSpec(val) => val.source_file(),
                NamedElementOrSubtype::BackendSpec(val) => val.source_file(),
                NamedElementOrSubtype::FormatterSpec(val) => val.source_file(),
                NamedElementOrSubtype::ContextSpec(val) => val.source_file(),
                NamedElementOrSubtype::SessionSpec(val) => val.source_file(),
                NamedElementOrSubtype::ComponentSpec(val) => val.source_file(),
                NamedElementOrSubtype::RequirementSpec(val) => val.source_file(),
                NamedElementOrSubtype::SamplingStrategySpec(val) => val.source_file(),
                NamedElementOrSubtype::PluginSpec(val) => val.source_file(),
                NamedElementOrSubtype::HookPayloadSpec(val) => val.source_file(),
                NamedElementOrSubtype::TelemetryMetricSpec(val) => val.source_file(),
                NamedElementOrSubtype::CliCommandSpec(val) => val.source_file(),
                NamedElementOrSubtype::ApiModelSpec(val) => val.source_file(),

        }
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        match self {
                NamedElementOrSubtype::RepositoryCatalog(val) => val.package_kind(),
                NamedElementOrSubtype::PythonPackage(val) => val.package_kind(),
                NamedElementOrSubtype::ModelElement(val) => val.package_kind(),
                NamedElementOrSubtype::ApiFieldSpec(val) => val.package_kind(),
                NamedElementOrSubtype::MethodSpec(val) => val.package_kind(),
                NamedElementOrSubtype::ModelIdentifierSpec(val) => val.package_kind(),
                NamedElementOrSubtype::IntrinsicAdapterSpec(val) => val.package_kind(),
                NamedElementOrSubtype::BackendSpec(val) => val.package_kind(),
                NamedElementOrSubtype::FormatterSpec(val) => val.package_kind(),
                NamedElementOrSubtype::ContextSpec(val) => val.package_kind(),
                NamedElementOrSubtype::SessionSpec(val) => val.package_kind(),
                NamedElementOrSubtype::ComponentSpec(val) => val.package_kind(),
                NamedElementOrSubtype::RequirementSpec(val) => val.package_kind(),
                NamedElementOrSubtype::SamplingStrategySpec(val) => val.package_kind(),
                NamedElementOrSubtype::PluginSpec(val) => val.package_kind(),
                NamedElementOrSubtype::HookPayloadSpec(val) => val.package_kind(),
                NamedElementOrSubtype::TelemetryMetricSpec(val) => val.package_kind(),
                NamedElementOrSubtype::CliCommandSpec(val) => val.package_kind(),
                NamedElementOrSubtype::ApiModelSpec(val) => val.package_kind(),

        }
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        match self {
                NamedElementOrSubtype::RepositoryCatalog(val) => val.element_kind(),
                NamedElementOrSubtype::PythonPackage(val) => val.element_kind(),
                NamedElementOrSubtype::ModelElement(val) => val.element_kind(),
                NamedElementOrSubtype::ApiFieldSpec(val) => val.element_kind(),
                NamedElementOrSubtype::MethodSpec(val) => val.element_kind(),
                NamedElementOrSubtype::ModelIdentifierSpec(val) => val.element_kind(),
                NamedElementOrSubtype::IntrinsicAdapterSpec(val) => val.element_kind(),
                NamedElementOrSubtype::BackendSpec(val) => val.element_kind(),
                NamedElementOrSubtype::FormatterSpec(val) => val.element_kind(),
                NamedElementOrSubtype::ContextSpec(val) => val.element_kind(),
                NamedElementOrSubtype::SessionSpec(val) => val.element_kind(),
                NamedElementOrSubtype::ComponentSpec(val) => val.element_kind(),
                NamedElementOrSubtype::RequirementSpec(val) => val.element_kind(),
                NamedElementOrSubtype::SamplingStrategySpec(val) => val.element_kind(),
                NamedElementOrSubtype::PluginSpec(val) => val.element_kind(),
                NamedElementOrSubtype::HookPayloadSpec(val) => val.element_kind(),
                NamedElementOrSubtype::TelemetryMetricSpec(val) => val.element_kind(),
                NamedElementOrSubtype::CliCommandSpec(val) => val.element_kind(),
                NamedElementOrSubtype::ApiModelSpec(val) => val.element_kind(),

        }
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        match self {
                NamedElementOrSubtype::RepositoryCatalog(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::PythonPackage(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::ModelElement(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::ApiFieldSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::MethodSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::ModelIdentifierSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::IntrinsicAdapterSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::BackendSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::FormatterSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::ContextSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::SessionSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::ComponentSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::RequirementSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::SamplingStrategySpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::PluginSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::HookPayloadSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::TelemetryMetricSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::CliCommandSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                NamedElementOrSubtype::ApiModelSpec(val) => val.coverage_scope().map(|x| x.to_any()),

        }
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        match self {
                NamedElementOrSubtype::RepositoryCatalog(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::PythonPackage(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::ModelElement(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::ApiFieldSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::MethodSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::ModelIdentifierSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::IntrinsicAdapterSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::BackendSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::FormatterSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::ContextSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::SessionSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::ComponentSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::RequirementSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::SamplingStrategySpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::PluginSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::HookPayloadSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::TelemetryMetricSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::CliCommandSpec(val) => val.tags().map(|x| x.to_any()),
                NamedElementOrSubtype::ApiModelSpec(val) => val.tags().map(|x| x.to_any()),

        }
    }
}
impl NamedElement for crate::ModelElementOrSubtype {
        fn id<'a>(&'a self) -> &'a crate::uriorcurie {
        match self {
                ModelElementOrSubtype::BackendSpec(val) => val.id(),
                ModelElementOrSubtype::FormatterSpec(val) => val.id(),
                ModelElementOrSubtype::ContextSpec(val) => val.id(),
                ModelElementOrSubtype::SessionSpec(val) => val.id(),
                ModelElementOrSubtype::ComponentSpec(val) => val.id(),
                ModelElementOrSubtype::RequirementSpec(val) => val.id(),
                ModelElementOrSubtype::SamplingStrategySpec(val) => val.id(),
                ModelElementOrSubtype::PluginSpec(val) => val.id(),
                ModelElementOrSubtype::HookPayloadSpec(val) => val.id(),
                ModelElementOrSubtype::TelemetryMetricSpec(val) => val.id(),
                ModelElementOrSubtype::CliCommandSpec(val) => val.id(),
                ModelElementOrSubtype::ApiModelSpec(val) => val.id(),

        }
    }
        fn name<'a>(&'a self) -> &'a str {
        match self {
                ModelElementOrSubtype::BackendSpec(val) => val.name(),
                ModelElementOrSubtype::FormatterSpec(val) => val.name(),
                ModelElementOrSubtype::ContextSpec(val) => val.name(),
                ModelElementOrSubtype::SessionSpec(val) => val.name(),
                ModelElementOrSubtype::ComponentSpec(val) => val.name(),
                ModelElementOrSubtype::RequirementSpec(val) => val.name(),
                ModelElementOrSubtype::SamplingStrategySpec(val) => val.name(),
                ModelElementOrSubtype::PluginSpec(val) => val.name(),
                ModelElementOrSubtype::HookPayloadSpec(val) => val.name(),
                ModelElementOrSubtype::TelemetryMetricSpec(val) => val.name(),
                ModelElementOrSubtype::CliCommandSpec(val) => val.name(),
                ModelElementOrSubtype::ApiModelSpec(val) => val.name(),

        }
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        match self {
                ModelElementOrSubtype::BackendSpec(val) => val.description(),
                ModelElementOrSubtype::FormatterSpec(val) => val.description(),
                ModelElementOrSubtype::ContextSpec(val) => val.description(),
                ModelElementOrSubtype::SessionSpec(val) => val.description(),
                ModelElementOrSubtype::ComponentSpec(val) => val.description(),
                ModelElementOrSubtype::RequirementSpec(val) => val.description(),
                ModelElementOrSubtype::SamplingStrategySpec(val) => val.description(),
                ModelElementOrSubtype::PluginSpec(val) => val.description(),
                ModelElementOrSubtype::HookPayloadSpec(val) => val.description(),
                ModelElementOrSubtype::TelemetryMetricSpec(val) => val.description(),
                ModelElementOrSubtype::CliCommandSpec(val) => val.description(),
                ModelElementOrSubtype::ApiModelSpec(val) => val.description(),

        }
    }
        fn module_path<'a>(&'a self) -> Option<&'a str> {
        match self {
                ModelElementOrSubtype::BackendSpec(val) => val.module_path(),
                ModelElementOrSubtype::FormatterSpec(val) => val.module_path(),
                ModelElementOrSubtype::ContextSpec(val) => val.module_path(),
                ModelElementOrSubtype::SessionSpec(val) => val.module_path(),
                ModelElementOrSubtype::ComponentSpec(val) => val.module_path(),
                ModelElementOrSubtype::RequirementSpec(val) => val.module_path(),
                ModelElementOrSubtype::SamplingStrategySpec(val) => val.module_path(),
                ModelElementOrSubtype::PluginSpec(val) => val.module_path(),
                ModelElementOrSubtype::HookPayloadSpec(val) => val.module_path(),
                ModelElementOrSubtype::TelemetryMetricSpec(val) => val.module_path(),
                ModelElementOrSubtype::CliCommandSpec(val) => val.module_path(),
                ModelElementOrSubtype::ApiModelSpec(val) => val.module_path(),

        }
    }
        fn source_file<'a>(&'a self) -> Option<&'a str> {
        match self {
                ModelElementOrSubtype::BackendSpec(val) => val.source_file(),
                ModelElementOrSubtype::FormatterSpec(val) => val.source_file(),
                ModelElementOrSubtype::ContextSpec(val) => val.source_file(),
                ModelElementOrSubtype::SessionSpec(val) => val.source_file(),
                ModelElementOrSubtype::ComponentSpec(val) => val.source_file(),
                ModelElementOrSubtype::RequirementSpec(val) => val.source_file(),
                ModelElementOrSubtype::SamplingStrategySpec(val) => val.source_file(),
                ModelElementOrSubtype::PluginSpec(val) => val.source_file(),
                ModelElementOrSubtype::HookPayloadSpec(val) => val.source_file(),
                ModelElementOrSubtype::TelemetryMetricSpec(val) => val.source_file(),
                ModelElementOrSubtype::CliCommandSpec(val) => val.source_file(),
                ModelElementOrSubtype::ApiModelSpec(val) => val.source_file(),

        }
    }
        fn package_kind<'a>(&'a self) -> Option<&'a crate::PackageKindEnum> {
        match self {
                ModelElementOrSubtype::BackendSpec(val) => val.package_kind(),
                ModelElementOrSubtype::FormatterSpec(val) => val.package_kind(),
                ModelElementOrSubtype::ContextSpec(val) => val.package_kind(),
                ModelElementOrSubtype::SessionSpec(val) => val.package_kind(),
                ModelElementOrSubtype::ComponentSpec(val) => val.package_kind(),
                ModelElementOrSubtype::RequirementSpec(val) => val.package_kind(),
                ModelElementOrSubtype::SamplingStrategySpec(val) => val.package_kind(),
                ModelElementOrSubtype::PluginSpec(val) => val.package_kind(),
                ModelElementOrSubtype::HookPayloadSpec(val) => val.package_kind(),
                ModelElementOrSubtype::TelemetryMetricSpec(val) => val.package_kind(),
                ModelElementOrSubtype::CliCommandSpec(val) => val.package_kind(),
                ModelElementOrSubtype::ApiModelSpec(val) => val.package_kind(),

        }
    }
        fn element_kind<'a>(&'a self) -> Option<&'a crate::ElementKindEnum> {
        match self {
                ModelElementOrSubtype::BackendSpec(val) => val.element_kind(),
                ModelElementOrSubtype::FormatterSpec(val) => val.element_kind(),
                ModelElementOrSubtype::ContextSpec(val) => val.element_kind(),
                ModelElementOrSubtype::SessionSpec(val) => val.element_kind(),
                ModelElementOrSubtype::ComponentSpec(val) => val.element_kind(),
                ModelElementOrSubtype::RequirementSpec(val) => val.element_kind(),
                ModelElementOrSubtype::SamplingStrategySpec(val) => val.element_kind(),
                ModelElementOrSubtype::PluginSpec(val) => val.element_kind(),
                ModelElementOrSubtype::HookPayloadSpec(val) => val.element_kind(),
                ModelElementOrSubtype::TelemetryMetricSpec(val) => val.element_kind(),
                ModelElementOrSubtype::CliCommandSpec(val) => val.element_kind(),
                ModelElementOrSubtype::ApiModelSpec(val) => val.element_kind(),

        }
    }
        fn coverage_scope<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CoverageScopeEnum>> {
        match self {
                ModelElementOrSubtype::BackendSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                ModelElementOrSubtype::FormatterSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                ModelElementOrSubtype::ContextSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                ModelElementOrSubtype::SessionSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                ModelElementOrSubtype::ComponentSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                ModelElementOrSubtype::RequirementSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                ModelElementOrSubtype::SamplingStrategySpec(val) => val.coverage_scope().map(|x| x.to_any()),
                ModelElementOrSubtype::PluginSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                ModelElementOrSubtype::HookPayloadSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                ModelElementOrSubtype::TelemetryMetricSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                ModelElementOrSubtype::CliCommandSpec(val) => val.coverage_scope().map(|x| x.to_any()),
                ModelElementOrSubtype::ApiModelSpec(val) => val.coverage_scope().map(|x| x.to_any()),

        }
    }
        fn tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        match self {
                ModelElementOrSubtype::BackendSpec(val) => val.tags().map(|x| x.to_any()),
                ModelElementOrSubtype::FormatterSpec(val) => val.tags().map(|x| x.to_any()),
                ModelElementOrSubtype::ContextSpec(val) => val.tags().map(|x| x.to_any()),
                ModelElementOrSubtype::SessionSpec(val) => val.tags().map(|x| x.to_any()),
                ModelElementOrSubtype::ComponentSpec(val) => val.tags().map(|x| x.to_any()),
                ModelElementOrSubtype::RequirementSpec(val) => val.tags().map(|x| x.to_any()),
                ModelElementOrSubtype::SamplingStrategySpec(val) => val.tags().map(|x| x.to_any()),
                ModelElementOrSubtype::PluginSpec(val) => val.tags().map(|x| x.to_any()),
                ModelElementOrSubtype::HookPayloadSpec(val) => val.tags().map(|x| x.to_any()),
                ModelElementOrSubtype::TelemetryMetricSpec(val) => val.tags().map(|x| x.to_any()),
                ModelElementOrSubtype::CliCommandSpec(val) => val.tags().map(|x| x.to_any()),
                ModelElementOrSubtype::ApiModelSpec(val) => val.tags().map(|x| x.to_any()),

        }
    }
}

pub trait RepositoryCatalog : NamedElement   {

    fn repository_root<'a>(&'a self) -> Option<&'a str>;
    // fn repository_root_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_repository_root(&mut self, value: Option<&'a str>);

    fn analyzed_on<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn analyzed_on_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_analyzed_on(&mut self, value: Option<&'a NaiveDate>);

    fn includes_path<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn includes_path_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_includes_path(&mut self, value: Option<&Vec<String>>);

    fn excludes_path<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn excludes_path_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_excludes_path(&mut self, value: Option<&Vec<String>>);

    fn declares_element<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, ModelElementOrSubtype>>;
    // fn declares_element_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, ModelElementOrSubtype>>;
    // fn set_declares_element<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ModelElement>;


}

impl RepositoryCatalog for crate::RepositoryCatalog {
        fn repository_root<'a>(&'a self) -> Option<&'a str> {
        return self.repository_root.as_deref();
    }
        fn analyzed_on<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.analyzed_on.as_ref();
    }
        fn includes_path<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.includes_path.as_ref();
    }
        fn excludes_path<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.excludes_path.as_ref();
    }
        fn declares_element<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, ModelElementOrSubtype>> {
        return self.declares_element.as_ref();
    }
}


pub trait PythonPackage : NamedElement   {

    fn package_name<'a>(&'a self) -> Option<&'a str>;
    // fn package_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_package_name(&mut self, value: Option<&'a str>);

    fn depends_on_package<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PythonPackage>>;
    // fn depends_on_package_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PythonPackage>>;
    // fn set_depends_on_package<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PythonPackage>;

    fn declares_element<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, ModelElementOrSubtype>>;
    // fn declares_element_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, ModelElementOrSubtype>>;
    // fn set_declares_element<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ModelElement>;


}

impl PythonPackage for crate::PythonPackage {
        fn package_name<'a>(&'a self) -> Option<&'a str> {
        return self.package_name.as_deref();
    }
        fn depends_on_package<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PythonPackage>> {
        return self.depends_on_package.as_ref().map(|x| poly_containers::ListView::new(x));
    }
        fn declares_element<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, ModelElementOrSubtype>> {
        return self.declares_element.as_ref();
    }
}


pub trait ModelElement : NamedElement   {


}

impl ModelElement for crate::ModelElement {
}
impl ModelElement for crate::BackendSpec {
}
impl ModelElement for crate::FormatterSpec {
}
impl ModelElement for crate::ContextSpec {
}
impl ModelElement for crate::SessionSpec {
}
impl ModelElement for crate::ComponentSpec {
}
impl ModelElement for crate::RequirementSpec {
}
impl ModelElement for crate::SamplingStrategySpec {
}
impl ModelElement for crate::PluginSpec {
}
impl ModelElement for crate::HookPayloadSpec {
}
impl ModelElement for crate::TelemetryMetricSpec {
}
impl ModelElement for crate::CliCommandSpec {
}
impl ModelElement for crate::ApiModelSpec {
}

impl ModelElement for crate::ModelElementOrSubtype {
}

pub trait BackendSpec : ModelElement   {

    fn backend_family<'a>(&'a self) -> Option<&'a crate::BackendFamilyEnum>;
    // fn backend_family_mut(&mut self) -> &mut Option<&'a crate::BackendFamilyEnum>;
    // fn set_backend_family(&mut self, value: Option<&'a BackendFamilyEnum>);

    fn model_identifier<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ModelIdentifierSpec>>;
    // fn model_identifier_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ModelIdentifierSpec>>;
    // fn set_model_identifier<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ModelIdentifierSpec>;

    fn default_formatter<'a>(&'a self) -> Option<&'a str>;
    // fn default_formatter_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_default_formatter<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn model_options_key<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn model_options_key_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_model_options_key(&mut self, value: Option<&Vec<String>>);

    fn supports_streaming(&self) -> Option<bool>;
    // fn supports_streaming_mut(&mut self) -> &mut Option<bool>;
    // fn set_supports_streaming(&mut self, value: Option<bool>);

    fn supports_tool_calls(&self) -> Option<bool>;
    // fn supports_tool_calls_mut(&mut self) -> &mut Option<bool>;
    // fn set_supports_tool_calls(&mut self, value: Option<bool>);

    fn supports_multimodal(&self) -> Option<bool>;
    // fn supports_multimodal_mut(&mut self) -> &mut Option<bool>;
    // fn set_supports_multimodal(&mut self, value: Option<bool>);


}

impl BackendSpec for crate::BackendSpec {
        fn backend_family<'a>(&'a self) -> Option<&'a crate::BackendFamilyEnum> {
        return self.backend_family.as_ref();
    }
        fn model_identifier<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ModelIdentifierSpec>> {
        return self.model_identifier.as_ref();
    }
        fn default_formatter<'a>(&'a self) -> Option<&'a str> {
        return self.default_formatter.as_deref();
    }
        fn model_options_key<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.model_options_key.as_ref();
    }
        fn supports_streaming(&self) -> Option<bool> {
        return self.supports_streaming;
    }
        fn supports_tool_calls(&self) -> Option<bool> {
        return self.supports_tool_calls;
    }
        fn supports_multimodal(&self) -> Option<bool> {
        return self.supports_multimodal;
    }
}


pub trait FormatterSpec : ModelElement   {


}

impl FormatterSpec for crate::FormatterSpec {
}


pub trait ContextSpec : ModelElement   {

    fn context_linearity<'a>(&'a self) -> Option<&'a crate::ContextLinearityEnum>;
    // fn context_linearity_mut(&mut self) -> &mut Option<&'a crate::ContextLinearityEnum>;
    // fn set_context_linearity(&mut self, value: Option<&'a ContextLinearityEnum>);

    fn stores_component_history(&self) -> Option<bool>;
    // fn stores_component_history_mut(&mut self) -> &mut Option<bool>;
    // fn set_stores_component_history(&mut self, value: Option<bool>);

    fn accepts_message_attachments(&self) -> Option<bool>;
    // fn accepts_message_attachments_mut(&mut self) -> &mut Option<bool>;
    // fn set_accepts_message_attachments(&mut self, value: Option<bool>);


}

impl ContextSpec for crate::ContextSpec {
        fn context_linearity<'a>(&'a self) -> Option<&'a crate::ContextLinearityEnum> {
        return self.context_linearity.as_ref();
    }
        fn stores_component_history(&self) -> Option<bool> {
        return self.stores_component_history;
    }
        fn accepts_message_attachments(&self) -> Option<bool> {
        return self.accepts_message_attachments;
    }
}


pub trait SessionSpec : ModelElement   {

    fn uses_backend<'a>(&'a self) -> Option<&'a str>;
    // fn uses_backend_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_uses_backend<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn uses_context<'a>(&'a self) -> Option<&'a str>;
    // fn uses_context_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_uses_context<E>(&mut self, value: Option<&'a str>) where E: Into<String>;

    fn exposed_method<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::MethodSpec>>;
    // fn exposed_method_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::MethodSpec>>;
    // fn set_exposed_method<E>(&mut self, value: Option<&Vec<E>>) where E: Into<MethodSpec>;


}

impl SessionSpec for crate::SessionSpec {
        fn uses_backend<'a>(&'a self) -> Option<&'a str> {
        return self.uses_backend.as_deref();
    }
        fn uses_context<'a>(&'a self) -> Option<&'a str> {
        return self.uses_context.as_deref();
    }
        fn exposed_method<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::MethodSpec>> {
        return self.exposed_method.as_ref();
    }
}


pub trait ComponentSpec : ModelElement   {

    fn component_category<'a>(&'a self) -> Option<&'a crate::ComponentCategoryEnum>;
    // fn component_category_mut(&mut self) -> &mut Option<&'a crate::ComponentCategoryEnum>;
    // fn set_component_category(&mut self, value: Option<&'a ComponentCategoryEnum>);

    fn input_modality<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn input_modality_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_input_modality(&mut self, value: Option<&Vec<String>>);

    fn parsed_output_type<'a>(&'a self) -> Option<&'a str>;
    // fn parsed_output_type_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_parsed_output_type(&mut self, value: Option<&'a str>);


}

impl ComponentSpec for crate::ComponentSpec {
        fn component_category<'a>(&'a self) -> Option<&'a crate::ComponentCategoryEnum> {
        return self.component_category.as_ref();
    }
        fn input_modality<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.input_modality.as_ref();
    }
        fn parsed_output_type<'a>(&'a self) -> Option<&'a str> {
        return self.parsed_output_type.as_deref();
    }
}


pub trait RequirementSpec : ModelElement   {

    fn validation_style<'a>(&'a self) -> Option<&'a str>;
    // fn validation_style_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_validation_style(&mut self, value: Option<&'a str>);

    fn may_trigger_repair(&self) -> Option<bool>;
    // fn may_trigger_repair_mut(&mut self) -> &mut Option<bool>;
    // fn set_may_trigger_repair(&mut self, value: Option<bool>);


}

impl RequirementSpec for crate::RequirementSpec {
        fn validation_style<'a>(&'a self) -> Option<&'a str> {
        return self.validation_style.as_deref();
    }
        fn may_trigger_repair(&self) -> Option<bool> {
        return self.may_trigger_repair;
    }
}


pub trait SamplingStrategySpec : ModelElement   {

    fn selection_policy<'a>(&'a self) -> Option<&'a str>;
    // fn selection_policy_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_selection_policy(&mut self, value: Option<&'a str>);

    fn loop_budget_hint(&self) -> Option<isize>;
    // fn loop_budget_hint_mut(&mut self) -> &mut Option<isize>;
    // fn set_loop_budget_hint(&mut self, value: Option<isize>);

    fn may_trigger_repair(&self) -> Option<bool>;
    // fn may_trigger_repair_mut(&mut self) -> &mut Option<bool>;
    // fn set_may_trigger_repair(&mut self, value: Option<bool>);


}

impl SamplingStrategySpec for crate::SamplingStrategySpec {
        fn selection_policy<'a>(&'a self) -> Option<&'a str> {
        return self.selection_policy.as_deref();
    }
        fn loop_budget_hint(&self) -> Option<isize> {
        return self.loop_budget_hint;
    }
        fn may_trigger_repair(&self) -> Option<bool> {
        return self.may_trigger_repair;
    }
}


pub trait PluginSpec : ModelElement   {

    fn plugin_mode<'a>(&'a self) -> Option<&'a crate::PluginModeEnum>;
    // fn plugin_mode_mut(&mut self) -> &mut Option<&'a crate::PluginModeEnum>;
    // fn set_plugin_mode(&mut self, value: Option<&'a PluginModeEnum>);

    fn hook_type<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::HookTypeEnum>>;
    // fn hook_type_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::HookTypeEnum>>;
    // fn set_hook_type(&mut self, value: Option<&Vec<HookTypeEnum>>);

    fn payload_model<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::HookPayloadSpec>>;
    // fn payload_model_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::HookPayloadSpec>>;
    // fn set_payload_model<E>(&mut self, value: Option<&Vec<E>>) where E: Into<HookPayloadSpec>;

    fn plugin_priority(&self) -> Option<isize>;
    // fn plugin_priority_mut(&mut self) -> &mut Option<isize>;
    // fn set_plugin_priority(&mut self, value: Option<isize>);


}

impl PluginSpec for crate::PluginSpec {
        fn plugin_mode<'a>(&'a self) -> Option<&'a crate::PluginModeEnum> {
        return self.plugin_mode.as_ref();
    }
        fn hook_type<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::HookTypeEnum>> {
        return self.hook_type.as_ref();
    }
        fn payload_model<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::HookPayloadSpec>> {
        return self.payload_model.as_ref();
    }
        fn plugin_priority(&self) -> Option<isize> {
        return self.plugin_priority;
    }
}


pub trait HookPayloadSpec : ModelElement   {

    fn hook_type<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::HookTypeEnum>>;
    // fn hook_type_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::HookTypeEnum>>;
    // fn set_hook_type(&mut self, value: Option<&Vec<HookTypeEnum>>);

    fn lifecycle_role<'a>(&'a self) -> Option<&'a str>;
    // fn lifecycle_role_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_lifecycle_role(&mut self, value: Option<&'a str>);


}

impl HookPayloadSpec for crate::HookPayloadSpec {
        fn hook_type<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::HookTypeEnum>> {
        return self.hook_type.as_ref();
    }
        fn lifecycle_role<'a>(&'a self) -> Option<&'a str> {
        return self.lifecycle_role.as_deref();
    }
}


pub trait TelemetryMetricSpec : ModelElement   {

    fn metric_name<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn metric_name_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_metric_name(&mut self, value: Option<&Vec<String>>);


}

impl TelemetryMetricSpec for crate::TelemetryMetricSpec {
        fn metric_name<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.metric_name.as_ref();
    }
}


pub trait CliCommandSpec : ModelElement   {

    fn command_group<'a>(&'a self) -> Option<&'a str>;
    // fn command_group_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_command_group(&mut self, value: Option<&'a str>);

    fn command_path<'a>(&'a self) -> Option<&'a str>;
    // fn command_path_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_command_path(&mut self, value: Option<&'a str>);

    fn command_purpose<'a>(&'a self) -> Option<&'a str>;
    // fn command_purpose_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_command_purpose(&mut self, value: Option<&'a str>);

    fn input_model<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApiModelSpec>>;
    // fn input_model_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ApiModelSpec>>;
    // fn set_input_model<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ApiModelSpec>;

    fn output_model<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApiModelSpec>>;
    // fn output_model_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ApiModelSpec>>;
    // fn set_output_model<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ApiModelSpec>;


}

impl CliCommandSpec for crate::CliCommandSpec {
        fn command_group<'a>(&'a self) -> Option<&'a str> {
        return self.command_group.as_deref();
    }
        fn command_path<'a>(&'a self) -> Option<&'a str> {
        return self.command_path.as_deref();
    }
        fn command_purpose<'a>(&'a self) -> Option<&'a str> {
        return self.command_purpose.as_deref();
    }
        fn input_model<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApiModelSpec>> {
        return self.input_model.as_ref();
    }
        fn output_model<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApiModelSpec>> {
        return self.output_model.as_ref();
    }
}


pub trait ApiModelSpec : ModelElement   {

    fn request_or_response<'a>(&'a self) -> Option<&'a crate::RequestResponseEnum>;
    // fn request_or_response_mut(&mut self) -> &mut Option<&'a crate::RequestResponseEnum>;
    // fn set_request_or_response(&mut self, value: Option<&'a RequestResponseEnum>);

    fn openai_object_type<'a>(&'a self) -> Option<&'a str>;
    // fn openai_object_type_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_openai_object_type(&mut self, value: Option<&'a str>);

    fn has_field<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApiFieldSpec>>;
    // fn has_field_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ApiFieldSpec>>;
    // fn set_has_field<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ApiFieldSpec>;


}

impl ApiModelSpec for crate::ApiModelSpec {
        fn request_or_response<'a>(&'a self) -> Option<&'a crate::RequestResponseEnum> {
        return self.request_or_response.as_ref();
    }
        fn openai_object_type<'a>(&'a self) -> Option<&'a str> {
        return self.openai_object_type.as_deref();
    }
        fn has_field<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApiFieldSpec>> {
        return self.has_field.as_ref();
    }
}


pub trait ApiFieldSpec : NamedElement   {

    fn field_name<'a>(&'a self) -> Option<&'a str>;
    // fn field_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_field_name(&mut self, value: Option<&'a str>);

    fn field_type<'a>(&'a self) -> Option<&'a str>;
    // fn field_type_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_field_type(&mut self, value: Option<&'a str>);

    fn required_field(&self) -> Option<bool>;
    // fn required_field_mut(&mut self) -> &mut Option<bool>;
    // fn set_required_field(&mut self, value: Option<bool>);

    fn allows_null(&self) -> Option<bool>;
    // fn allows_null_mut(&mut self) -> &mut Option<bool>;
    // fn set_allows_null(&mut self, value: Option<bool>);


}

impl ApiFieldSpec for crate::ApiFieldSpec {
        fn field_name<'a>(&'a self) -> Option<&'a str> {
        return self.field_name.as_deref();
    }
        fn field_type<'a>(&'a self) -> Option<&'a str> {
        return self.field_type.as_deref();
    }
        fn required_field(&self) -> Option<bool> {
        return self.required_field;
    }
        fn allows_null(&self) -> Option<bool> {
        return self.allows_null;
    }
}


pub trait MethodSpec : NamedElement   {

    fn method_name<'a>(&'a self) -> Option<&'a str>;
    // fn method_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_method_name(&mut self, value: Option<&'a str>);

    fn method_signature<'a>(&'a self) -> Option<&'a str>;
    // fn method_signature_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_method_signature(&mut self, value: Option<&'a str>);

    fn lifecycle_role<'a>(&'a self) -> Option<&'a str>;
    // fn lifecycle_role_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_lifecycle_role(&mut self, value: Option<&'a str>);


}

impl MethodSpec for crate::MethodSpec {
        fn method_name<'a>(&'a self) -> Option<&'a str> {
        return self.method_name.as_deref();
    }
        fn method_signature<'a>(&'a self) -> Option<&'a str> {
        return self.method_signature.as_deref();
    }
        fn lifecycle_role<'a>(&'a self) -> Option<&'a str> {
        return self.lifecycle_role.as_deref();
    }
}


pub trait ModelIdentifierSpec : NamedElement   {

    fn hf_model_name<'a>(&'a self) -> Option<&'a str>;
    // fn hf_model_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_hf_model_name(&mut self, value: Option<&'a str>);

    fn ollama_name<'a>(&'a self) -> Option<&'a str>;
    // fn ollama_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_ollama_name(&mut self, value: Option<&'a str>);

    fn watsonx_name<'a>(&'a self) -> Option<&'a str>;
    // fn watsonx_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_watsonx_name(&mut self, value: Option<&'a str>);

    fn openai_name<'a>(&'a self) -> Option<&'a str>;
    // fn openai_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_openai_name(&mut self, value: Option<&'a str>);

    fn bedrock_name<'a>(&'a self) -> Option<&'a str>;
    // fn bedrock_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_bedrock_name(&mut self, value: Option<&'a str>);

    fn provider_name<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn provider_name_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_provider_name(&mut self, value: Option<&Vec<String>>);


}

impl ModelIdentifierSpec for crate::ModelIdentifierSpec {
        fn hf_model_name<'a>(&'a self) -> Option<&'a str> {
        return self.hf_model_name.as_deref();
    }
        fn ollama_name<'a>(&'a self) -> Option<&'a str> {
        return self.ollama_name.as_deref();
    }
        fn watsonx_name<'a>(&'a self) -> Option<&'a str> {
        return self.watsonx_name.as_deref();
    }
        fn openai_name<'a>(&'a self) -> Option<&'a str> {
        return self.openai_name.as_deref();
    }
        fn bedrock_name<'a>(&'a self) -> Option<&'a str> {
        return self.bedrock_name.as_deref();
    }
        fn provider_name<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.provider_name.as_ref();
    }
}


pub trait IntrinsicAdapterSpec : NamedElement   {

    fn repo_id<'a>(&'a self) -> Option<&'a str>;
    // fn repo_id_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_repo_id(&mut self, value: Option<&'a str>);

    fn adapter_type<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AdapterTypeEnum>>;
    // fn adapter_type_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AdapterTypeEnum>>;
    // fn set_adapter_type(&mut self, value: Option<&Vec<AdapterTypeEnum>>);


}

impl IntrinsicAdapterSpec for crate::IntrinsicAdapterSpec {
        fn repo_id<'a>(&'a self) -> Option<&'a str> {
        return self.repo_id.as_deref();
    }
        fn adapter_type<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AdapterTypeEnum>> {
        return self.adapter_type.as_ref();
    }
}
