import re
import heapq
from collections import deque

grid = {}
doors = dict()
keys = set()

f = open('2019/data/day18')
y = 0
for line in f:
    x = 0
    for c in line.strip():
        if re.match(r"[A-Z]", c):
            doors[c] = (x, y)
        elif re.match(r"[a-z]", c):
            keys.add(c)
        elif c== '@': entr = (x,y)
        grid[(x,y)] = c
        x+= 1
    x_max = x
    y+= 1
y_max = y

def print_grid():
    for y in range(y_max):
        for x in range(x_max):
            print(grid[(x,y)], end='')
        print()

print_grid()
print(doors)
print(keys)

seen = set()
x,y = entr
grid[(x,y)] = '.'
queue = deque([(x,y)])
d = 0
while len(queue)>0:
    x,y = queue.popleft()
    if (x,y) in seen:
        continue
    seen.add((x,y))
    neighbors = [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] == '.' or re.match(r"[a-z]", grid[n])]
    d+= 1
    for nb in neighbors:
        c = grid[nb]
        if re.match(r"[a-z]", c):
            _x, _y = doors[c.upper()]
            grid[(_x, _y)] = '.'
            grid[nb] = '.'
            seen = set()
            keys.remove(c)
            if len(keys) == 0: print('min path', d)
        queue.append((nb[0], nb[1]))


print('min path', d)

#Part 1: 2453 too low not 67942, 22605, 19404, 32500, 35701