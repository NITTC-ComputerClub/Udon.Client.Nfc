#!/bin/bash
ps aux | grep python3 | grep -v grep | awk '{ print "kill -9", $2 }' | sh
/usr/bin/python3 /home/pi/Desktop/Git/Udon.Client.Nfc/scripts/main.py & xdg-open /home/pi/Desktop/Git/Udon.Client.Nfc/clients/main.html;
