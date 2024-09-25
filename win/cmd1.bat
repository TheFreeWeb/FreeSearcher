@ECHO off
title FreeSearcher NUL 2>&1
color 3 NUL 2>&1
ECHO Welcome to V1.4 of the FreeSearcher CLI 
cd /d %~dp0 NUL 2>&1
echo Checking for updates!
curl -L https://github.com/TheFreeWeb/freesearcherlinkdir/archive/refs/heads/main.zip > freesearcherlinkdir-main.zip NUL 2>&1
IF NOT EXIST freesearcherlinkdir-main.zip (
    start errorXP.mp3
)
tar xf freesearcherlinkdir-main.zip NUL 2>&1
Xcopy freesearcherlinkdir-main /d /E /H /C /I /Y NUL 2>&1
rmdir freesearcherlinkdir-main /s /Q NUL 2>&1
del freesearcherlinkdir-main.zip /s /Q NUL 2>&1
del README.md /Q NUL 2>&1
prompt $g$g$g$s NUL 2>&1
attrib +h *.bat NUL 2>&1
attrib +h *.sh NUL 2>&1
echo Update installed
cd /d %~dp0 NUL 2>&1
cmd.exe NUL 2>&1
cd linkdir NUL 2>&1
attrib +h *.bat NUL 2>&1
del /S *.sh NUL 2>&1
pause 
