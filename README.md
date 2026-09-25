# RenPyVN Studio — Private development repository

This repository stays **PRIVATE**. Do not make it public: it contains build/patch code and is not the public download destination.

## Publish Windows v2.4.2 without distributing plain source

Follow [the Vietnamese release guide](tools/README_PUBLISH_BINARY_ONLY_VI.md).

- [Windows branded binary-only build](tools/BUILD_BINARY_ONLY_BRANDED.py) and [build launcher](tools/BUILD_BINARY_ONLY_BRANDED.cmd).
- [Guarded public release publisher](tools/PUBLISH_BINARY_ONLY.ps1) and [publish launcher](tools/PUBLISH_BINARY_ONLY.cmd).

Public release destination (will exist *after* a successful Windows build, verification and publisher run):
https://github.com/dphucduc/RenPyVN-Downloads/releases/latest

The previous FULL/PRIVATE zips include readable Python source and must never be used as public release assets. A Nuitka EXE is a compiled binary but can still be reverse engineered.
