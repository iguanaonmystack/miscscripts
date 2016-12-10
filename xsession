#!/bin/bash

export PATH=/home/flexo/bin:$PATH

# xfsettingsd ensures that apps are updated when changeing xfconf settings:
xfsettingsd --replace

# Docked or undocked specialisation, mostly regarding DPI settings:
CONNECTED=$(xrandr | grep ' connected' -c)
if [[ "$CONNECTED" -eq 2 ]]; then
    SESSION=docked
    bash -x /home/flexo/bin/extend-extnative.sh
    xfconf-query -c xsettings -p /Xft/DPI -s 96
    gsettings set org.gnome.desktop.interface scaling-factor 1
    digiguide &
else
    SESSION=undocked
    xrandr --dpi 168
    xfconf-query -c xsettings -p /Xft/DPI -s 168
    gsettings set org.gnome.desktop.interface scaling-factor 2

    # There has got to be a better way than this....
    # vncdesk: https://github.com/feklee/vncdesk
    /home/flexo/.local/bin/vncdesk 2 & #digiguide &
fi

# Tray applets:
xfce4-power-manager &
pasystray &
nm-applet &

# The tray itself:
stalonetray -i 32 &

# Settings:
/usr/bin/xmodmap /home/flexo/.Xmodmap
#/usr/bin/xbindkeys -f /home/flexo/.xbindkeysrc.noauto

# Other background programs:
redshift -l 51.4155:0.0501 -t 6400:5400 &
sshfs elzar.nevira.net:notes ~/notes
sshfs elzar.nevira.net:misc ~/misc

# UIs:
xfce4-terminal &
x-www-browser 2> /dev/null &

# Aaaaand finally:
notion -session "$SESSION"

if [ "$SESSION" == "undocked" ]; then
    # Quitting vncdesk won't quit Digiguide on the created Xserver
    killall DigiGuide.exe
fi
