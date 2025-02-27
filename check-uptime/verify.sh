#!/bin/bash

# Check if the user ran the 'uptime' command (without executing it)
if history | grep -qE '^\s*[0-9]+\s+uptime\b'; then
    echo "Success: System uptime command executed."
    exit 0
else
    echo "Error: You did not run the uptime command."
    exit 1
fi
