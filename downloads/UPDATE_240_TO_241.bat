@echo off
setlocal
set "APPROOT=%~dp0"
if not exist "%APPROOT%RenPyVN_Studio.exe" for %%I in ("%~dp0..") do set "APPROOT=%%~fI\"
if not exist "%APPROOT%RenPyVN_Studio.exe" (
  echo STOP: Dat nguyen thu muc downloads vao thu muc co RenPyVN_Studio.exe.
  pause
  exit /b 1
)
if not exist "%APPROOT%runtime\python.exe" (
  echo STOP: Khong tim thay runtime\python.exe cua ban 2.4.0 tai "%APPROOT%".
  pause
  exit /b 1
)
"%APPROOT%runtime\python.exe" "%~dp0REN241_INSTALL.py"
set "ERR=%ERRORLEVEL%"
if not "%ERR%"=="0" echo CAP NHAT THAT BAI. Khong tu dong xoa project hay rule.
pause
exit /b %ERR%
