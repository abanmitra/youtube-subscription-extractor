#!/bin/bash

# YouTube Subscription Extractor - Unix Launcher
# This script runs the YouTube Subscription Extractor application on macOS and Linux

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo ""
echo "============================================================"
echo "YouTube Subscription Extractor"
echo "============================================================"
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed${NC}"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Using Python $PYTHON_VERSION"

# Check if requirements are installed
python3 -c "import google.auth" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing required packages..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo -e "${RED}Error: Failed to install requirements${NC}"
        exit 1
    fi
fi

# Prompt for file path
echo ""
read -p "Enter the path to the email IDs file: " FILE_PATH

if [ -z "$FILE_PATH" ]; then
    echo -e "${RED}Error: No file path provided${NC}"
    exit 1
fi

if [ ! -f "$FILE_PATH" ]; then
    echo -e "${RED}Error: File not found at $FILE_PATH${NC}"
    exit 1
fi

# Run the application
echo "Running YouTube Subscription Extractor with file: $FILE_PATH"
echo ""
python3 src/youtube_extractor.py "$FILE_PATH"

EXIT_CODE=$?
echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}Process completed successfully${NC}"
else
    echo -e "${RED}Process failed with error code $EXIT_CODE${NC}"
fi

exit $EXIT_CODE
