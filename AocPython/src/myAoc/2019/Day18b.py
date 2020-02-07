import re
import heapq
import sys
from collections import deque
from collections import defaultdict
from itertools import permutations
from bitarray import bitarray, frozenbitarray

grid = {}
doors = dict()
keys = dict()

f = open('2019/data/day18')
y = 0
for line in f:
    x = 0
    for c in line.strip():
        if re.match(r"[A-Z]", c):
            doors[c] = (x, y)
        elif re.match(r"[a-z]", c):
            keys[c] = (x, y)
        elif c== '@':
            entr = (x,y)
        grid[(x,y)] = c
        x+= 1
    x_max = x
    y+= 1
y_max = y

grid2 = grid.copy()

def print_grid(grid):
    for y in range(y_max):
        for x in range(x_max):
            print(grid[(x,y)], end='')
        print()

def BFS(start, seen):
    max_keys = 0
    ba = bitarray(len(keys))
    ba.setall(False)
    fba = frozenbitarray(ba)
    skeys = sorted(keys.keys())
    x,y = start
    queue = [(0,x,y,fba)]
    while len(queue)>0:
        d,x,y,fba = heapq.heappop(queue)
        ba =bitarray(fba)
        if re.match(r"[a-z]", grid[(x,y)]):
            ba[skeys.index(grid[(x,y)])] = True
            count= ba.count(True)
            if count < max_keys-1: continue
            max_keys = max(max_keys, count)
            if count == len(keys):
                return d
        fba = frozenbitarray(ba)
        seen[(x,y,fba)] = d
        neighbors = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]]
        for nb in neighbors:
            if (nb[0], nb[1], fba) not in seen or seen[(nb[0], nb[1], fba)] > d:
                if re.match(r"[a-z]|\.", grid[nb]) or (re.match(r"[A-Z]", grid[nb]) and fba[skeys.index(grid[nb].lower())]):
                    heapq.heappush(queue, (d+1,nb[0],nb[1], fba))

grid[entr] = '.'
d = BFS(entr, {})
print('Part 1: %d' % d)
