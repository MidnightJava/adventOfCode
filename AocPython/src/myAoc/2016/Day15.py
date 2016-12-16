'''
Created on Dec 16, 2016

@author: maleone
'''

import re


def a(x):
    print x.type, x

with open("data/day15") as f:
    data = []
    for line in f:
        line = line.strip()
        data.append(map(lambda x : (int(x[0]), int(x[1])), re.findall(r".*(\d+)\s+positions.*at\s+position\s+(\d+).", line))[0])
    
    for d in data:
        print "num pos: %s current pos: %s" % d
        
    t = 0
    done = None
    while not done or done != [True]*len(data):
        done = [False]*len(data)
        for i in xrange(1, len(data) + 1):
            done[i-1] = ((data[i-1][1] + i - t) % data[i-1][0] == 0)
            print done, done.count(True)
        t += 1
    print t-1