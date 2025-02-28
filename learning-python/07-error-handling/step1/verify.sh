#!/bin/bash
python3 -c "try: result=10/0 except ZeroDivisionError: print('Cannot divide by zero')" | grep 'Cannot divide by zero'