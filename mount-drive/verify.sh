#!/bin/bash
mount | grep -q "/mnt/drive" && exit 0 || exit 1
