#!/usr/bin/env python
"""Script to format my Dreamwidth/Livejournal entries consistently"""
import sys
from cgi import escape

img_fmt = '<a href="%s"><img src="%s" style="border: 2px solid black;" /></a>'
thumb_fmt = '<a href="%s"><img src="%s" style="border: 2px solid black; float: left; margin: 0 1em 1em 0;" /></a>'
first_header = True

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
        line = img_fmt % (linkurl, imgurl)
    elif line.startswith('Header: '):
        header = line[len('Header: '):]
        line = ''
        if not first_header:
            line += '</div></cut>\n'
        line += '<cut text="' + escape(header) + '">'
        line += '<div style="width: 604px; margin: 0 auto;">'
        line += '<strong>' + header + '</strong>'
        first_header = False
    elif line.startswith('Thumbnail: '):
        imgurl = linkurl = line = line[len('Thumbnail: '):]
        if '.small.' in line:
            imgurl = line.replace('.small.', '.thumb.')
        elif '.thumb.' in line:
            linkurl = line.replace('.thumb.', '.small.')
        elif '.lj.' in line:
            imgurl = line.replace('.lj.', '.thumb.')
            linkurl = line.replace('.lj.', '.small.')
        else:
            linkurl = line[:-4] + '.small' + line[-4:]
            imgurl = line[:-4] + '.thumb' + line[-4:]
        line = thumb_fmt % (linkurl, imgurl)

    print line
print '</div></cut>'
