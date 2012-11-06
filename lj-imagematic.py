#!/usr/bin/env python
import sys

# Simple script to allow me to just copy image links into vim
# and have this script turn them into actual images.

fmt = '<a href="%s"><img src="%s" /></a>'

for line in sys.stdin:
    line = line.strip()
    if line.startswith('http') and line.lower().endswith('.jpg'):
        if '.small.' in line:
            line = fmt % (line, line.replace('.small.', '.thumb.'))
        elif '.thumb.' in line:
            line = fmt % (line.replace('.thumb.', '.small.'), line)
    print line

