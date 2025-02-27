#!/bin/bash
USERNAME="testuser"
if id "$USERNAME" &>/dev/null; then
    echo "User '$USERNAME' exists."
    exit 0
else
    echo "User '$USERNAME' does not exist."
    exit 1
fi
