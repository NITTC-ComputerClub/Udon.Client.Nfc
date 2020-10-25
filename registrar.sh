#!/bin/sh
ps aux | grep python3 | grep -v grep | awk '{ print "kill -9", $2 }' | sh
python3 ./clients/registrar.py
