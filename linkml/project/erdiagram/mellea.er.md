erDiagram
ModelElement {
    uriorcurie id  
    string name  
    string description  
    CoverageScopeEnumList coverage_scope  
    ElementKindEnum element_kind  
    PythonDottedPath module_path  
    PackageKindEnum package_kind  
    RepositoryRelativePath source_file  
    stringList tags  
}
RepositoryCatalog {
    date analyzed_on  
    RepositoryRelativePathList excludes_path  
    RepositoryRelativePathList includes_path  
    RepositoryRelativePath repository_root  
    uriorcurie id  
    string name  
    string description  
    CoverageScopeEnumList coverage_scope  
    ElementKindEnum element_kind  
    PythonDottedPath module_path  
    PackageKindEnum package_kind  
    RepositoryRelativePath source_file  
    stringList tags  
}

RepositoryCatalog ||--}o ModelElement : "declares_element"

