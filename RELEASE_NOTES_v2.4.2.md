# RenPyVN Studio v2.4.2 — binary-only public release plan

The existing source-inclusive ZIP is **NOT** suitable for public release: it contains readable `app.py` and `renpyvn/*.py`. Keep this development repository **private**.

Prepare a native compiled Windows x64 build privately. The build kit `RenPyVN_v2.4.2_BINARY_ONLY_BUILD_KIT.zip` contains `BUILD_BINARY_ONLY.py`, `BUILD_BINARY_ONLY.cmd`, and `README_RELEASE.md`. Copy the two scripts into the FULL 2.4.2 app/source folder and run the CMD on Windows. It stages only application code and the third-party decompiler, patches the frozen subprocess compatibility in the temporary stage, compiles with Nuitka, validates that no plaintext Python modules/game scripts/project databases are in the output, and writes a SHA-256 checksum. **This has not yet been run on Windows.**

Publish only the output `RenPyVN_Studio_v2.4.2_Windows_x64_BINARY_ONLY.zip` after Windows GUI/decompile smoke tests pass. Create a separate **public, downloads-only** repository with only README and Releases; attach the binary ZIP under tag `v2.4.2`. Do not make this development repository public. Executables can still be reverse engineered; no plain project source is included in the intended release.

No public release asset has been uploaded as of this note.
