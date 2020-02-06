import re
import heapq
import sys
from collections import deque
from collections import defaultdict
from itertools import permutations

grid = {}
doors = dict()
keys = dict()

f = open('2019/data/day18c')
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
    global grid, grid2
    keys_found = set()
    x,y = start
    queue = [(0,x,y)]
    dist = 0
    while len(queue)>0:
        d,x,y = heapq.heappop(queue)
        if re.match(r"[a-z]", grid[(x,y)]):
            dist+= d
            print(d)
            # d = 0
            keys_found.add(grid[(x,y)])
            print('Found key %s' % grid[(x,y)])
            grid2[(x,y)] = '*'
            loc = doors.get(grid[(x,y)].upper())
            if loc:
                print('Opening door %s' % grid[loc])
                grid[loc] = '.'
                heapq.heappush(queue, (d+1,loc[0],loc[1]))
                a,b = loc
                for nbr in [n for n in [(a-1,b), (a+1,b), (a,b-1), (a,b+1)] if grid[n] == '.' or re.match(r"[a-z]", grid[n])]:
                     heapq.heappush(queue, (d+1,nbr[0],nbr[1]))
                # seen = {}
            grid[(x,y)] = '.'
            if len(keys_found) == len(keys):
                print('last loc %s', (x,y))
                return dist
        if (x,y) in seen and seen[(x,y)] < d:
            continue
        seen[(x,y)] = d
        grid2[(x,y)] = '*'
        neighbors = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if grid[n] == '.' or re.match(r"[a-z]", grid[n])]       
        for nb in neighbors:
            heapq.heappush(queue, (d+1,nb[0],nb[1]))

grid[entr] = '.'
d = BFS(entr, {})
print_grid(grid)
print()
print_grid(grid2)
print('Part 1: %d' % d)
