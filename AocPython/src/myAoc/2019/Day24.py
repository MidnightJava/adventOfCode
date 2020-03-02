from frozendict import frozendict
from collections import defaultdict

grid = {}
seen = set()

def print_grid(_grid):
    for y in range(5):
        for x in range(5):
            print(_grid[(x,y)], end='')
        print()
    print()

def bio_diversity(grid):
    e = 0
    bd = 0
    y = 0
    for y in range(5):
        x = 0
        for x in range(5):
            if grid[(x,y)] == '#':
                bd+= 2**e
            e+= 1
    return bd

def transform(grid):
    gridc = grid.copy()
    for y in range(5):
        for x in range(5):
            nbrs = [gridc.get(t, '.') for t in [(x,y-1), (x, y+1), (x-1, y), (x+1, y)]]
            # print(nbrs)
            if grid[(x,y)] == '#':
                grid[(x,y)] = '#'  if nbrs.count('#') == 1 else '.'
            elif grid[(x,y)] == '.':
                 grid[(x,y)] = '#' if nbrs.count('#') == 1 or nbrs.count('#') == 2 else '.'
            else:
                print('Bad grid val: %s' % grid.get((x,y)))
    return grid

y = 0
for line  in open('./2019/data/day24a').readlines():
    line = line.strip()
    x = 0
    for c in line:
        grid[(x,y)] = c
        x+= 1
    y+= 1

# print_grid(grid)
grid_orig = grid.copy()
while not frozendict(grid) in seen:
    seen.add(frozendict(grid))
    grid = transform(grid)
    # print_grid(grid)
    
print('Part 1: %d' % bio_diversity(grid))
# print_grid(grid)

def empty_grid():
    _grid = {}
    for y in range(5):
        for x in range(5):
            _grid[(x,y)] = '.'
    return _grid

def transform_grid(level, grids):
    grid = grids[level]
    grid_c = grid.copy()
    o_grid = grids[level+1]
    i_grid = grids[level-1]
    for y in range(5):
        for x in range(5):
            if (x,y) == (2,2):
                continue
            nbrs = []
            #North
            if y == 0:
                nbrs.append(o_grid[(2, 4)])
            elif y == 3 and x == 2:
                for i in range(5):
                    nbrs.append(i_grid[(i, 4)])
            else:
                nbrs.append(grid.get((x,y-1), '.'))
            #East
            if x == 4:
                 nbrs.append(o_grid[(0, 2)])
            elif x == 1 and y == 2:
                for i in range(5):
                    nbrs.append(i_grid[(0, i)])
            else:
                nbrs.append(grid.get((x+1, y), '.'))
            #South
            if y == 4:
                nbrs.append(o_grid[(2, 0)])
            elif y == 1 and x == 2:
                for i in range(5):
                    nbrs.append(i_grid[(i, 0)])
            else:
                nbrs.append(grid.get((x,y+1),'.'))
            #West
            if x == 0:
                nbrs.append(o_grid[(4, 2)])
            elif y == 2 and x == 3:
                for i in range(5):
                    nbrs.append(i_grid[(4, i)])
            else:
                nbrs.append(grid.get((x-1,y), '.'))

            # print(nbrs)
            if grid_c[(x,y)] == '#':
                grid_c[(x,y)] = '#'  if nbrs.count('#') == 1 else '.'
            elif grid_c[(x,y)] == '.':
                 grid_c[(x,y)] = '#' if nbrs.count('#') == 1 or nbrs.count('#') == 2 else '.'
            else:
                print('Bad grid val: %s' % grid.get((x,y)))
    grids[level] = grid_c

def transform2(grids):
    level = 0
    while list(grids[level].values()).count('#') > 0:
    # while level >= -2000:
        transform_grid(level, grids)
        level-= 1
    level = 1
    while list(grids[level].values()).count('#') > 0:
    # while level <= 2000:
        transform_grid(level, grids)
        level+= 1
    

grids = defaultdict(empty_grid)

grids[0] = grid.copy()
for i in range(10):
    transform2(grids)

count = 0
for grid in grids.values():
    count+= list(grid.values()).count('#')

print('Part 2: %d' % count)
#Part 1: 26540495 too high