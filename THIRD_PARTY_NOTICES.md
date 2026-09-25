# Third-party components

## CPython / python-build-standalone

Bundled runtime: CPython **3.12.14**, x86_64 Windows MSVC, build **20260901**,
distributed by the official [astral-sh/python-build-standalone repository](https://github.com/astral-sh/python-build-standalone).

Artifact: `cpython-3.12.14+20260901-x86_64-pc-windows-msvc-install_only_stripped.tar.gz`.
Upstream release: https://github.com/astral-sh/python-build-standalone/releases/tag/20260901

Downloaded archive SHA-256 (matched the upstream GitHub asset digest):
`7c45c9622400d578709a9b2cddbe8124cc21d382409d9f13406d706d28e31b14`.

The runtime includes Python, Tcl/Tk, OpenSSL, SQLite and other components under
their respective licenses. Preserve `runtime/LICENSE.txt`, Tcl/Tk license files,
and all license notices distributed inside the runtime when redistributing it.
Python itself is under the PSF license and accompanying historical notices.

## unrpyc

Version **2.0.3**, from upstream tag `v2.0.3`:
https://github.com/CensoredUsername/unrpyc/tree/v2.0.3

Copyright (c) 2012–2024 Yuri K. Schlesner, CensoredUsername, Jackmcbarn.
MIT license; full original license in `vendor/unrpyc/LICENSE` and source headers.
Source code is included. App runs its standard decompiler in a child process;
the optional obfuscation recovery mode is not enabled.

## Windows launcher compiler

The small launcher in `tools/launcher.c` was cross-compiled with Zig 0.16.0's
Windows GNU target. Its Windows runtime imports are standard OS/UCRT libraries.
The launcher source is included. The Zig compiler itself is not shipped.

## Original application

The `renpyvn/` modules, `app.py`, original tests, launch scripts and launcher
source are provided under `LICENSE`. Third-party components retain their own
licenses.
