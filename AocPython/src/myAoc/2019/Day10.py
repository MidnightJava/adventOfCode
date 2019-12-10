from collections import defaultdict
from fractions import Fraction

rocks = []
scores = {}

def ratios_equal(r1, r2):
    res1 = (r1[0] * r2[1], r1[1] * r2[1])
    res2 = (r2[0] * r1[1], r2[1] * r1[1])
    return res1[0] == res2[0] and res1[1] == res2[1]

def get_mon_count(rock):
    slopes = set()
    for _rock in [_rock for _rock in rocks if _rock != rock]:
        xdelt = rock[0] - _rock[0]
        ydelt = rock[1] - _rock[1]
        slope = (ydelt, xdelt)
        # if xdelt != 0:
        #     f = Fraction(ydelt, xdelt)
        #     slope = (f.numerator, f.denominator)
        # else:
        #     slope = (float("inf") if ydelt > 0 else -float("inf"), 0)
        l = len(slopes)
        slopes.add(slope)
        if l == len(slopes):
            print('slope not added %s, %s' % (slope))
        # found = False
        # for s in slopes:
        #     if ratios_equal(s, slope):
        #         found = True
        #         break
        # if not found: slopes.add(slope)
        # if xdelt == 0:
        #     slope = (float("inf"), float("inf")) if ydelt > 0 else (-float("inf"), -float("inf"))
        # else:
        #     slope = (ydelt, xdelt)
        # slopes.add(slope)
   
    # if len(slopes) == 214: print(slopes)
    print(slopes)
    return len(slopes)

f = open('2019/data/day10a')
y = 0
for line in f:
    x = 0
    for c in line:
        if c == '#': rocks.append((x,y))
        x+= 1
    y+=1

total_rocks = len(rocks)

for rock in rocks:
    scores[rock] = get_mon_count(rock)

best_rock = [(rock, count) for rock, count in scores.items() if count == max(scores.values())][0]
print('Part 1: %s monitors %d asteroids' % (best_rock))

# print(len(rocks))
#Part 1: 160 < ans < 352 not: 259,264,275,276,283  between 275 and 283? 280, 281, 282
