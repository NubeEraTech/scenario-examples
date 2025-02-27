#!/bin/bash
systemctl is-active --quiet apache2 && exit 0 || exit 1
