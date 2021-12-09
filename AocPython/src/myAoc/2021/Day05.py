import sys

verticals = []
horizontals = []
diagonals = []

minx = miny = sys.maxint
maxx = maxy = -sys.maxint

if len(sys.argv) >= 2:
    part = sys.argv[1]
else:
    part = "1"

with open('2021/data/day05') as f:
    for line in f.readlines():
        p1s, p2s = line.strip().split('->')
        p1 = tuple(map(lambda x: int(x), p1s.split(',')))
        p2 = tuple(map(lambda x: int(x), p2s.split(',')))
        minx, maxx = min(minx, p1[0], p2[0]), max(maxx, p1[0], p2[0])
        miny, maxy = min(miny, p1[1], p2[1]), max(maxy, p1[1], p2[1])
        
        if p1[0] == p2[0]:
            verticals.append([p1, p2] if p1[1] < p2[1] else [p2, p1])
        elif p1[1] == p2[1]:
            horizontals.append([p1, p2] if p1[0] < p2[0] else [p2, p1])
        elif part == "2":
            diagonals.append([p1, p2] if p1[0] < p2[0] else [p2, p1])


grid = []
for i in range(maxy+1): grid.append([0] * (maxx+1))

for h in horizontals:
    x1, x2 = h[0][0], h[1][0]
    y = h[0][1]
    for x in range(x1, x2+1): grid[y][x]+= 1

for v in verticals:
    x = v[0][0]
    y1, y2 = v[0][1], v[1][1]
    for y in range(y1, y2+1): grid[y][x]+= 1

for d in diagonals:
    x1 = d[0][0]
    x2 = d[1][0]
    y1, y2 = d[0][1], d[1][1]
    dir = 1 if y1 < y2 else -1
    y = y1
    for x in range(x1, x2+1):
        grid[y][x]+= 1
        y+= dir

count = len([row for row in grid for c in row if c >= 2])

print('Part %s: %d' % (part, count))

# Part 1: 7438
# Part 2: 21406