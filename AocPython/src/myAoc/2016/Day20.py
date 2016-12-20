'''
Created on Dec 20, 2016

@author: maleone
'''

import re

sortedIntervals = []

def merge_intervals(intervals):
    global sortedIntervals
    sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
    merged = []
    
    for higher in sorted_by_lower_bound:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            # test for intersection between lower and higher:
            # we know via sorting that lower[0] <= higher[0]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)  # replace by merged interval
            else:
                merged.append(higher)
    return merged

with open("data/day20") as f:
    data = []
    for line in f:
        lo,hi = re.findall("(\d+)\-(\d+)", line)[0]
        if int(lo) >= (hi):
            print "data error",lo,hi
        data.append(( int(lo), int(hi) ))
#     data = [(5, 7), (50, 60), (3, 6), (10, 12), (6, 12), (10, 20)]
    sortedIntervals = merge_intervals(data)

allowed = 0
#Part 1
for i in xrange(len(sortedIntervals) - 1):
    if sortedIntervals[i+1][0] - sortedIntervals[i][1] > 1:
        print "Lowest allowed", sortedIntervals[i][1] +1
        break;
#Part 2
for i in xrange(len(sortedIntervals) - 1):
    if sortedIntervals[i+1][0] - sortedIntervals[i][1] > 1:
        allowed+= (sortedIntervals[i+1][0] - sortedIntervals[i][1] -1)

print "Total allowed", allowed
    
