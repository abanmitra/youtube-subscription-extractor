@echo off
REM YouTube Subscription Extractor - Windows Launcher
REM This script runs the YouTube Subscription Extractor application

setlocal enabledelayedexpansion

echo.
echo ============================================================
echo YouTube Subscription Extractor
echo ============================================================
echo.

REM Get the directory where this script is located
cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from https://www.python.org/
    pause
    exit /b 1
)

REM Check if requirements are installed
python -c "import google.auth" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install requirements
        pause
        exit /b 1
    )
)

REM Prompt for file path
echo.
set /p FILE_PATH="Enter the path to the email IDs file: "

if "%FILE_PATH%"==" " (
    echo Error: No file path provided
    pause
    exit /b 1
)

if not exist "%FILE_PATH%" (
    echo Error: File not found at %FILE_PATH%
    pause
    exit /b 1
)

REM Run the application
echo Running YouTube Subscription Extractor with file: %FILE_PATH%
echo.
python src\youtube_extractor.py "%FILE_PATH%"

if errorlevel 1 (
    echo.
    echo Process failed with error code !errorlevel!
    pause
) else (
    echo.
    echo Process completed successfully
)

endlocal
