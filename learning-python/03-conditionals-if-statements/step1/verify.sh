#!/bin/bash
python3 -c "x=7; print('x is greater than 5' if x > 5 else '')" | grep 'x is greater than 5'