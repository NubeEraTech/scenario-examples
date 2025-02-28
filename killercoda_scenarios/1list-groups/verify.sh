#!/bin/bash
getent group | grep -q "devgroup" && exit 0 || exit 1
