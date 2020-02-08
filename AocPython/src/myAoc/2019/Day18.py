import re
import heapq
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

def print_grid(grid):
    for y in range(y_max):
        for x in range(x_max):
            print(grid[(x,y)], end='')
        print()

def BFS(start, seen):
    ba = bitarray(len(keys))
    ba.setall(False)
    fba = frozenbitarray(ba)
    skeys = sorted(keys.keys())
    x,y = start
    queue = [(0,x,y,fba)]
    while queue:
        d,x,y,fba = heapq.heappop(queue)
        ba =bitarray(fba)
        if re.match(r"[a-z]", grid[(x,y)]):
            ba[skeys.index(grid[(x,y)])] = True
            if ba.count(False) == 0: return d
        fba = frozenbitarray(ba)
        if (x,y,fba) not in seen or seen[(x,y,fba)] > d:
            seen[(x,y,fba)] = d
            neighbors = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]]
            for nb in neighbors:
                if (nb[0], nb[1], fba) not in seen or seen[(nb[0], nb[1], fba)] > d:
                    if re.match(r"[a-z]|\.", grid[nb]) or (re.match(r"[A-Z]", grid[nb]) and fba[skeys.index(grid[nb].lower())]):
                        heapq.heappush(queue, (d+1,nb[0],nb[1], fba))

grid[entr] = '.'
d = BFS(entr, {})
print('Part 1: %d' % d)

# Part 1: 4420
