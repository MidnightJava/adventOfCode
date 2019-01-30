

from __future__ import print_function
import time

constellations = []

def inConst(pt, const):
    for c in const:
        if sum([abs(c[i] - pt[i]) for i in range(4)]) <= 3:
            return True
    return False

def constelllationsNear(const1, const2):
    for pt in const1:
        if inConst(pt, const2):
            return True
    return False

def joinConstellations(const1, const2):
    global constellations
    const2|= const1
    if const1 in constellations:
        del constellations[constellations.index(const1)]

start_time = time.time()
with open('data/Day25') as f:
    for line in f:
        pt = tuple(map(int,line.strip().split(',')))
        found = False
        for c in constellations:
            if inConst(pt, c):
                c.add(pt)
                found = True
                break
        if not found:
            c = set()
            c.add(pt)
            constellations.append(c)

modified = True
while modified:
    modified = False
    for const in constellations:
        for const2 in [c for c in constellations if c != const]:
            if constelllationsNear(const, const2):
                joinConstellations(const, const2)
                modified = True

print('%d constellations' % len(constellations))
print('time %d seconds' % (time.time() - start_time))
