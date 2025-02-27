#!/bin/bash

# Run uptime command and store the output
USER_UPTIME=$(history | grep 'uptime' | tail -1)

# If the uptime command was run, the verification succeeds
if [[ -n "$USER_UPTIME" ]]; then
    echo "Success: System uptime command executed."
    exit 0
else
    echo "Error: You did not run the uptime command."
    exit 1
fi

