#!/bin/sh

pactl load-module module-null-sink sink_name="Null Sink"

# now choose 'Null Sink' in pavucontrol for the Playback device to loop
# and the Recording device to loop.
