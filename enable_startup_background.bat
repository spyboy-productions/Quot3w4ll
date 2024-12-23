@echo off
setlocal

:: Get the directory where the enable_startup.bat is located
set "SCRIPT_DIR=%~dp0"

:: Define the Startup folder path
set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

:: Create the startup_wall.vbs file in the Startup folder
echo Set WshShell = CreateObject("WScript.Shell") > "%STARTUP_FOLDER%\startup_wall.vbs"
echo WshShell.Run "cmd /c cd /d ""D:\projects\GitHub\Quot3w4ll"" && python3 wall.py", 0, False >> "%STARTUP_FOLDER%\startup_wall.vbs"

echo The startup_wall.vbs file has been created in the Startup folder.

endlocal
pause
