; Define the installer settings
OutFile "MyApp.exe"
InstallDir "$EXEDIR"
RequestExecutionLevel admin ; Request admin rights

; Define the sections and their actions
Section "Main"

    ; Set the installation path
    SetOutPath "$EXEDIR"

    ; Include necessary files
    File "cmd1.bat"

    ; Execute the batch file with admin privileges
    ExecShell "runas" "$EXEDIR\cmd1.bat" "" SW_SHOWNORMAL

    ; Hide the installer window instantly after executing the batch file
    ; Postpone hiding the window until after the batch file has started
    ; Delay is set to ensure the batch file starts properly
    System::Call 'user32::ShowWindow(i $HWNDPARENT, i ${SW_HIDE}) i.r0'
    Sleep 1000

SectionEnd

; Request the installation directory page
Page Directory
; Request the installation files page
Page InstFiles
