"""
Input represents successive depth soundings of concentric circles
from your present position.

Part 1: Determine the number fo times the depth increases from its previous measurement.

Part 2: Consider successive sliding windows of three measurements. Determine the number
of times the sum of measurements in a sliding window increases from the sum of measurements
in the previous sliding window.
"""

with open('2021/data/day01') as f:
    prev = None
    count = 0
    for m in f:
        n = int(m)
        if prev and n > prev: count+= 1
        prev = n

print("Part 1: %d"  % count)

count = 0
measurements = [int(m.strip()) for m in open('2021/data/day01').readlines()]
for i in xrange(3, len(measurements) + 1):
    if sum(measurements[i-2: i+1]) > sum(measurements[i-3: i]): count+= 1
    
print('Part 2: %d' % count)

# Part 1: 1226
# Part 2: 1252