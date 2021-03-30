#!/usr/bin/env python3
from __future__ import print_function
import sys
from urllib.parse import unquote
try:
    from shlex import quote
except ImportError:
    from pipes import quote

for line in sys.stdin:
    line = line.strip()
    if line.startswith('http') and line.split(' ', 1)[0].lower().endswith('.jpg'):
        path = unquote(line.split(' ', 1)[0]).split('/', 3)
        if len(path) > 3:
            filepath = path[3]
            if '.small.' in filepath:
                newpath = filepath.replace('.small.', '.lj.')
            elif '.thumb.' in filepath:
                newpath = filepath.replace('.thumb.', '.lj.')
                filepath = filepath.replace('.thumb.', '.small.')
            elif '.lj.' in filepath:
                newpath = filepath
                filepath = filepath.replace('.lj.', '.')
            else:
                newpath = filepath[:-4] + '.lj' + filepath[-4:]
            print('convert', quote(filepath), '-scale 1200', quote(newpath))

