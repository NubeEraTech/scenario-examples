#!/bin/bash
[ -z "$(lsof -i :8080)" ] && exit 0 || exit 1
