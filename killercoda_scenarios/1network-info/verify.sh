#!/bin/bash
ip addr show | grep -q "inet " && exit 0 || exit 1
