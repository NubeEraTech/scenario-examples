#!/bin/bash
ufw status | grep -q "Status: inactive" && exit 0 || exit 1
