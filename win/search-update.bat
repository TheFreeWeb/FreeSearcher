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
