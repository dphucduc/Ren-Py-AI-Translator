@echo off
setlocal
set "ROOT=%~dp0"
if not exist "%ROOT%app.py" (
  echo STOP: Copy BUILD_BINARY_ONLY_BRANDED.py and this CMD into the FULL private RenPyVN v2.4.2 folder next to app.py.
  pause
  exit /b 1
)
if not exist "%ROOT%runtime\python.exe" (
  echo STOP: runtime\python.exe missing. Do not use a small patch-only folder.
  pause
  exit /b 1
)
"%ROOT%runtime\python.exe" "%ROOT%BUILD_BINARY_ONLY_BRANDED.py"
set "STATUS=%ERRORLEVEL%"
if not "%STATUS%"=="0" echo BUILD FAILED. Do not publish the old source-containing ZIP.
pause
exit /b %STATUS%
