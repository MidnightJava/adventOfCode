'''
Created on Dec 25, 2015

@author: Mark
'''
from _collections import defaultdict
from itertools import combinations
#Main insight that I was missing for a while is that you only
#need to consider the smallest group. This reduces greatly
#the combinatorial possibilities that need to be analyzed

# numgroups = 3 # part 1
numgroups = 4 # part 2

weights = []
combos = []
with open("day24input") as f:
    for line in f.readlines():
        weights.append(int(line.strip()))

minLength = None
minVals = defaultdict(list)
for i in xrange(1, len(weights) // numgroups):
    combos = combinations(weights, i)
    for c in combos:
        if sum(c) == sum(weights) // numgroups:
            if not minLength or len(c) < minLength:
                minLength = len(c)
                minVals[minLength].append(reduce(lambda x,y: x*y, c))

print min(minVals[minLength]) 

            
