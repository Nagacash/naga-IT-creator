
[![GitHub](https://img.shields.io/github/license/Nagacash/naga-IT-creator)](https://github.com/Nagacash/naga-IT-creator/blob/main/LICENSE)
[![PyPI - Version](https://img.shields.io/pypi/v/nagacodex-editor)](https://pypi.org/project/nagacodex-editor/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/nagacodex-editor)](https://pypi.org/project/nagacodex-editor/)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Nagacash/naga-IT-creator)](https://github.com/Nagacash/naga-IT-creator/pulse)
[![GitHub last commit](https://img.shields.io/github/last-commit/Nagacash/naga-IT-creator)](https://github.com/Nagacash/naga-IT-creator/commits/main)
[![GitLab Issues](https://img.shields.io/github/issues/Nagacash/naga-IT-creator)](https://github.com/Nagacash/naga-IT-creator/issues)

<!--
![image](https://github.com/user-attachments/assets/a578d600-a4a8-4ce4-904d-4aa0e73fc124)
-->

`Naga Codex` is a fast, extensible, native AI code editor with NVIDIA NIM built in. lightweight <20 mb in size. install and start using in seconds. 

- built on the open-source biscuit engine, rebranded for Naga Codex
- for developer/user guides, see the project [documentation](https://github.com/Nagacash/naga-IT-creator)
- packed with superpowers: AI chat, agentic edits, code intelligence, source control

<img alt="nagacodex" src="https://github.com/user-attachments/assets/ac5254cc-e1ac-4fe6-a582-51b5129756e3" />

## `installing`

install the latest release by running:

```bash
pip install nagacodex-editor        # using pip
uv tool install nagacodex-editor    # using uv
```

quickly open up a project using **`nagacodex path/to/src`** and start editing.

## `contributing`

- please check the [contributing guide](https://github.com/Nagacash/naga-IT-creator/blob/main/CONTRIBUTING.md) for a quick tour of the project structure and to set up the environment.
- [support the work](https://github.com/sponsors/Nagacash)


# `PROGRESS` 

### `agents`

- [x] gemini, anthropic API support (`claude-4-5-opus/sonnet/haiku`, `gemini-2-5-flash/pro`)
- [x] planning agent with task list
  - [x] ReadFileTool
  - [x] EditFileTool
  - [x] DeleteFileTool
  - [x] ListDirTool
  - [x] GlobFileSearchTool
  - [x] GrepTool
  - [x] CodebaseSearchTool
  - [x] RunTerminalCmdTool
  - [x] TodoWriteTool
  - [x] GetWorkspaceInfoTool
  - [x] GetActiveEditorTool
- [x] add more LLM providers through biscuit extensions
- [x] attach files for adding context in chat
- [ ] LLM provider extension examples (old ones are now deprecated)
- [x] run local LLMs with ~~[ollama extension](https://github.com/tomlin7/biscuit-extensions/blob/main/extensions/ollama.py)~~ (deprecated)
- [ ] ollama extension rewrite 
- [x] LLM calls inside biscuit terminals (use `# your prompt` inside terminal, then accept/decline response)

### `code intelligence`

- [x] fast tree-sitter based parsing and highlights 
- [x] code completions within editor (with icons)
- [x] hover for symbol definition/docstring (rendered with highlights + markdown)
- [x] symbol outline sidebar panel for navigating symbols in open editor
- [x] symbol search through command palette `Ctrl + J`)
- [x] floating peek widget to jump-to-definition/declaration of symbols
- [x] symbol references in open editor
- [x] adding more language servers through biscuit extensions

more language servers are registered through extensions, see the [rust](https://github.com/biscuit-extensions/rust), [clangd](https://github.com/biscuit-extensions/clangd) extensions for reference.

<img alt="lsp and agents" src="https://github.com/user-attachments/assets/30b52da7-af5b-490b-912a-fb8b4d61dcb0" />

### `source control`

- [x] split diff viewer for changes/staged changes
- [x] essential git operations easily accessible (push, pull, commit, stage, unstage, switch branches)
- [x] clone repositories and immediately open in active window, or new window
- [x] view gitHub issues/prs within editor (TODO: disabled rn, will be converted to an extension)

### `fast search`

- [x] ripgrep based fast search, quickly accessible from statusbar
- [x] replace occurrences individually or all at once
- [x] regex support, case sensitive search and more customization
- [x] search within open editors with floating find-replace widget

<img alt="search" src="https://github.com/user-attachments/assets/d4ef7657-f37b-40ab-b9b1-c00d45e7f764" />

### `code debugging`

- [x] setting breakpoints across files
- [x] inspection panel for all runtime variables 
- [x] modify runtime variables while debugging
- [x] call stack visualization and exception tracing
- [ ] full [DAP client](https://github.com/tomlin7/debug-adapter-client) integration
- [x] built-in python debugger
- [x] add debuggers can be registered through biscuit extensions.

### `extensions`

- [x] install and manage all available extensions though a gui
- [x] extension search within biscuit
- [x] extension bootstrapping cli commands and templates
- [x] [extension docs](https://github.com/tomlin7/biscuit-extensions)
- [x] extensions marketplace website: [visit here](https://biscuit-extensions.github.io/marketplace)

<img alt="extensions" src="https://github.com/user-attachments/assets/91ab0044-2eac-4c20-972d-6719002edb1a" />

### `misc`

- [x] split markdown editor, plain HTML renderer
- [x] toggle relative line numbering support
- [ ] vim mode support
- [x] add formatters through biscuit extensions
- [x] formatter extensions: ~~[black](https://github.com/tomlin7/biscuit-extensions/blob/main/extensions/black.py)~~ [DEPRECATED], ~~[ruff](https://github.com/tomlin7/biscuit-extensions/blob/main/extensions/ruff.py)~~[DEPRECATED], ~~[YAPF](https://github.com/tomlin7/biscuit-extensions/blob/main/extensions/yapf.py)~~[DEPRECATED], ~~[autopep8](https://github.com/tomlin7/biscuit-extensions/blob/main/extensions/autopep8.py)~~ [DEPRECATED] for reference.
- [x] drag-n-drop to open files or folders in biscuit
- [x] [editorconfig](https://editorconfig.org/) support for projects
- [x] sophisticated command palette (full list of static commands in [src/biscuit/commands](https://github.com/tomlin7/biscuit/blob/main/src/biscuit/commands.py))

<img alt="preview" src="https://github.com/user-attachments/assets/1c44aab4-d8d1-4ba8-b92b-73c0c6dbfb00" />

## `license`

biscuit uses the MIT License, see [LICENSE](https://github.com/Nagacash/naga-IT-creator/blob/main/LICENSE.md) file.
# naga-IT-creator
