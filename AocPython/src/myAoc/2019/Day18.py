import re
import heapq
from collections import deque

grid = []
doors = dict()
keys = set()

f = open('2019/data/day18')
y = 0
for line in f:
    row = []
    x = 0
    for c in line.strip():
        if re.match(r"[A-Z]", c):
            doors[c] = (y, x)
        elif re.match(r"[a-z]", c):
            keys.add(c)
        elif c== '@': entr = (y,x)
        row.append(c)
        x+= 1
    grid.append(row)
    y+= 1

for row in grid:
    print("".join(row))

seen = set()
y,x = entr
grid[y][x] = '.'
queue = deque([(y,x)])
d = 0
while len(queue)>0:
    y,x = queue.popleft()
    if (y,x) in seen:
        continue
    seen.add((y,x))
    neighbors = [n for n in [(y, x-1), (y, x+1), (y-1, x), (y+1,x)] if grid[n[0]][n[1]] == '.' or re.match(r"[a-z]", grid[n[0]][n[1]])]
    d+= 1
    for nb in neighbors:
        c = grid[nb[0]][nb[1]]
        if re.match(r"[a-z]", c):
            _y,_x = doors[c.upper()]
            grid[_y][_x] = '.'
            grid[nb[0]][nb[1]] = '.'
            seen = set()
            keys.remove(c)
            if len(keys) == 0: print('min path', d)
        queue.append((nb[0], nb[1]))


print('min path', d)

#Part 1: 2453 too low not 67942, 22605, 19404