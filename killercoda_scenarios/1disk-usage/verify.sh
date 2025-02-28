#!/bin/bash
df -h | grep -q "/" && exit 0 || exit 1
