#!/bin/bash

# Path to the folder
FOLDER_PATH="/etc/abc"

# Check if the folder exists
if [ -d "$FOLDER_PATH" ]; then
    echo "The folder '$FOLDER_PATH' exists."
else
    echo "The folder '$FOLDER_PATH' does not exist."
fi
