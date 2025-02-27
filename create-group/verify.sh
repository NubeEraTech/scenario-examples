#!/bin/bash
getent group devgroup >/dev/null && exit 0 || exit 1
