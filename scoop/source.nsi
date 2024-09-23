OutFile "MyApp.exe"
InstallDir "$EXEDIR"
RequestExecutionLevel admin 

Section "Main"

    SetOutPath "$EXEDIR"

    File "cmd1.bat"

    ExecShell "runas" "$EXEDIR\cmd1.bat" "" SW_SHOWNORMAL

    System::Call 'user32::ShowWindow(i $HWNDPARENT, i ${SW_HIDE}) i.r0'
    Sleep 1000

SectionEnd

Page Directory
Page InstFiles
