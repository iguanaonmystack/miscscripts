#!/usr/bin/env python
from __future__ import print_function
import sys
try:
    from shlex import quote
except ImportError:
    from pipes import quote

for line in sys.stdin:
    line = line.strip()
    if line.startswith('http') and line.split(' ', 1)[0].lower().endswith('.jpg'):
        path = line.split(' ', 1)[0].split('/', 3)
        if len(path) > 3:
            filepath = path[3]
            if '.small.' in filepath:
                newpath = filepath.replace('.small.', '.lj.')
            elif '.thumb.' in filepath:
                filepath = filepath.replace('.thumb.', '.small.')
                newpath = filepath.replace('.thumb.', '.lj.')
            elif '.lj.' in filepath:
                newpath = filepath
                filepath = filepath.replace('.lj.', '.')
            else:
                newpath = filepath[:-4] + '.lj' + filepath[-4:]
            print('convert', quote(filepath), '-scale 600', quote(newpath))

