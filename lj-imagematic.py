#!/usr/bin/env python
"""Script to format my Dreamwidth/Livejournal entries consistently"""
import sys
from cgi import escape

img_fmt_start = '<figure style="border: 2px solid black; width: 600px;"><a href="%s"><img src="%s" style="display: block;" width="600" /></a>'
caption_fmt = '<figcaption style="text-align: center; border-top: 2px solid black; background-color: #ddd; padding: 0.5ex;">%s</figcaption>'
img_fmt_end = '</figure>'
thumb_fmt = '<a href="%s"><img src="%s" style="border: 2px solid black; float: left; margin: 0 1em 1em 0;" /></a>'
first_header = True

for line in sys.stdin:
    line = line.strip()
    if line.startswith('http'):
        if ' ' in line:
            imgurl, caption = line.split(' ', 1)
        else:
            imgurl = line
            caption = None
        linkurl = imgurl
        if '.small.' in imgurl:
            imgurl = imgurl.replace('.small.', '.lj.')
        elif '.thumb.' in imgurl:
            imgurl = imgurl.replace('.thumb.', '.lj.')
            linkurl = imgurl.replace('.thumb.', '.small.')
        elif '.lj.' in imgurl:
            linkurl = imgurl.replace('.lj.', '.small.')
        else:
            linkurl = imgurl[:-4] + '.small' + imgurl[-4:]
            imgurl = imgurl[:-4] + '.lj' + imgurl[-4:]
        line = img_fmt_start % (linkurl, imgurl)
        if caption:
            line += caption_fmt % (caption,)
        line += img_fmt_end
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
