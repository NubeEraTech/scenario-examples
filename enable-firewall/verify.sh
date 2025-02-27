#!/bin/bash
ufw status | grep -q "Status: active" && exit 0 || exit 1
