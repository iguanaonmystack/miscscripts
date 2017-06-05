#!/bin/bash -e

bash -x /home/flexo/bin/extend-noextend.sh
xrandr --dpi 168
xfconf-query -c xsettings -p /Xft/DPI -s 168
gsettings set org.gnome.desktop.interface scaling-factor 2

# Settings:
xmodmap /home/flexo/.Xmodmap.laptop

xrandr --output DP-3-2 --off

# WM:
killall --user $USER notion || true
notion -session undocked &
