"""
The input represents the horizontal positions of sme crab submarines.
Find the way toget them all at the same position using the least
amount of fuel possible. Report the total fuel used by all the submarines.

Part 1: Movement from one horizontal position to the next takes one unit of fuel.

Part 2: While moving from a starting point to an end point, tghe first step takes
one unit of fuel, and each successive step takes one more step than the last step.
"""

data = open('2021/data/day07').readlines()[0].split(',')
data = map(lambda x: int(x), data)

dists =[sum(abs(data[i] - data[j]) for i in range(len(data))) for j in range(len(data))]
print('Part 1: %d' % min(dists))

dists = []
for i in range(len(data)):
    d = 0
    for j in range(len(data)):
        diff = abs(data[i] - data[j])
        d+= (diff * (diff+1) / 2) #sum of all numbers from 1 to diff
    dists.append(d)

print('Part 2: %d' % min(dists))

# Part 1: 356958
# Part 2: 105461913