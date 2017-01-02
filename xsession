#!/bin/bash

export PATH=/home/flexo/bin:$PATH

# xfsettingsd ensures that apps are updated when changing xfconf settings:
xfsettingsd --replace

# Docked or undocked specialisation, mostly regarding DPI settings:
CONNECTED=$(xrandr | grep ' connected' -c)
if [[ "$CONNECTED" -eq 2 ]]; then
    export SESSION=docked
    bash -x /home/flexo/bin/extend-extnative.sh
    xfconf-query -c xsettings -p /Xft/DPI -s 96
    gsettings set org.gnome.desktop.interface scaling-factor 1
else
    export SESSION=undocked
    xrandr --dpi 168
    xfconf-query -c xsettings -p /Xft/DPI -s 168
    gsettings set org.gnome.desktop.interface scaling-factor 2
fi

# Tray applets:
/home/flexo/subversion/phwmon/phwmon.py --cpu &
xfce4-power-manager --restart &
pasystray &
nm-applet &

# The tray itself:
stalonetray -i 32 &

# Settings:
syndaemon -d -i 0.5 -K -R # disable touchpad while typing
#/usr/bin/xbindkeys -f /home/flexo/.xbindkeysrc.noauto
if [ "$SESSION" == "undocked" ]; then
    xmodmap /home/flexo/.Xmodmap.laptop
else
    xmodmap /home/flexo/.Xmodmap.desktop
fi

# Other background programs and mountpoints:
redshift -l 51.4155:0.0501 -t 6400:5400 &
sshfs elzar.nevira.net:notes ~/notes
sshfs elzar.nevira.net:misc ~/misc
mount /mnt/cloudbox/storage/
mount /mnt/cloudbox/Shared/

# UIs:
digiguide &
xfce4-terminal &
x-www-browser 2> /dev/null &

# Aaaaand finally:
notion -session "$SESSION"

if [ "$SESSION" == "undocked" ]; then
    # Quitting vncdesk won't quit Digiguide on the created Xserver
    killall DigiGuide.exe
fi
