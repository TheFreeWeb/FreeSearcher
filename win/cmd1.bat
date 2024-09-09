@ECHO off
ECHO Welcome to V1.0 of the FreeSearcher CLI
Color E
echo Checking for updates!
curl -L https://github.com/TheFreeWeb/freesearcherlinkdir/archive/refs/heads/main.zip > freesearcherlinkdir-main.zip
tar xf freesearcherlinkdir-main.zip
Xcopy freesearcherlinkdir-main /d /E /H /C /I /Y 
rmdir freesearcherlinkdir-main /s /Q
del freesearcherlinkdir-main.zip /s /Q 
del README.md /Q
attrib +h *.bat
attrib +h *.sh
echo Update installed
cd /d %~dp0
cmd.exe
cd linkdir
attrib +h *.bat
del /S *.sh
pause 
