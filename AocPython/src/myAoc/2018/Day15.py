from __future__ import print_function
import sys

def print_grid():
    for y in range(h):
        for x in range(w):
            print(grid[(x,y)], end='')
        print()

def get_actors():
    l = []
    for y in range(h):
        for x in range(w):
            if grid[(x,y)] == 'G' or grid[(x,y)] == 'E':
                l.append((x,y))
    return l

def get_open_locs(u):
    locs = set()
    for y in range(h):
        for x in range(w):
            if grid[(x,y)] == u:
                for loc in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                    if loc in grid and grid[loc] == '.':
                        locs.add(loc)
    return locs

with open('./data/Day15a') as f:
    global grid, hits
    grid = {}
    hits = {}
    y = 0
    for line in f:
        x = 0
        for c in line:
            grid[(x,y)] = c
            hits[(x,y)] = 200
            x+= 1
        y+= 1
    w = x
    h = y

def find_shortest_path(s, d):
    a = 1

def best_loc(locs):
    ymin = h
    xmin = w
    best = None
    for loc in locs:
        if not best or (loc[1] <= ymin and loc[0] <= xmin):
            xmin = loc[0], ymin = loc[1]
            best = loc
    return best

def move(loc):
    subj = grid[loc]
    enemy = 'G' if subj == 'E' else 'E'
    paths = []
    splen = sys.maxint
    targets = []
    for target in get_open_locs(enemy):
        plen = shortest_path_len(loc, target)
        if plen == splen:
            targets.append(target)
        elif plen < splen:
            splen = plen
            targets = [target]
    target = best_loc(targets)
    paths = shortest_paths(loc, target)
    first_steps = map(lambda x: x[0], paths)
    next_loc = best_loc(first_steps)
            
    grid[loc] = '.'
    grid[next_loc] = subj

print_grid()

def tick():
    actors = get_actors()
    print(actors)
    for actor in actors:
        move(actor)

done = False
while not done:
    tick()
    done = True


