import re
from collections import defaultdict

grid = {}
ports = {}
rport = defaultdict(list)

f = open('./2019/data/day20')
lines = f.read().split('\n')
y = 0
for line in lines:
    x = 0
    for c in line:
        if re.match(r"[\#\s\.]|[A-Z]", c):
            grid[(x,y)] = c
            x+=1
    y+= 1
h = y
w = x

for x in range(w):
    for y in range(h):
        if re.match(r"[A-Z]", grid[(x,y)]):
            if re.match(r"[A-Z]", grid.get((x,y+1),"")):
                cc = grid[(x,y)] + grid[(x,y+1)]
                if re.match(r"\.", grid.get((x,y-1), "")):
                    loc = (x, y-1)
                else:
                    loc = (x, y+2)
                ports[loc] = cc
                grid[loc] = "*"
                rport[cc].append(loc)
for y in range(h):
    for x in range(w):
        if re.match(r"[A-Z]", grid[(x,y)]):
            if re.match(r"[A-Z]", grid.get((x+1,y),"")):
                cc = grid[(x,y)] + grid[(x+1,y)]
                if re.match(r"\.", grid.get((x-1,y), "")):
                    loc = (x-1, y)
                else:
                    loc = (x+2, y)
                ports[loc] = cc
                grid[loc] = "*"
                rport[cc].append(loc)



for y in range(h):
    for x in range(w):
        print(grid[(x,y)], end='')
    print()

for k,v in rport.items():
    print('%s : %s' % (k,v))

