"""Private Windows build: RenPyVN v2.4.2 with the chosen chibi app icon.
Only the compiled ZIP is intended for public GitHub Releases.
Run next to app.py, renpyvn/, vendor/, assets/ and runtime/ on Windows x64.
"""
from __future__ import annotations
import ast
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import zipfile

VERSION = "2.4.2"
NAME = f"RenPyVN_Studio_v{VERSION}_Windows_x64_BINARY_ONLY"
GUARD = '    if not (app_home()/"vendor"/"unrpyc"/"unrpyc.py").exists():\n'
FROZEN = 'if getattr(sys,"frozen",False): cmd=[sys.executable,"--decompile",str(staged)]'
COMPILED = 'if getattr(sys,"frozen",False) or "__compiled__" in globals(): cmd=[sys.executable,"--decompile",str(staged)]'

def validate_stage(source: Path, stage: Path) -> None:
    required = ["app.py", "renpyvn/gui.py", "renpyvn/archives.py",
                "renpyvn/__init__.py", "vendor/unrpyc/unrpyc.py",
                "vendor/unrpyc/LICENSE", "assets/app.ico",
                "assets/logo_64.png", "assets/logo_40.png", "LICENSE",
                "THIRD_PARTY_NOTICES.md", "runtime/python.exe"]
    for name in required:
        if not (source / name).is_file():
            raise RuntimeError(f"Missing {name}; use the FULL private 2.4.2 WITH_LOGO folder")
    if '2.4.2-PairSearch' not in (source/"renpyvn/__init__.py").read_text("utf8"):
        raise RuntimeError("Build only from v2.4.2 (not 2.3.6/2.4.0/2.4.1)")
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)
    shutil.copy2(source/"app.py", stage/"app.py")
    shutil.copytree(source/"renpyvn", stage/"renpyvn",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.pyo"))
    shutil.copytree(source/"vendor/unrpyc", stage/"vendor/unrpyc",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.pyo", ".git"))
    shutil.copytree(source/"assets", stage/"assets")
    path = stage/"renpyvn/archives.py"
    original = path.read_text("utf8")
    rows = original.splitlines(keepends=True)
    result = []
    i = 0
    guard_count = 0
    while i < len(rows):
        if rows[i] == GUARD:
            if i+1 >= len(rows) or 'raise ArchiveError("Thiếu vendor/unrpyc.' not in rows[i+1]:
                raise RuntimeError("Unexpected vendor preflight in archives.py")
            i += 2
            guard_count += 1
        else:
            result.append(rows[i])
            i += 1
    changed = "".join(result)
    if guard_count != 1 or changed.count(FROZEN) != 1:
        raise RuntimeError("Unexpected decompile worker; refusing to build")
    changed = changed.replace(FROZEN, COMPILED)
    ast.parse(changed, filename="renpyvn/archives.py")
    path.write_text(changed, "utf8")
    for path in (stage/"renpyvn").glob("*.py"):
        ast.parse(path.read_text("utf8"), filename=str(path))
    ast.parse((stage/"app.py").read_text("utf8"), filename="app.py")
    print("Private stage verified; no user projects or tokens copied.")

def build(root: Path) -> Path:
    stage = root/"_release_build_242"/"stage"
    validate_stage(root, stage)
    if os.name != "nt":
        raise RuntimeError("Windows x64 compilation must run on Windows, not Linux.")
    py = root/"runtime/python.exe"
    subprocess.run([str(py), "-m", "pip", "install", "--upgrade",
                    "nuitka", "ordered-set", "zstandard"], check=True)
    compile_dir = root/"_release_build_242"/"compile"
    compile_dir.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env["PYTHONPATH"] = os.pathsep.join([str(stage), str(stage/"vendor/unrpyc"),
                                         env.get("PYTHONPATH","")])
    cmd = [str(py), "-m", "nuitka", "--mode=standalone", "--mingw64",
           "--assume-yes-for-downloads", "--enable-plugin=tk-inter",
           "--windows-console-mode=disable", "--include-package=renpyvn",
           "--include-module=unrpyc", "--include-package=decompiler",
           "--output-filename=RenPyVN_Studio.exe",
           f"--output-dir={compile_dir}",
           f"--windows-icon-from-ico={stage/'assets/app.ico'}",
           f"--include-data-dir={stage/'assets'}=assets",
           str(stage/"app.py")]
    print("Nuitka compiling. First Windows build may take a while.")
    subprocess.run(cmd, cwd=stage, env=env, check=True)
    dist = compile_dir/"app.dist"
    if not (dist/"RenPyVN_Studio.exe").is_file():
        raise RuntimeError("Expected Nuitka exe was not created")
    for name in ("LICENSE", "THIRD_PARTY_NOTICES.md"):
        shutil.copy2(root/name, dist/name)
    (dist/"vendor/unrpyc").mkdir(parents=True, exist_ok=True)
    shutil.copy2(root/"vendor/unrpyc/LICENSE", dist/"vendor/unrpyc/LICENSE")
    (dist/"README_DOWNLOAD.txt").write_text(
        "RenPyVN Studio 2.4.2 Windows x64\n"
        "Extract the whole ZIP and run RenPyVN_Studio.exe.\n"
        "Use your own API key or Ollama. No game projects included.\n"
        "See LICENSE and THIRD_PARTY_NOTICES.md.\n"
        "Binary-only packaging is not absolute protection against reverse engineering.\n",
        encoding="utf8")
    forbidden = {".py", ".pyc", ".pyo", ".rpy", ".rpyc", ".sqlite3", ".db", ".pem", ".key"}
    unsafe = [str(p.relative_to(dist)) for p in dist.rglob("*")
              if p.is_file() and (p.suffix.lower() in forbidden or
                 any(part.lower() in ("projects", "user_data", ".renpyvn") for part in p.parts))]
    if unsafe:
        raise RuntimeError("Unsafe files in distribution: " + ", ".join(unsafe[:10]))
    output = root/"_release_binary_only"
    output.mkdir(parents=True, exist_ok=True)
    archive = output/f"{NAME}.zip"
    with zipfile.ZipFile(archive,"w",compression=zipfile.ZIP_DEFLATED,
                         compresslevel=6,allowZip64=True) as zipout:
        for path in sorted(dist.rglob("*")):
            if path.is_file():
                zipout.write(path, f"{NAME}/{path.relative_to(dist).as_posix()}")
    with zipfile.ZipFile(archive) as check:
        if check.testzip() is not None: raise RuntimeError("Release ZIP CRC error")
    sha = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output/"SHA256SUMS.txt").write_text(f"{sha}  {archive.name}\n","ascii")
    print("BUILT:", archive)
    print("SHA256:",sha)
    print("TEST the compiled EXE on Windows before publishing.")
    return archive

if __name__=="__main__":
    try:
        root=Path(__file__).resolve().parent
        result=build(root)
    except Exception as exc:
        print("BUILD FAILED:",exc,file=sys.stderr)
        raise SystemExit(1)
