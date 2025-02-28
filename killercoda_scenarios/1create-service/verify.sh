#!/bin/bash
systemctl list-unit-files | grep -q "mycustom.service" && exit 0 || exit 1
