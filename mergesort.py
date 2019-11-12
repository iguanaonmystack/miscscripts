#!/usr/bin/env python3
# Implementation of mergesort with user prompts.
#
# Copyright (c) 2006, 2010, 2019 Kathy Murdoch
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys

def mergesort(list):
    """Merge-sorts a list, giving the user prompts
    Returns a list with the user's preferences,
    sorted with their favourites at the end of the list"""
    length = len(list)
    left = []
    right = []
    if length <= 1:
        return list
    else:
        middle = list[length//2]
        for item in list:
            if item is middle:
                pass
            else:
                try:
                    choice = int(input(middle + " or " + item + "? "))
                except ValueError:
                    choice = 2
                if choice == 1: # if < middle
                    left = left + [item]
                else:            # if > middle
                    right = right + [item]
        left = mergesort(left)
        right = mergesort(right)
        return left + [middle] + right

def usage():
    return "Usage: %s <item1> <item2> <item3> ..." % sys.argv[0]

if __name__ == "__main__":
    
    list = sys.argv[1:]
    if not list or list[0] in ('-h', '--help'):
        sys.exit(usage())

    print('Type 1 if you prefer the first film given,')
    print('or 2 if you prefer the second.')
    print()
    
    newlist = mergesort(list)

    print()

    i = 1
    length = len(newlist)
    while i <= length:
        print(str(i) + ": " + newlist[length - i])
        i = i + 1

