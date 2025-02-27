#!/bin/bash
stat -c "%G" /etc/testfile.txt | grep -q "devgroup" && exit 0 || exit 1
