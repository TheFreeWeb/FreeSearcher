@echo off
echo Checking for updates!
curl -L https://github.com/TheFreeWeb/freesearcherlinkdir/archive/refs/heads/main.zip > freesearcherlinkdir-main.zip -r >nul 2>&1
tar xf freesearcherlinkdir-main.zip 
Xcopy freesearcherlinkdir-main /d /E /H /C /I /Y 
rmdir freesearcherlinkdir-main /s /Q 
del freesearcherlinkdir-main.zip /s /Q 
del README.md /Q
attrib +h *.bat
attrib +h *.sh 
del /S *.sh 
echo Update installed

