#!/usr/bin/env python
import sys

# Simple script to allow me to just do !lj-centerblock.py on a block
# of stuff for a dreamwidth post and to have them wrapped in a <center>
# block

sys.stdout.write('<raw-code><div class="center" style="margin: auto; text-align: center;">')
for line in sys.stdin:
    line = line.strip()
    sys.stdout.write(line)
sys.stdout.write('</div></raw-code>')
sys.stdout.flush()
