'''
Created on Dec 1, 2016

@author: Mark
'''

from functools import reduce
from collections import defaultdict
import re
direction = 0
visits = defaultdict(list)
done = False

def checkDone(x, y):
    global done
    if not done and y in visits[x]:
        print "PART 2:", x, y
        done = True

def p(cum, pos):
    global direction, visits
    m = re.search("([LR])(\d+)", pos.strip())
    direc = m.group(1)
    mag = int(m.group(2))
    if direc == "L":
        direction = (direction + 3) % 4
    elif direc == "R":
        direction = (direction + 1) % 4
        
    if direction == 0:
        for x in xrange(1, mag+1):
            checkDone(cum[0], cum[1] + x)
            visits[cum[0]].append(cum[1] + x)
        cum[1]+= mag
    elif direction == 2:
        for x in xrange(1, mag+1):
            checkDone(cum[0], cum[1] - x)
            visits[cum[0]].append(cum[1] - x)
        cum[1]-= mag
    elif direction == 1:
        for x in xrange(1, mag+1):
            checkDone(cum[0] + x, cum[1])
            visits[cum[0] + x].append(cum[1])
        cum[0]+= mag
    elif direction == 3:
        for x in xrange(1, mag+1):
            checkDone(cum[0] - x, cum[1])
            visits[cum[0] - x].append(cum[1])
        cum[0]-= mag
        
    return cum

with open("data/day01") as f:
    for line in f:
        res = reduce(lambda x,y: p(x,y), line.split(","), [0,0])
        print(res[0] + res[1])
    
