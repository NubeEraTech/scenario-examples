#!/bin/bash
FILE_PATH="/etc/testfile.txt"
if [ -f "$FILE_PATH" ]; then
    echo "The file '$FILE_PATH' exists."
    exit 0
else
    echo "The file '$FILE_PATH' does not exist."
    exit 1
fi
