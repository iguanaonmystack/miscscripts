#!/usr/bin/env python3
"""Script to format my Dreamwidth/Livejournal entries consistently"""
import sys
from html import escape

img_fmt_start = '<figure style="border: 2px solid black; width: 600px; margin: 0; background: url(\'%s\'); background-size: cover; background-position: center; overflow: hidden;"><a href="%s"><img src="%s" style="display: block; max-width: 600px; max-height: 400px; margin-left: auto; margin-right: auto; box-shadow: 0 0 150px 150px rgba(0,0,0,1);" /></a>'
caption_fmt = '<figcaption style="text-align: center; border-top: 2px solid black; background-color: #ddd; padding: 0.5ex;">%s</figcaption>'
img_fmt_end = '</figure>'
thumb_fmt = '<a href="%s"><img src="%s" style="border: 2px solid black; float: left; margin: 0 1em 1em 0;" width="200" height="300" /></a>'
first_header = True
current_thumbnail = False
after_thumbnail = False

for line in sys.stdin:
    line = line.strip()
    end = '\n'
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
            linkurl = imgurl.replace('.thumb.', '.small.')
            imgurl = imgurl.replace('.thumb.', '.lj.')
        elif '.lj.' in imgurl:
            linkurl = imgurl.replace('.lj.', '.small.')
        else:
            linkurl = imgurl[:-4] + '.small' + imgurl[-4:]
            imgurl = imgurl[:-4] + '.lj' + imgurl[-4:]
        line = img_fmt_start % (imgurl, imgurl, imgurl)
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
        end = ''
        current_thumbnail = True

    if after_thumbnail:
        if not line.strip():
            line = ''
            end = ''
        else:
            after_thumbnail = False

    print(line, end=end)

    if current_thumbnail:
        after_thumbnail = True
        current_thumbnail = False
print('</div></cut>')
