from __future__ import print_function
import heapq
from copy import deepcopy

grid = {}

y = 0
max_x = 0
max_y = 0
for line in open('2021/data/day15').readlines():
    max_y= max(max_y, y)
    line = line.strip()
    for x in range(len(line)):
        max_x = max(max_x, x)
        grid[(y,x)] = int(line[x])
    y+= 1
max_x+= 1
max_y+= 1

def heuristic(risk, curr, end):
    return abs(end[0] - curr[0]) + abs(end[1]-curr[1]) + risk

def solve(part, grid, end):
    start = (0,0)
    queue = [(heuristic(0, start, end), 0, start)]
    visited = {}
    risks = []
    while queue:
        _, risk, curr = heapq.heappop(queue)
        y,x = curr
        if curr == end:
            risks.append(risk)
        if curr in visited: continue
        visited[curr] = risk
        for nbr in [n for n in [(y, x-1), (y, x+1), (y-1,x), (y+1,x)] if n in grid]:
            if not nbr in visited or visited[nbr] > risk + grid[nbr]:
                heapq.heappush(queue, (heuristic(risk + grid[nbr], nbr, end), risk + grid[nbr], nbr))

    print('Part %d: %d' % (part, min(risks)))

end = (max_y-1, max_x-1)
solve(1, grid, end)

def make_grid(n):
    _grid = deepcopy(grid)
    for y in range(max_y):
        for x in range(max_x):
            _grid[(y,x)]+= n
            if _grid[(y,x)] > 9:
                _grid[(y,x)]%= 9
    return _grid

deltas = [[0 for x in range(5)] for x in range(5)]

for y in range(5):
    for x in range(5):
        deltas[y][x] = x+y

grids = {}
for y in range(5):
    for x in range(5):
        grids[(y,x)] = make_grid(deltas[y][x])

yoff = 0
for y in range(5):
    xoff = 0
    for x in range(5):
        _grid = grids[(y,x)]
        for yy in range(max_y):
            for xx in range(max_x):
                grid[(yy+yoff, xx+xoff)] = _grid[(yy,xx)]
        xoff+= max_x
    yoff+= max_y

end = (max_y*5-1, max_x*5-1)
solve(2, grid, end)

# Part 1: 656
# Part 2: 2979