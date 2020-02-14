import re
from collections import defaultdict
import heapq

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

def jump(loc):
    port = ports[loc]
    for _loc in rport[port]:
        if _loc != loc: return _loc

for y in range(h):
    for x in range(w):
        print(grid[(x,y)], end='')
    print()

for k,v in rport.items():
    print('%s : %s' % (k,v))


def BFS(start):
    seen = {}
    x,y = start
    queue = [(0,x,y)]
    while queue:
        d,x,y = heapq.heappop(queue)
        if grid[(x,y)] == "*":
            if ports[(x,y)] == 'ZZ':
                return d
            if ports[(x,y)] != 'AA':
                rem_loc = jump((x,y))
                heapq.heappush(queue, (d+1, rem_loc[0], rem_loc[1]))
        if (x,y) not in seen or seen[(x,y)] > d:
            seen[(x,y)] = d
            neighbors = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if re.match(r"[\.\*]", grid[n])]
            for nb in neighbors:
                if (nb[0], nb[1]) not in seen or seen[(nb[0], nb[1])] > d:
                    heapq.heappush(queue, (d+1, nb[0], nb[1]))

start = rport['AA'][0]
d = BFS(start)
print('PART 1 %d' % d)
