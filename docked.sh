#!/bin/bash -e

bash -x /home/flexo/bin/extend-extnative.sh
xrandr --output eDP-1 --off
xrandr --dpi 96
xfconf-query -c xsettings -p /Xft/DPI -s 96
gsettings set org.gnome.desktop.interface scaling-factor 1

# Settings:
xmodmap /home/flexo/.Xmodmap.desktop

# WM:
killall --user $USER notion || true
notion -session docked &
