#!/bin/bash
FILE_PATH="/etc/testfile.txt"
PERMISSIONS="644"
if [ "$(stat -c "%a" "$FILE_PATH")" == "$PERMISSIONS" ]; then
    echo "The file permissions are set correctly."
    exit 0
else
    echo "The file permissions are incorrect."
    exit 1
fi
