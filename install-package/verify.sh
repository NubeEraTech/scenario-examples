#!/bin/bash
if dpkg -l | grep -q "^ii  curl "; then
    echo "The package 'curl' is installed."
    exit 0
else
    echo "The package 'curl' is not installed."
    exit 1
fi
