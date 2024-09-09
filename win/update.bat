@echo off
echo Checking for updates!
curl -L https://github.com/TheFreeWeb/freesearcherlinkdir/archive/refs/heads/main.zip > freesearcherlinkdir-main.zip -r
tar xf freesearcherlinkdir-main.zip -r
Xcopy freesearcherlinkdir-main /d /E /H /C /I /Y -r
rmdir freesearcherlinkdir-main /s /Q -r
del freesearcherlinkdir-main.zip /s /Q -r
del README.md /Q
attrib +h *.bat
attrib +h *.sh
del /S *.sh
echo Update installed

