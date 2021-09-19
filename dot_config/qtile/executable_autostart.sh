#!/usr/bin/bash
nitrogen --set-auto ~/.local/share/wallpapers/arch.png &
while [[ "$DISPLAY" != ":0" ]]; do echo "wait";done
xrandr --output eDP-1 --scale 1.5x1.5
