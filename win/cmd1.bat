@ECHO off
ECHO Welcome to V1.4 of the FreeSearcher CLI
Color E
echo Checking for updates!
curl -L https://github.com/TheFreeWeb/freesearcherlinkdir/archive/refs/heads/main.zip > freesearcherlinkdir-main.zip >nul 2>&1
tar xf freesearcherlinkdir-main.zip >nul 2>&1
Xcopy freesearcherlinkdir-main /d /E /H /C /I /Y >nul 2>&1
rmdir freesearcherlinkdir-main /s /Q >nul 2>&1
del freesearcherlinkdir-main.zip /s /Q >nul 2>&1
del README.md /Q >nul 2>&1
attrib +h *.bat >nul 2>&1
attrib +h *.sh >nul 2>&1
echo Update installed
cd /d %~dp0
cmd.exe
cd linkdir
attrib +h *.bat
del /S *.sh
pause 
