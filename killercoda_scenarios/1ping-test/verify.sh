#!/bin/bash
ping -c 1 google.com >/dev/null 2>&1 && exit 0 || exit 1
