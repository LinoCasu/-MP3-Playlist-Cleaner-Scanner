#!/bin/bash
echo "Installing Python dependencies for MP3 Playlist Cleaner..."

# Check for pip
if ! command -v pip &> /dev/null
then
    echo "❌ pip not found. Please install Python 3.x and pip."
    exit 1
fi

# Install mutagen
pip install mutagen

echo "✅ Done! You can now run the script with:"
echo "python3 playlist.py"
