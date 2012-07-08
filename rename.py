#!/usr/bin/python

import os
import sys

files = []
pad = 2 # default padding for output filename numbering.
startAt = 1 # value of suffix of first renamed file in a batch.
version = """rename 0.5.1
Copyright (C) 2005 Nick Murdoch."""

# Process options
i = 0
while i < len(sys.argv):
	i = i + 1 # i originally 0, for block starts at 1, so we're okay.
	arg = sys.argv[i]
	if arg == "-h" or arg == "--help":
		print """\
Usage: rename SOURCE DEST
  or:  rename SOURCES DESTPREFIX
Rename SOURCE to DEST, or batch rename SOURCES specified to DESTPREFIXi, where i is a consecutive number.

  -p  --pad      set the padding of the appended sequence number.
                   Not implemented yet.
  -f  --first    set the first sequence number to use
  -h, --help     display this help and exit
  -v, --version  output version information and exit
"""
		sys.exit(0)
	elif arg == "-v" or arg == "--version":
		print version
		sys.exit(0)
	elif arg.startswith("-"):
		if arg == "-f" or arg == "--first":
			try:
				startAt = int(sys.argv[i+1])
				i = i + 1
			except:
				sys.stderr.write("rename: parameter for -f must be an integer")
				sys.exit(1)
		else:
			sys.stderr.write("rename: unrecognised option `" + arg + "'\nTry --help for more information.\n")
			sys.exit(1)
	elif arg == sys.argv[0]:
		pass
	else: 
		break # finish processing options



# expect at least two further arguments (ie, the filnames).
if len(sys.argv) <= i + 2:
	sys.stderr.write("rename: not enough parameters\nTry `rename --help' for more information.\n")
	sys.exit(1)



oldfilenames = sys.argv[i:-1]
newfileprefix = sys.argv[-1]

if len(oldfilenames) == 1:
	os.rename(oldfilenames[0], newfileprefix)
	sys.exit(0)
else:
	for file in oldfilenames:
		fileextension = ""
		if file.find(".") != -1:
			fileextension = file[file.find("."):]
		os.rename(file, newfileprefix + str(startAt).zfill(pad) + fileextension)
		startAt = startAt + 1
	sys.exit(0)

