#!/usr/bin/env python
import sys

# Simple script to allow me to just copy image links into vim
# and have this script turn them into actual images.

fmt = '<a href="%s"><img src="%s" style="border: 2px solid black;" /></a>'

for line in sys.stdin:
    line = line.strip()
    if line.startswith('http') and line.lower().endswith('.jpg'):
        imgurl = linkurl = line
        if '.small.' in line:
            imgurl = line.replace('.small.', '.lj.')
        elif '.thumb.' in line:
            imgurl = line.replace('.thumb.', '.lj.')
            linkurl = line.replace('.thumb.', '.small.')
        elif '.lj.' in line:
            linkurl = line.replace('.lj.', '.small.')
        else:
            linkurl = line[:-4] + '.small' + line[-4:]
            imgurl = line[:-4] + '.lj' + line[-4:]
        line = fmt % (linkurl, imgurl)
    print line
