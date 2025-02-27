#!/bin/bash

# Get uptime
UPTIME=$(uptime -p)

# Check if uptime command provides output
if [ -n "$UPTIME" ]; then
    echo "System uptime: $UPTIME"
else
    echo "Failed to retrieve uptime."
fi
