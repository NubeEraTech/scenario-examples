#!/bin/bash
stat -c "%U" /etc/testfile.txt | grep -q "testuser" && exit 0 || exit 1
