@ECHO off
title FreeSearcher
color 3
ECHO Welcome to V1.4 of the FreeSearcher CLI 
cd /d %~dp0
echo Checking for updates!
curl -L https://github.com/TheFreeWeb/freesearcherlinkdir/archive/refs/heads/main.zip > freesearcherlinkdir-main.zip 
IF NOT EXIST freesearcherlinkdir-main.zip (
    start errorXP.mp3
)
tar xf freesearcherlinkdir-main.zip 
Xcopy freesearcherlinkdir-main /d /E /H /C /I /Y 
rmdir freesearcherlinkdir-main /s /Q 
del freesearcherlinkdir-main.zip /s /Q
del README.md /Q 
prompt $g$g$g$s
attrib +h *.bat 
attrib +h *.sh
echo Update installed
cd /d %~dp0
cmd.exe
cd linkdir
attrib +h *.bat
del /S *.sh
pause 
