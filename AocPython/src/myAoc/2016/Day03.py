'''
Created on Dec 2, 2016

@author: maleone
'''

from __future__ import print_function

def checkTriange(t):
    for x in xrange(0, 3):
        if int(t[x]) >= sum([int(t[(x+1) % 3]), int(t[(x+2) % 3])]):
            return False;
    return True
        
with open("data/day03") as f:
    count = 0
    print("Part 1: ", end="")
    for line in f:
        t = line.split()
        if checkTriange(line.split()):
            count+= 1
    print(count)
    
with open("data/day03") as f:
    count = 0
    print("Part 2: ", end="")
    trans = [x.split() for x in f]
    for z in zip(*trans):
        for t in zip(*[iter(z)]*3):
            if checkTriange(t):
                count += 1
    print(count)