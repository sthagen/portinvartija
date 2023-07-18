# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/portinvartija/blob/default/sbom/cdx.json) with SHA256 checksum ([9fbcd422 ...](https://git.sr.ht/~sthagen/portinvartija/blob/default/sbom/cdx.json.sha256 "sha256:9fbcd422a3e4cdbf1bc33c8433c48f0554bc4ca1d4f88b26113f2fd076cceeac")).
<!--[[[end]]] (checksum: 2b61d946d222e1f60ee0aceed953b325)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                          | Version                                               | License     | Author             | Description (from packaging data)                                                                        |
|:--------------------------------------------------------------|:------------------------------------------------------|:------------|:-------------------|:---------------------------------------------------------------------------------------------------------|
| [PyYAML](https://pyyaml.org/)                                 | [6.0.1](https://pypi.org/project/PyYAML/6.0.1/)       | MIT License | Kirill Simonov     | YAML parser and emitter for Python                                                                       |
| [first](http://github.com/hynek/first/)                       | [2.0.2](https://pypi.org/project/first/2.0.2/)        | MIT License | Hynek Schlawack    | Return the first true value of an iterable.                                                              |
| [jmespath](https://github.com/jmespath/jmespath.py)           | [1.0.1](https://pypi.org/project/jmespath/1.0.1/)     | MIT License | James Saryerwinnie | JSON Matching Expressions                                                                                |
| [jsonschema](https://github.com/python-jsonschema/jsonschema) | [4.18.4](https://pypi.org/project/jsonschema/4.18.4/) | MIT License | Julian Berman      | An implementation of JSON Schema validation for Python                                                   |
| [lxml](https://lxml.de/)                                      | [4.9.3](https://pypi.org/project/lxml/4.9.3/)         | BSD License | lxml dev team      | Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.         |
| [msgspec](https://jcristharif.com/msgspec/)                   | [0.17.0](https://pypi.org/project/msgspec/0.17.0/)    | BSD License | Jim Crist-Harif    | A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML. |
| [toml](https://github.com/uiri/toml)                          | [0.10.2](https://pypi.org/project/toml/0.10.2/)       | MIT License | William Pearson    | Python Library for Tom's Obvious, Minimal Language                                                       |
| [typer](https://github.com/tiangolo/typer)                    | [0.9.0](https://pypi.org/project/typer/0.9.0/)        | MIT License | Sebastián Ramírez  | Typer, build great CLIs. Easy to code. Based on Python type hints.                                       |
| [xmlschema](https://github.com/sissaschool/xmlschema)         | [2.3.1](https://pypi.org/project/xmlschema/2.3.1/)    | MIT License | Davide Brunato     | An XML Schema validator and decoder                                                                      |
<!--[[[end]]] (checksum: 49c51091f0aa143d1bc46c63c6a0e660)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                                        | Version                                                                  | License                            | Author                                                                                | Description (from packaging data)                                    |
|:--------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|:-----------------------------------|:--------------------------------------------------------------------------------------|:---------------------------------------------------------------------|
| [attrs](https://www.attrs.org/en/stable/changelog.html)                                     | [23.1.0](https://pypi.org/project/attrs/23.1.0/)                         | MIT License                        | Hynek Schlawack <hs@ox.cx>                                                            | Classes Without Boilerplate                                          |
| [click](https://palletsprojects.com/p/click/)                                               | [8.1.3](https://pypi.org/project/click/8.1.3/)                           | BSD License                        | Armin Ronacher                                                                        | Composable command line interface toolkit                            |
| [elementpath](https://github.com/sissaschool/elementpath)                                   | [4.1.2](https://pypi.org/project/elementpath/4.1.2/)                     | MIT License                        | Davide Brunato                                                                        | XPath 1.0/2.0/3.0/3.1 parsers and selectors for ElementTree and lxml |
| [jsonschema-specifications](https://github.com/python-jsonschema/jsonschema-specifications) | [2023.6.1](https://pypi.org/project/jsonschema-specifications/2023.6.1/) | MIT License                        | Julian Berman                                                                         | The JSON Schema meta-schemas and vocabularies, exposed as a Registry |
| [pyrsistent](https://github.com/tobgu/pyrsistent/)                                          | [0.19.2](https://pypi.org/project/pyrsistent/0.19.2/)                    | MIT License                        | Tobias Gustafsson                                                                     | Persistent/Functional/Immutable data structures                      |
| [rpds-py](https://github.com/crate-py/rpds)                                                 | [0.8.10](https://pypi.org/project/rpds-py/0.8.10/)                       | MIT License                        | Julian Berman                                                                         | Python bindings to Rust's persistent data structures (rpds)          |
| [typing_extensions](https://github.com/python/typing_extensions)                            | [4.4.0](https://pypi.org/project/typing_extensions/4.4.0/)               | Python Software Foundation License | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com> | Backported and Experimental Type Hints for Python 3.7+               |
<!--[[[end]]] (checksum: 4b5c21866a76a6f205fd9435580c2821)-->

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
jsonschema==4.18.4
├── attrs [required: >=22.2.0, installed: 23.1.0]
├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.6.1]
│   └── referencing [required: >=0.28.0, installed: 0.29.1]
│       ├── attrs [required: >=22.2.0, installed: 23.1.0]
│       └── rpds-py [required: >=0.7.0, installed: 0.8.10]
├── referencing [required: >=0.28.4, installed: 0.29.1]
│   ├── attrs [required: >=22.2.0, installed: 23.1.0]
│   └── rpds-py [required: >=0.7.0, installed: 0.8.10]
└── rpds-py [required: >=0.7.1, installed: 0.8.10]
lxml==4.9.3
msgspec==0.17.0
PyYAML==6.0.1
toml==0.10.2
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
└── typing-extensions [required: >=3.7.4.3, installed: 4.4.0]
xmlschema==2.3.1
└── elementpath [required: >=4.1.2,<5.0.0, installed: 4.1.2]
````
<!--[[[end]]] (checksum: df526863822350eb71d18292dff22060)-->
