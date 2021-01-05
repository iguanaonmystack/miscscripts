#!/bin/bash -e

DEVICEID=$(xsetwacom --list devices | grep STYLUS | cut -f 2 | cut -d ' ' -f 2)
ERASERID=$(xsetwacom --list devices | grep ERASER | cut -f 2 | cut -d ' ' -f 2)
DISPLAYID=$(xrandr  | grep ' connected primary' | cut -d ' ' -f 1)
DISPLAYID=${DISPLAYID:-eDP-1}

xsetwacom --set "$DEVICEID" ResetArea

INITIAL_AREA=$(xsetwacom --get "$DEVICEID" Area)
NEW_AREA=$(python3 -c '
import sys
coords = [int(v) for v in sys.argv[1:]]
height = coords[3]
coords[1] = height // 4
coords[3] = height // 4 + (height // 2)
coords[2] = coords[2] // 2
sys.stdout.write(" ".join((str(c) for c in coords)))
' $INITIAL_AREA)

# Set usable area of tablet to just half X and half Y (ie, top left corner)
xsetwacom --set "$DEVICEID" Area $NEW_AREA
xsetwacom --set "$ERASERID" Area $NEW_AREA

# Set wacom to map only to primary display
xsetwacom --set "$DEVICEID" MapToOutput "$DISPLAYID"

# Press+tap side buttons to middle/right click rather than hover+tap
# (not needed any more)
#xsetwacom --set "$DEVICEID" TabletPCButton on

# Set eraser (button 1) to be right mouse click (button 3)
xsetwacom --set "$ERASERID" Button 1 3


