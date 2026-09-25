#requires -Version 5.1
param(
    [string]$Owner = "dphucduc",
    [string]$PublicRepo = "RenPyVN-Downloads",
    [string]$Tag = "v2.4.2",
    [string]$ZipPath = ""
)
$ErrorActionPreference = "Stop"
$fullRepo = "$Owner/$PublicRepo"
if (-not $ZipPath) {
    $ZipPath = Join-Path $PSScriptRoot "..\_release_binary_only\RenPyVN_Studio_v2.4.2_Windows_x64_BINARY_ONLY.zip"
}
$ZipPath = [IO.Path]::GetFullPath($ZipPath)
$checksums = Join-Path (Split-Path $ZipPath -Parent) "SHA256SUMS.txt"
if (-not (Test-Path -LiteralPath $ZipPath -PathType Leaf)) { throw "No built binary ZIP: $ZipPath. Run BUILD_BINARY_ONLY.cmd first." }
if (-not (Test-Path -LiteralPath $checksums -PathType Leaf)) { throw "Missing SHA256SUMS.txt from the build." }

Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead($ZipPath)
try {
    $names = @($zip.Entries | ForEach-Object { $_.FullName.Replace('\','/') })
    $unsafe = @($names | Where-Object {
        $_ -match '(?i)(^|/)(app\.py|\.env|\.renpyvn|progress\.sqlite3|user_data|projects?)(/|$)' -or
        $_ -match '(?i)\.(py|pyc|pyo|rpy|rpyc|sqlite3|db|pem|key)$'
    })
    if ($unsafe.Count -gt 0) { throw "REFUSING TO PUBLISH private/source files: $($unsafe[0])" }
    if (-not @($names | Where-Object { $_ -match '(?i)(^|/)RenPyVN_Studio\.exe$' }).Count) {
        throw "No RenPyVN_Studio.exe in release ZIP."
    }
    if (-not @($names | Where-Object { $_ -match '(?i)(^|/)LICENSE$' }).Count) {
        throw "LICENSE missing from release ZIP."
    }
    if (-not @($names | Where-Object { $_ -match '(?i)(^|/)THIRD_PARTY_NOTICES\.md$' }).Count) {
        throw "THIRD_PARTY_NOTICES.md missing from release ZIP."
    }
} finally { $zip.Dispose() }
$actualSha = (Get-FileHash -LiteralPath $ZipPath -Algorithm SHA256).Hash.ToLowerInvariant()
$sumText = Get-Content -LiteralPath $checksums -Raw
if (-not $sumText.ToLowerInvariant().Contains($actualSha)) { throw "SHA256SUMS.txt does not match built ZIP." }

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw "Install GitHub CLI (gh) on Windows, then run: gh auth login --web"
}
& gh auth status
if ($LASTEXITCODE -ne 0) { throw "Please run gh auth login --web in PowerShell. Never paste tokens in chat." }

# Never use --source or --push: this creates a fresh downloads-only repository.
$visibility = (& gh repo view $fullRepo --json visibility --jq .visibility 2>$null)
if ($LASTEXITCODE -ne 0) {
    Write-Host "Creating PUBLIC downloads-only repo $fullRepo (private source repo is untouched)..."
    & gh repo create $fullRepo --public --add-readme --description "RenPyVN Studio binary-only Windows downloads; source lives in a separate private repo."
    if ($LASTEXITCODE -ne 0) { throw "Could not create downloads repository." }
} elseif ($visibility.Trim().ToUpperInvariant() -ne "PUBLIC") {
    throw "Existing $fullRepo is not PUBLIC. Refusing to change the visibility of an existing repository."
}

# Public repository contains only this small README plus release assets.
$readme = @"
# RenPyVN Studio - Windows downloads

Get the latest Windows x64 app under [Releases](https://github.com/$fullRepo/releases/latest).

1. Download the \`*_BINARY_ONLY.zip\` file from the latest release (not GitHub's automatic **Source code** ZIP).
2. Extract the whole archive and run \`RenPyVN_Studio.exe\`.
3. Bring your own AI API credentials or Ollama. No game scripts or personal project data are included.

The development/source repository is PRIVATE. Executables can still be reverse engineered; binary-only means source files are not distributed in the release ZIP. License and third-party notices are included in the download.
"@
$encodedReadme = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($readme))
$readmeSha = (& gh api "repos/$fullRepo/contents/README.md" --jq .sha)
if ($LASTEXITCODE -ne 0) { throw "Cannot inspect public README." }
& gh api --method PUT "repos/$fullRepo/contents/README.md" -f message="Document Windows binary download" -f content="$encodedReadme" -f sha="$readmeSha" | Out-Null
if ($LASTEXITCODE -ne 0) { throw "Cannot update public README." }

& gh release view $Tag --repo $fullRepo *> $null
if ($LASTEXITCODE -eq 0) { throw "Release $Tag already exists. Not overwriting published files." }

Write-Host ""
Write-Host "READY TO PUBLISH:"
Write-Host "  Public repo: $fullRepo"
Write-Host "  Binary ZIP:  $ZipPath"
Write-Host "  SHA-256:     $actualSha"
Write-Host "  Source repo remains PRIVATE. No .py or project database in the ZIP."
$confirmation = Read-Host "After testing the EXE on Windows, type PUBLISH to release publicly"
if ($confirmation -cne "PUBLISH") { throw "Cancelled before publishing." }

$notes = "RenPyVN Studio v2.4.2 - Windows x64. New app mascot icon, section 03 pair search, pronoun-change review and Smart Translation QA. Download the binary-only ZIP, extract all files and run RenPyVN_Studio.exe. Bring your own API credentials or Ollama. SHA256SUMS.txt is attached. This release does not include plain Python source, personal scripts or project databases."
& gh release create $Tag $ZipPath $checksums --repo $fullRepo --title "RenPyVN Studio v2.4.2 - Windows x64" --notes $notes --latest
if ($LASTEXITCODE -ne 0) { throw "Release upload failed; check GitHub before retrying." }
& gh release view $Tag --repo $fullRepo --json url,isDraft,assets
if ($LASTEXITCODE -ne 0) { throw "Release was submitted but verification failed. Inspect GitHub manually." }
Write-Host "DONE: https://github.com/$fullRepo/releases/tag/$Tag"
