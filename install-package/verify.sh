#!/bin/bash

PACKAGE="curl"

if dpkg -s "$PACKAGE" &>/dev/null && command -v "$PACKAGE" &>/dev/null; then
    echo "The package '$PACKAGE' is installed."
    exit 0
else
    echo "The package '$PACKAGE' is not installed."
    exit 1
fi

