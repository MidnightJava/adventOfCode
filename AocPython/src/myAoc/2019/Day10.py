from fractions import Fraction
from collections import defaultdict
from math import atan2
from math import pi
import itertools

rocks = []
scores = {}

def rotate(d):
    rot_d = {}
    for k,v in d.items():
        rot_d[atan2(k[0], k[1])] = v
    while True:
        start = False
        for item in itertools.cycle(sorted(rot_d.items(), key=lambda x: x[0])):
            if start or item[0] == pi/2:
                start = True
                yield item

def kill_rocks(base, n):
    slopes = scores[base]
    d = rotate(slopes)
    killed = 0
    while killed < n:
        l = next(d)
        r = l[1].pop(0)
        killed+= 1
    return r[0]*100 + r[1]

def get_mon_data(rock):
    slopes = defaultdict(list)
    for _rock in [_rock for _rock in rocks if _rock != rock]:
        xdelt = rock[0] - _rock[0]
        ydelt = rock[1] - _rock[1]
        slope = (ydelt, xdelt)
        #swine Fraction class messes up the signs!
        signs = (-1 if slope[0] < 0 else 1, -1 if slope[1] < 0 else 1)
        if xdelt != 0:
            f = Fraction(ydelt, xdelt)
            slope = (abs(f.numerator) * signs[0], abs(f.denominator) * signs[1])
        else:
            slope = (float("inf") if ydelt > 0 else -float("inf"), 0)
        slopes[slope].append(_rock)
    
    for k, v in slopes.items():
        v = sorted(v, key=lambda x: abs(rock[0] - x[0]) + abs(rock[1] - x[1]))
        slopes[k] = v
    #keys: distinct slopes from this rock to other rocks, value: list of target rocks along each slope, sorted by distance
    return slopes

f = open('2019/data/day10')
y = 0
for line in f:
    x = 0
    for c in line:
        if c == '#': rocks.append((x,y))
        x+= 1
    y+=1

total_rocks = len(rocks)

for rock in rocks:
    scores[rock] = get_mon_data(rock)

best = sorted(scores.items(), key=lambda x: len(x[1]), reverse=True)[0]
print('Part 1: %s monitors %d asteroids' % (best[0], len(best[1])))
print('Part 2: %d' % kill_rocks(best[0], 200))

#Part 1: 286
#Part 2: 504
