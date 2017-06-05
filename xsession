#!/bin/bash

export PATH=$HOME/bin:$PATH

# xfsettingsd ensures that apps are updated when changing xfconf settings:
xfsettingsd --replace

# Docked or undocked specialisation, mostly regarding DPI settings:
CONNECTED=$(xrandr | grep ' connected' -c)
if [[ "$CONNECTED" -eq 2 ]]; then
    export SESSION=docked
    bash -x $HOME/bin/docked.sh
else
    export SESSION=undocked
    bash -x $HOME/bin/undocked.sh
fi
sleep 1

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

# Other background programs and mountpoints:
ps x | grep -q [r]edshift || redshift -l 51.4155:0.0501 -t 6400:2300 &
sshfs elzar.nevira.net:notes ~/notes &
sshfs elzar.nevira.net:misc ~/misc &
mount /mnt/cloudbox/storage/ &
mount /mnt/cloudbox/Shared/ &

# UIs:
digiguide &
echo "starting xfce-terminal"
xfce4-terminal --role=initial -x mosh elzar.nevira.net &
echo "started"
x-www-browser 2> /dev/null &

# Sentinel
while true; do
    if ps x | grep -q [n]otion
    then
        #echo 'running'
        sleep 2
        continue
    else
        sleep 1
        if ps aux | grep -q [n]otion
        then
            echo 'just running'
            continue
        else
            echo 'not running'
            break
        fi
    fi
done

