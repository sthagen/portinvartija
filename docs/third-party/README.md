# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/portinvartija/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([3e6037b8 ...](https://git.sr.ht/~sthagen/portinvartija/blob/default/etc/sbom/cdx.json.sha256 "sha256:3e6037b80db8e57394e7692bfeecaa2882144609f7c82f787cd2d8a8d72a4437")).
<!--[[[end]]] (checksum: 9e3f183f2a1e0fac84473fffae8aa8f0)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                            | Version                                                | License     | Author             | Description (from packaging data)                                                                        |
|:----------------------------------------------------------------|:-------------------------------------------------------|:------------|:-------------------|:---------------------------------------------------------------------------------------------------------|
| [PyYAML](https://pyyaml.org/)                                   | [6.0.1](https://pypi.org/project/PyYAML/6.0.1/)        | MIT License | Kirill Simonov     | YAML parser and emitter for Python                                                                       |
| [first](http://github.com/hynek/first/)                         | [2.0.2](https://pypi.org/project/first/2.0.2/)         | MIT License | Hynek Schlawack    | Return the first true value of an iterable.                                                              |
| [jmespath](https://github.com/jmespath/jmespath.py)             | [1.0.1](https://pypi.org/project/jmespath/1.0.1/)      | MIT License | James Saryerwinnie | JSON Matching Expressions                                                                                |
| [jsonschema](https://github.com/python-jsonschema/jsonschema)   | [4.20.0](https://pypi.org/project/jsonschema/4.20.0/)  | MIT License | Julian Berman      | An implementation of JSON Schema validation for Python                                                   |
| [kdl-py](https://github.com/tabatkins/kdlpy/)                   | [1.1.6](https://pypi.org/project/kdl-py/1.1.6/)        | MIT License | Tab Atkins-Bittner | A parser for the KDL language.                                                                           |
| [lxml](https://lxml.de/)                                        | [5.0.1](https://pypi.org/project/lxml/5.0.1/)          | BSD License | lxml dev team      | Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.         |
| [msgspec](https://jcristharif.com/msgspec/)                     | [0.18.5](https://pypi.org/project/msgspec/0.18.5/)     | BSD License | Jim Crist-Harif    | A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML. |
| [referencing](https://github.com/python-jsonschema/referencing) | [0.32.1](https://pypi.org/project/referencing/0.32.1/) | MIT License | Julian Berman      | JSON Referencing + Python                                                                                |
| [toml](https://github.com/uiri/toml)                            | [0.10.2](https://pypi.org/project/toml/0.10.2/)        | MIT License | William Pearson    | Python Library for Tom's Obvious, Minimal Language                                                       |
| [typer](https://github.com/tiangolo/typer)                      | [0.9.0](https://pypi.org/project/typer/0.9.0/)         | MIT License | Sebastián Ramírez  | Typer, build great CLIs. Easy to code. Based on Python type hints.                                       |
| [xmlschema](https://github.com/sissaschool/xmlschema)           | [3.0.0](https://pypi.org/project/xmlschema/3.0.0/)     | MIT License | Davide Brunato     | An XML Schema validator and decoder                                                                      |
<!--[[[end]]] (checksum: 112a950b8f271bbf55ae13ed3553bd58)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                                        | Version                                                                  | License                            | Author                                                                                | Description (from packaging data)                                    |
|:--------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|:-----------------------------------|:--------------------------------------------------------------------------------------|:---------------------------------------------------------------------|
| [attrs](https://www.attrs.org/en/stable/changelog.html)                                     | [23.2.0](https://pypi.org/project/attrs/23.2.0/)                         | MIT License                        | Hynek Schlawack <hs@ox.cx>                                                            | Classes Without Boilerplate                                          |
| [click](https://palletsprojects.com/p/click/)                                               | [8.1.5](https://pypi.org/project/click/8.1.5/)                           | BSD License                        | Pallets <contact@palletsprojects.com>                                                 | Composable command line interface toolkit                            |
| [elementpath](https://github.com/sissaschool/elementpath)                                   | [4.1.5](https://pypi.org/project/elementpath/4.1.5/)                     | MIT License                        | Davide Brunato                                                                        | XPath 1.0/2.0/3.0/3.1 parsers and selectors for ElementTree and lxml |
| [jsonschema-specifications](https://github.com/python-jsonschema/jsonschema-specifications) | [2023.6.1](https://pypi.org/project/jsonschema-specifications/2023.6.1/) | MIT License                        | Julian Berman                                                                         | The JSON Schema meta-schemas and vocabularies, exposed as a Registry |
| [rpds-py](https://github.com/crate-py/rpds)                                                 | [0.9.2](https://pypi.org/project/rpds-py/0.9.2/)                         | MIT License                        | Julian Berman                                                                         | Python bindings to Rust's persistent data structures (rpds)          |
| [typing_extensions](https://github.com/python/typing_extensions)                            | [4.7.1](https://pypi.org/project/typing_extensions/4.7.1/)               | Python Software Foundation License | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com> | Backported and Experimental Type Hints for Python 3.7+               |
<!--[[[end]]] (checksum: 2e95bc819cc51e9f8ae09533817672cd)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
first==2.0.2
jmespath==1.0.1
jsonschema==4.20.0
├── attrs [required: >=22.2.0, installed: 23.2.0]
├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.6.1]
│   └── referencing [required: >=0.28.0, installed: 0.32.1]
│       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       └── rpds-py [required: >=0.7.0, installed: 0.9.2]
├── referencing [required: >=0.28.4, installed: 0.32.1]
│   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   └── rpds-py [required: >=0.7.0, installed: 0.9.2]
└── rpds-py [required: >=0.7.1, installed: 0.9.2]
kdl-py==1.1.6
lxml==5.0.1
msgspec==0.18.5
PyYAML==6.0.1
toml==0.10.2
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.5]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
xmlschema==3.0.0
└── elementpath [required: >=4.1.5,<5.0.0, installed: 4.1.5]
````
<!--[[[end]]] (checksum: b3e22ebdd7b3f244b93f79cf84c1b45c)-->
