# RenPyVN Studio v2.4.2 — Windows x64

**Distribution status:** The portable Windows package is prepared, but the repository is currently private and no GitHub Release asset has been published yet. Do not mistake the `downloads/` patches for the standalone application.

## Release package

File name: `RenPyVN_Studio_v2.4.2_Windows_x64_PUBLIC.zip`

SHA-256: `5f3728eb80f5aa8dc16cdf0e419c19c71accbf4f9bdfd435b5461622ae36c0a6`

Portable: extract the whole ZIP, then run `RenPyVN_Studio.exe`. Includes Python runtime; does not require a separate Python installation.

Features: Smart Translation QA (2.4.0), review before applying pronoun changes from imported Rule JSON (2.4.1), and pair search in section 03 (2.4.2).

## Publication checklist

- Publish **only the sanitized release archive**. Personal scripts, project databases, and API credentials must not be bundled.
- Add the ZIP as an asset in **GitHub Releases** with tag `v2.4.2`; do not publish a small upgrade patch as a full installer.
- Change repository visibility to public only if you intend to publish repository contents and commit history. A separate public downloads repository can preserve a private development repository.
- Preserve `LICENSE`, `THIRD_PARTY_NOTICES.md`, and bundled third-party licenses.
- Windows GUI and live provider integration have not been end-to-end verified in the present environment.

## Install

1. Download the full Windows x64 ZIP from Releases once it is published.
2. Extract it completely.
3. Open `RenPyVN_Studio.exe`. Configure your own AI provider or Ollama. No API keys or game scripts are included.
