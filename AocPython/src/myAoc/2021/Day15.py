from __future__ import print_function

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

def min_risk():
    tc = [[0 for x in range(max_x+1)] for y in range(max_y+1)]

    for y in range(1, max_y+1):
        tc[y][0] = tc[y-1][0] + grid[(y,0)]
    for x in range(1,max_x+1):
        tc[0][x] = tc[0][x-1] + grid[(0,x)]

    for y in range(1, max_y+1):
        for x in range(1, max_x+1):
            tc[y][x] = min(tc[y][x-1], tc[y-1][x]) + grid[(y,x)]

    return tc[max_y][max_x]

print('Part 1: %d' % min_risk())

# Part 1: < 1048 not 658, 661