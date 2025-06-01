@echo off
echo Installing Python dependencies for MP3 Playlist Cleaner...

:: Optional: Check if pip is available
pip --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Error: pip is not available. Please install Python 3.x from https://www.python.org/
    pause
    exit /b
)

:: Install mutagen
pip install mutagen

echo ✅ Done! You can now run the script with:
echo python playlist.py
pause
