#!/bin/bash
[ -f "/etc/testfile.txt" ] && exit 0 || exit 1
