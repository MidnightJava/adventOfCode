"""
The input is a 10x10 grid representing the energy levels of
octopuses. For each step, each octopus's level is increased by
one. Then any octopus whose energy level is greater than 9 "flashes".
This means every adjacent octopus's energy level is incresed by
one. Diagonal adjacencies are included. Each octopus may flash at
most once during each step.

Part 1: Report the number of octopuses that have flashed after 100 steps.

Part 2: Determine the number of the first step in which all octopuses flash.
"""

from copy import deepcopy

global grid
grid = []
global count
count = 0
global seen

def flash(row, col):
    global count, seen, grid
    seen.add((row,col))
    count+= 1
    for y in [row-1, row, row+1]:
        for x in [col-1, col, col+1]:
            if y>=0 and x >=0 and (y,x) != (row,col):
                try:
                    grid[y][x]+= 1
                except IndexError:
                    pass

    grid[row][col] = 0
    flashable = True
    while flashable:
        flashable = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in seen and grid[row][col] > 9:
                    flash(row, col)
                    flashable = True


f = open('2021/data/day11')
for line in f:
    grid.append(map(lambda x: int(x), line.strip()))
    grid_orig = deepcopy(grid)

for part in [1,2]:
    seen = set()
    if part == 2:
        grid = grid_orig
    done = False
    step = 0
    while not done:
        if step == 100 and part == 1:
            res = count
            break
        elif len(seen) == 100 and part == 2:
            res = step
            break
        for pt in seen:
            y,x = pt
            grid[y][x] = 0
        seen = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                grid[row][col]+= 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] > 9: flash(row, col)
        step+= 1
    
    print('Part %d: %d' % (part, res))
# Part 1: 1755
# Prt 2: 212