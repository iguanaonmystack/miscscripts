#!/usr/bin/env python
import sys

fmt = '<a href="%s"><img src="%s" /></a>'

for line in sys.stdin:
    line = line.strip()
    if line.startswith('http') and line.lower().endswith('.jpg'):
        if '.small.' in line:
            line = fmt % (line, line.replace('.small.', '.thumb.'))
        elif '.thumb.' in line:
            line = fmt % (line.replace('.thumb.', '.small.'), line)
    print line

