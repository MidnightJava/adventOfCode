
from __future__ import print_function
from heapq import heappop, heappush
from collections import deque
import sys

def print_grid():
    for y in range(h):
        for x in range(w):
            print(grid[(x,y)], end='')
        print()

def get_units():
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

with open('2018/data/Day15b') as f:
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

def heuristic(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

def shortest_path_len(start, goal):
    paths = shortest_paths(start, goal)
    if not paths: return None
    return min([len(x) for x in paths])

def shortest_paths(start, goal):
    paths = []
    queue = deque([(0, [], start)])
    visited = {}
    while queue:
        l, path, current = queue.popleft()
        x,y = current
        if current == goal:
            np = list(path)
            np.append(goal)
            paths.append(np)
            visited[goal] = len(np)
            continue
        if current in visited:
            continue
        visited[current] = len(path)
        for neighbor in [loc for loc in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if loc in grid and grid[loc] == '.']:
            np = list(path)
            np.append(neighbor)
            if neighbor not in visited or visited[neighbor] > len(path):
                queue.append((len(np), np, neighbor))


    if path: paths.append(list(path))
    if not paths:
        return None
    else:
        return filter(lambda x: len(x) == min([len(p) for p in paths]), paths)

def best_loc(locs):
    ymin = h
    xmin = w
    best = None
    for loc in locs:
        if not best or (loc[1] <= ymin and loc[0] <= xmin):
            xmin = loc[0]
            ymin = loc[1]
            best = loc
    return best

def move(loc):
    subj = grid[loc]
    enemy = 'G' if subj == 'E' else 'E'
    paths = []
    splen = sys.maxint
    targets = []
    open_locs = get_open_locs(enemy)
    if not open_locs: return False
    for target in open_locs:
        plen = shortest_path_len(loc, target)
        if not plen: continue
        if plen == splen:
            targets.append(target)
        elif plen < splen:
            splen = plen
            targets = [target]
    if not targets: return False
    target = best_loc(targets)
    paths = shortest_paths(loc, target)
    if not paths: return False
    first_steps = map(lambda x: x[0], paths)
    next_loc = best_loc(first_steps)
            
    grid[loc] = '.'
    grid[next_loc] = subj
    return True

def attack(loc):
    enemy = 'E' if grid[loc] == 'G' else 'G'
    x,y = loc
    targets = []
    for cand in [loc for loc in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if grid[loc] == enemy]:
        targets.append(cand)
    if not targets: return False
    targets2 = []
    minhp = sys.maxint
    for t in targets:
        if hits[t] < minhp:
            minhp = hits[t]
            targets2 = [t]
        elif hits[t] == minhp:
            targets2.append(t)
    target = best_loc(targets2)
    hits[target]-= 3
    if hits[target] <= 0:
        grid[target] = '.'
    return True

def tick():
    units = get_units()
    if not 'E' in [grid[loc] for loc in units] or not 'G' in [grid[loc] for loc in units]:
        return False
    # print(units)
    # print([grid[loc] for loc in units])
    for unit in units:
        if not attack(unit):
            move(unit)
            attack(unit)
            if not 'E' in [grid[loc] for loc in get_units()] or not 'G' in [grid[loc] for loc in get_units()]:
                return False
        else:
            if not 'E' in [grid[loc] for loc in get_units()] or not 'G' in [grid[loc] for loc in get_units()]:
                return False
    if not 'E' in [grid[loc] for loc in get_units()] or not 'G' in [grid[loc] for loc in get_units()]:
        return False
    return True

done = False
global rounds
rounds = 0
while not done:
    print('round %d' % rounds)
    print_grid()
    if tick():
        rounds+= 1
    else:
        done = True
        units = get_units()
        print(units)
        print([grid[loc] for loc in units])

print_grid()

score = rounds * sum(hits.values())
print('rounds: %d,   hit points: %d' % (rounds, sum(hits.values())))
print('Part 1: %d' % score)


