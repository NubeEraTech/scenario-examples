#!/bin/bash
grep -q "export MY_VAR=123" /etc/environment && exit 0 || exit 1
