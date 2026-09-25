@echo off
setlocal
set "APPROOT=%~dp0"
if not exist "%APPROOT%RenPyVN_Studio.exe" for %%I in ("%~dp0..") do set "APPROOT=%%~fI\"
if not exist "%APPROOT%RenPyVN_Studio.exe" (
  echo STOP: Dat file REN241_ONEFILE_INSTALL.py va BAT trong thu muc ung dung hoac thu muc con downloads.
  pause
  exit /b 1
)
if not exist "%APPROOT%runtime\python.exe" (
  echo STOP: Khong tim thay runtime\python.exe cua ban 2.4.0 tai "%APPROOT%".
  pause
  exit /b 1
)
"%APPROOT%runtime\python.exe" "%~dp0REN241_ONEFILE_INSTALL.py"
set "ERR=%ERRORLEVEL%"
if not "%ERR%"=="0" echo CAP NHAT THAT BAI. Du lieu project khong duoc ghi de.
pause
exit /b %ERR%
