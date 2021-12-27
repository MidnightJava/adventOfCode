from __future__ import print_function
from collections import defaultdict

grid = []
folds = []

max_y = 0
max_x = 0
points = defaultdict(list)
for line in open('2021/data/day13').readlines():
    if ','in line:
        vals =map(lambda x: int(x), line.strip().split(','))
        max_x = max(max_x, vals[0])
        max_y = max(max_y, vals[1])
        points[vals[1]].append(vals[0])
    elif '=' in line:
        fold = line.strip().split()[2]
        vals = fold.split('=')
        folds.append((vals[0], int(vals[1])))

for y in range(max_y+1):
    row = map(lambda x: 1 if x in points[y] else 0, range(max_x+1))
    grid.append(row)
    # print(row)

first_run = False
for fold in folds:
    if fold[0] == 'x':
        x = fold[1]

        for y in range(max_y):
            l1 = grid[y][:x]
            l2 = grid[y][x:][::-1]
            l3 = []
            for i in range(x):
                l3.append(l1[i] or l2[i])
            grid[y] = l3
        max_x = x

    elif fold[0] == 'y':
        y = fold[1]
        l1 = grid[:y]
        l2 = grid[y+1:][::-1]
        grid = []
        max_y = y
        for i in range(y):
            grid.append([a or b for a,b in zip(l1[i],l2[i])])

    if not first_run:
        count = 0
        for row in grid:
            count+= row.count(1)

        print('Part 1: %d' % count)
        first_run = True

for row in grid:
    for n in row:
       print('#' if n == 1 else ' ', end=' ')
    print()

# part 1: 704
# Part 2: HGAJBEHC
