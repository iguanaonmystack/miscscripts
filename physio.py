#!/usr/bin/env python
import sys
import time

def beep():
    sys.stdout.write('\a')
    sys.stdout.flush()

for i in range(6):
    for j in range(10):
        for k in range(5):
            print i + 1, j + 1, k + 1
            beep()
            if k == 4 and j == 9:
                time.sleep(0.2)
                beep()
            time.sleep(1)
        time.sleep(1)
    time.sleep(4)
