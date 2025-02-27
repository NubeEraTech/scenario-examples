#!/bin/bash
LINK="/etc/mylink"; TARGET="/etc/abc"; [ -L "$LINK" ] && [ "$(readlink "$LINK")" == "$TARGET" ] && exit 0 || exit 1
