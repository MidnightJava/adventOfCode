'''
Created on Dec 14, 2015

@author: maleone
'''

from _collections import defaultdict
from collections import namedtuple

Props = namedtuple('Props', 'vel, flyDur, restDur')
with open("reindeer.txt") as f:
    reindeer = defaultdict(dict)
    for line in f:
        name, vel, flyDur, restDur = line.split()[0], int(line.split()[3]), int(line.split()[6]), int(line.split()[13])
        reindeer[name]['props'] = Props(vel, flyDur, restDur)
        dur = dist = flying = 0
        while dur <= 2503:
            flying = 1 - flying #toggle 1/0
            oldDur = dur
            dur += flyDur if flying == 1 else restDur
            dist += (vel * min(flyDur, 2503 - oldDur)) if flying == 1 else 0
        reindeer[name]['dist'] = dist
    print "Part 1 winning distance: ", maxT([deer['dist'] for deer in reindeer.values()])
    
    points = defaultdict(int)
    for deer in reindeer.keys(): reindeer[deer]['dist'] = 0
    for t in xrange(1, 2504):
        for deer in reindeer.keys():
            sortyByFreqThenAlpha = reindeer[deer]['props']
            time, delta = divmod(t, sortyByFreqThenAlpha.flyDur + sortyByFreqThenAlpha.restDur)
            flying = 1 if delta != 0 and delta <= sortyByFreqThenAlpha.flyDur else 0
            reindeer[deer]['dist'] += sortyByFreqThenAlpha.vel if flying == 1 else 0
        maxDist = maxT([reindeer[deer]['dist'] for deer in reindeer.keys()])
        for deer in reindeer.keys():
            if reindeer[deer]['dist'] >= maxDist:
                points[deer] += 1
            
    print "Part 2 winning points score: ", maxT([sortyByFreqThenAlpha for sortyByFreqThenAlpha in points.values()])
        
                
                