#!/bin/bash

# Path to the folder
FOLDER_PATH="/etc/abc"

# I just Changed here and Added exit code
# Check if the folder exists
if [ -d "$FOLDER_PATH" ]; then
    echo "The folder '$FOLDER_PATH' exists."
    exit 0
else
    echo "The folder '$FOLDER_PATH' does not exist."
    exit 1
fi
