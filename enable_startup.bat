@echo off
setlocal

:: Get the directory where the enable_startup.bat is located
set "SCRIPT_DIR=%~dp0"

:: Define the Startup folder path
set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

:: Create the startup_wall.bat file in the Startup folder
echo @echo off > "%STARTUP_FOLDER%\startup_wall.bat"
echo cd /d "%SCRIPT_DIR%" >> "%STARTUP_FOLDER%\startup_wall.bat"
echo python3 wall.py >> "%STARTUP_FOLDER%\startup_wall.bat"

echo The startup_wall.bat file has been created in the Startup folder.

endlocal
pause