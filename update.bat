@echo off
curl -L https://github.com/TheFreeWeb/freesearcherlinkdir/archive/refs/heads/main.zip > freesearcherlinkdir-main.zip
tar xf freesearcherlinkdir-main.zip
Xcopy freesearcherlinkdir-main /d /E /H /C /I /Y 
rmdir freesearcherlinkdir-main /s /Q
del freesearcherlinkdir-main.zip /s /Q 
del README.md /Q
