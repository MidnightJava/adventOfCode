'''
Created on Dec 8, 2015

@author: maleone
'''

import re

def memChars(l):
    l = l[1:-1]
    count = 2
    count += len(re.findall(r"\\\"|\\\\", l))
    count += 3 * len(re.findall(r"\\x[0-9a-f]{2}", l))
    return count

def countEscape(c):
    if c =="\\" or c == "\"":
        return True
    return False

p1 = p2 = 0 
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        p1+= memChars(line)
        p2 += len(filter(countEscape, line)) + 2
print "p1:", p1
print "p2:", p2

