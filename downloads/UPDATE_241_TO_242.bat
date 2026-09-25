@echo off
setlocal
set "ROOT=%~dp0.."
if not exist "%ROOT%\RenPyVN_Studio.exe" set "ROOT=%~dp0"
if not exist "%ROOT%\RenPyVN_Studio.exe" (
  echo STOP: Hay chep thu muc downloads vao thu muc ung dung RenPyVN 2.4.1.
  pause
  exit /b 1
)
if not exist "%ROOT%\runtime\python.exe" (
  echo STOP: Thieu runtime\python.exe trong thu muc ung dung.
  pause
  exit /b 1
)
"%ROOT%\runtime\python.exe" "%~dp0REN242_INSTALL.py"
set "RC=%ERRORLEVEL%"
if not "%RC%"=="0" echo CAP NHAT THAT BAI. Hay xem thong bao o tren.
pause
exit /b %RC%
