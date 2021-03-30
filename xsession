#!/bin/bash

echo "starting xsession..."
export PATH=$HOME/bin:$PATH

xterm &

# xfsettingsd ensures that apps are updated when changing xfconf settings:
xfsettingsd --replace & sleep 3

echo "Started xfsettingsd"

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
$HOME/subversion/phwmon/phwmon.py --cpu &
xfce4-power-manager --restart &
pasystray &
nm-applet &

# The tray itself:
stalonetray -i 32 &

# Settings:
#syndaemon -d -i 0.5 -K -R # disable touchpad while typing
syndaemon -d -i 0.4 -K -R # disable touchpad while typing
#/usr/bin/xbindkeys -f $HOME/.xbindkeysrc.noauto
xrdb $HOME/.Xresources

# Other background programs and mountpoints:
#redshift -l 51.4155:0.0501 -t 6400:2600 &
redshift -l 50.6433:-3.6397 -t 6400:2600 &
sshfs elzar.nevira.net:notes ~/notes &
sshfs elzar.nevira.net:misc ~/misc &
mount /mnt/cloudbox/storage/ &
mount /mnt/cloudbox/Shared/ &
DISPLAY=:0 qjoypad &
dropbox start &

# UIs:
#digiguide &
echo "starting terminal"
#xfce4-terminal --role=initial -x mosh elzar.nevira.net &
urxvt -fn xft:Monospace:size=17,xft:Symbola -name toprightterm &
echo "started"
x-www-browser 2> /dev/null &

# Exit tasks
function finish {
    killall --user $USER redshift
}
trap finish EXIT

# Sentinel
while true; do
    if ps x | grep -q [n]otion
    then
        #echo 'running'
        sleep 2
        continue
    else
        sleep 1
        if ps x | grep -q [n]otion
        then
            echo 'just running'
            continue
        else
            echo 'not running'
            break
        fi
    fi
done

