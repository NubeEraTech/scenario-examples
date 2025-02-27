#!/bin/bash
id testuser | grep -q "devgroup" && exit 0 || exit 1
