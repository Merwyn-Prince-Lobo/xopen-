@echo off
:: install.bat — installs xopen on Windows
:: Run this as Administrator

echo Installing xopen...

set SCRIPT=%~dp0xopen.py
set TARGET=C:\Windows\System32\xopen.cmd

:: Create a wrapper .cmd so you can type 'xopen' from anywhere
(
echo @echo off
echo python "%SCRIPT%" %%*
) > "%TARGET%"

echo Done! You can now use: xopen ^<file^>
echo.
echo Examples:
echo   xopen video.mp4
echo   xopen document.pdf
echo   xopen .
pause
