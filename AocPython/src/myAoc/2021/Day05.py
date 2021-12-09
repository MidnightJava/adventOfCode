import sys

verticals = []
horizontals = []

minx = sys.maxint
miny = sys.maxint
maxx = -sys.maxint
maxy = -sys.maxint

with open('2021/data/day05') as f:
    for line in f.readlines():
        [p1, p2] = line.strip().split('->')
        p1 = tuple(map(lambda x: int(x), p1.split(',')))
        p2 = tuple(map(lambda x: int(x), p2.split(',')))
        minx = min(minx, p1[0], p2[0])
        maxx = max(maxx, p1[0], p2[0])
        miny = min(miny, p1[1], p2[1])
        maxy = max(maxy, p1[1], p2[1])
        if p1[0] == p2[0]:
            if p1[1] < p2[1]:
                verticals.append([p1, p2])
            else:
                verticals.append([p2, p1])
        elif p1[1] == p2[1]:
            if p1[0] < p2[0]:
                horizontals.append([p1, p2])
            else:
                horizontals.append([p2, p1])
        # else:
        #     print('ignore line %s -> %s' % (p1, p2))


grid = []
for i in range(maxy+1): grid.append([0] * (maxx+1))

for h in horizontals:
    x1 = h[0][0]
    x2 = h[1][0]
    y1 = h[0][1]
    y2 = h[1][1]
    if y1 != y2: print("ERR")
    for x in range(x1, x2+1): grid[y1][x]+= 1

for v in verticals:
    x1 = h[0][0]
    x2 = h[1][0]
    y1 = h[0][1]
    y2 = h[1][1]
    # if x1 != x2: print("ERR")
    for y in range(y1, y2+1): grid[y][x1]+= 1

count = 0
for row in grid:
    for c in row:
        if c >= 2: count+= 1

# for row in grid:
#     print(row)
print(count)

# Part 1: > 2981