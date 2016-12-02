'''
Created on Dec 21, 2015

@author: maleone
'''
from collections import namedtuple
from itertools import combinations

Prop = namedtuple('Prop', 'cost, damage, armor')
weapons = []
armors = []
rings = []

def win(d, a):
    hit = {0:100, 1:104}
    damage = (d, 8)
    armor = (a,1)
    current = 0
    while hit[0] > 0 and hit[1] > 0:
        hit[1 - current] -= max(damage[current] - armor[1 - current], 1)
        current = 1 - current
    return hit[0] > 0

with open("rpg.txt") as f:
    lines = f.readlines()
    for i in xrange(1,6):
        line = lines[i].split()
        weapons.append(Prop(int(line[1]), int(line[2]), int(line[3])))
    for i in xrange(8, 13):
        line = lines[i].split()
        armors.append(Prop(int(line[1]), int(line[2]), int(line[3])))
    for i in xrange(15, 21):
        line = lines[i].split()
        rings.append(Prop(int(line[2]), int(line[3]), int(line[4])))

armors.append(Prop(0,0,0))
rings.append(Prop(0,0,0))
for x in combinations(rings, 2):
    rings.append(Prop(x[0][0] + x[1][0], x[0][1] + x[1][1], x[0][2] + x[1][2]))

#part 1
def sim(part2):
    minCost = None
    maxCost = 0
    for w in weapons:
        for a in armors:
            for r in rings:
                z = zip(w, a, r)
                cost, damage, armor = sum(z[0]), sum(z[1]), sum(z[2])
                if part2:
                    if  not win(damage, armor):
                        maxCost = cost if cost > maxCost else maxCost
                else:
                    if win(damage, armor):
                        minCost = cost if (not minCost or cost < minCost) else minCost
    return maxCost if part2 else minCost

print "Part 1:", sim(False)
print "Part 2:", sim(True)

            
    
