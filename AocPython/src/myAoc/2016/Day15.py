'''
Created on Dec 16, 2016

@author: maleone
'''

import re


def a(x):
    print x.type, x

data = []
with open("data/day15") as f:
    i = 0
    for line in f:
        line = line.strip()
        data.append(map(lambda x : (int(x[0]), int(x[1])), re.findall(r"[^\d](\d+)\s+positions.*at\s+position\s+(\d+).", line))[0])
    
    for i in xrange(len(data)):
        data[i] = (data[i][0], (data[i][1] + i + 1) % data[i][0])
        print "Number: %d  Position: %d" % data[i]
        i+=1
        
    for i in [1, 0]:
        maxT = 0
        t = 0
        done = None
        dataLen = len(data) -i
        while not done or done != [True]*dataLen:
            done = [False]*dataLen
            for i in xrange(dataLen):
                done[i] = ((data[i][1] + t) % data[i][0] == 0)
                if done.count(True) > maxT:
                    maxT = done.count(True)
                    print maxT, "disks aligned"
            t += 1
        print "Time:", t-1
    
    #Part1 121834
    #Part 2 3208099