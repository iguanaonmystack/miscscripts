#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    if line.startswith('http') and line.lower().endswith('.jpg'):
        path = line.split('/', 3)
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
            print 'convert', filepath, '-scale 600', newpath

