from collections import defaultdict
import os

grid = defaultdict(set)
grid2 = defaultdict(int)
min_d = int(1e12)
min_steps = int(1e12)
print(os.getcwd())

f = open('./2019/data/day03')

wire = 0
for line in f.readlines():
    pos = (0,0)
    steps = 0
    for mv in line.split(','):
        steps-= 1
        if mv[0] == 'L':
            for x in range(pos[0], pos[0] - int(mv[1:])-1, -1):
                new_pos = (x, pos[1])
                steps+= 1
                if not wire in grid[new_pos]: grid2[new_pos]+= steps
                if new_pos != (0,0):
                    grid[new_pos].add(wire)

            pos = (pos[0] - int(mv[1:]), pos[1])
        elif mv[0] == 'R':
            for x in range(pos[0], pos[0] + int(mv[1:])+1):
                new_pos = (x, pos[1])
                steps+= 1
                if not wire in grid[new_pos]: grid2[new_pos]+= steps
                if new_pos != (0,0):
                    grid[new_pos].add(wire)
            pos = (pos[0] + int(mv[1:]), pos[1])
        elif mv[0] == 'U':
            for y in range(pos[1], pos[1] + int(mv[1:])+1):
                new_pos = (pos[0], y)
                steps+= 1
                if not wire in grid[new_pos]: grid2[new_pos]+= steps
                if new_pos != (0,0):
                    grid[new_pos].add(wire)
            pos = (pos[0], pos[1] + int(mv[1:]))
        elif mv[0] == 'D':
            for y in range(pos[1], pos[1] - int(mv[1:])-1, -1):
                new_pos = (pos[0], y)
                steps+= 1
                if not wire in grid[new_pos]: grid2[new_pos]+= steps
                if new_pos != (0,0):
                    grid[new_pos].add(wire)
            pos = (pos[0], pos[1] - int(mv[1:]))
    wire+= 1

for k, v in grid.items():
    if len(v) >= 2:
        min_d = min(min_d, abs(k[0]) + abs(k[1]))

for k, v in grid2.items():
    if len(grid[k]) == 2:
         min_steps = min(min_steps, v)

print('Part 1: %d' % min_d)
print('Part 2: %d' % min_steps)

# Part 1: 258
# Part 2: 12304
