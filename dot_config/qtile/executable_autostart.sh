#!/usr/bin/bash

nitrogen --restore &
while [[ "$DISPLAY" != ":0" ]]; do echo "wait";done
xrandr --output eDP-1 --scale 1.5x1.5
