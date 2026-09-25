@echo off
setlocal
set "ROOT=%~dp0"
if not exist "%ROOT%_release_binary_only\RenPyVN_Studio_v2.4.2_Windows_x64_BINARY_ONLY.zip" (
  echo STOP: Build the private app first with BUILD_BINARY_ONLY_BRANDED.cmd.
  echo Do not upload an older FULL/source ZIP.
  pause
  exit /b 1
)
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%ROOT%PUBLISH_BINARY_ONLY.ps1" -ZipPath "%ROOT%_release_binary_only\RenPyVN_Studio_v2.4.2_Windows_x64_BINARY_ONLY.zip"
set "RESULT=%ERRORLEVEL%"
if not "%RESULT%"=="0" echo PUBLICATION NOT COMPLETE. Review the error above.
pause
exit /b %RESULT%
