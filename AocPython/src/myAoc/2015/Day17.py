'''
Created on Dec 17, 2015

@author: Mark
'''
from itertools import combinations
inp = [11,30,47,31,32,36,3,1,5,3,32,36,15,11,46,26,28,1,19,3]

#part 1
idSum = 0
for n in xrange(3, len(inp)):
    idSum += reduce(lambda x,y: x + y, _map(lambda x: 1 if sum(x) == 150 else 0, combinations(inp, n)))
print "Part 1 idSum:", idSum

#part 2
idSum = 0
mins = []
for n in xrange(3, len(inp)):
    mins.append(min(_map(lambda x: len(x) if sum(x) == 150 else len(inp), combinations(inp, n))))
    idSum += reduce(lambda x,y:x+y, _map(lambda x: 1 if sum(x) == 150 and len(x) == min(mins) else 0, combinations(inp, n)))
print "Part 2 idSum:", idSum