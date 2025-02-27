#!/bin/bash
getent passwd | grep -q "testuser" && exit 0 || exit 1
