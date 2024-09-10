@echo off
echo Checking for updates!
curl -L https://github.com/TheFreeWeb/freesearcherlinkdir/archive/refs/heads/main.zip > freesearcherlinkdir-main.zip -r >nul 2>&1
tar xf freesearcherlinkdir-main.zip >nul 2>&1
Xcopy freesearcherlinkdir-main /d /E /H /C /I /Y >nul 2>&1
rmdir freesearcherlinkdir-main /s /Q >nul 2>&1
del freesearcherlinkdir-main.zip /s /Q >nul 2>&1
del README.md /Q >nul 2>&1
attrib +h *.bat >nul 2>&1
attrib +h *.sh >nul 2>&1
del /S *.sh >nul 2>&1
echo Update installed

