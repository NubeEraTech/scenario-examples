#!/bin/bash
python3 -c "def greet(): print('Hello!'); greet()" | grep 'Hello!'