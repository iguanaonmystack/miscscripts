#!/bin/sh
# extend non-HiDPI external display on DP* to left of HiDPI internal display eDP*
# and make external display the primary.
#
# Modified from https://gist.github.com/wvengen/178642bbc8236c1bdb67
#
# see also https://wiki.archlinux.org/index.php/HiDPI
# you may run into https://bugs.freedesktop.org/show_bug.cgi?id=39949
#                  https://bugs.launchpad.net/ubuntu/+source/xorg-server/+bug/883319
#
# Reset external monitor scale to 1x1 before running this again or it will calculate
# based on the virutal pixel size rather than the original.

EXT_DPI=96
INT_DPI=192
EXT_SCALE=`python -c "print(float($EXT_DPI) / float($INT_DPI))"`

EXT=`xrandr --current | sed 's/^\(.*\) connected.*$/\1/p;d' | grep -v ^eDP | head -n 1`
INT=`xrandr --current | sed 's/^\(.*\) connected.*$/\1/p;d' | grep -v ^DP | head -n 1`

ext_w=`xrandr | sed 's/^'"${EXT}"' [^0-9]* \([0-9]\+\)x.*$/\1/p;d'`
ext_h=`xrandr | sed 's/^'"${EXT}"' [^0-9]* [0-9]\+x\([0-9]\+\).*$/\1/p;d'`
int_w=`xrandr | sed 's/^'"${INT}"' [^0-9]* \([0-9]\+\)x.*$/\1/p;d'`
off_w=`python -c "print(int($EXT_SCALE * $ext_w))"`

xrandr --output "${EXT}" --primary --scale 1x1  --output "${INT}" --scale ${EXT_SCALE}x${EXT_SCALE} --right-of $EXT
