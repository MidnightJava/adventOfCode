
from __future__ import print_function
from heapq import heappop, heappush
from collections import deque, defaultdict
import sys

hitmap = defaultdict(int)
def print_grid():
    for y in range(h):
        print('%s) ' % str(y).zfill(2), end='')
        for x in range(w):
            print(grid[(x,y)], end='')
        print('  ', end='')
        units = {}
        for k,v in hits.items():
            if k[1] == y: units[k] = v
        for k,v in sorted(units.items(), key=lambda unit: unit[0][0]):
            print('%s(%d), ' % (grid[k], v), end='')
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
            if grid[(x,y)] == u and (x,y) in hits and hits[(x,y)] > 0:
                for loc in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                    if loc in grid and grid[loc] == '.':
                        locs.add(loc)
    return locs

def best_loc(locs):
    return sorted(locs, key=lambda x: (x[1], x[0]))[0]

def heuristic(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

def shortest_path_len(start, goal):
    global grid
    queue = deque([(0 + heuristic(start, goal), 0, start)])
    visited = {}
    while queue:
        _, dist, current = queue.popleft()
        if current == goal:
            return dist
        if current in visited:
            continue
        visited[current] = dist
        x,y = current
        for neighbor in [loc for loc in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if loc in grid and grid[loc] == '.']:
            queue.append((dist + heuristic(neighbor, goal), dist + 1, neighbor))
    
    return None

def move(loc):
    subj = grid[loc]
    enemy = 'G' if subj == 'E' else 'E'
    splen = sys.maxsize
    targets = []
    open_locs = get_open_locs(enemy)
    if not open_locs: return None
    for target in open_locs:
        plen = shortest_path_len(loc, target)
        if plen is None: continue
        if plen == splen:
            targets.append(target)
        elif plen < splen:
            splen = plen
            targets = [target]
    if not targets: return None
    target = best_loc(targets)
    
    x,y = loc
    splen = sys.maxsize
    next_steps = []
    for t in [coord for coord in [(x-1,y), (x+1,y),(x,y-1),(x,y+1)] if coord in grid and grid[coord] == '.']:
        plen = shortest_path_len(t, target)
        # if plen is not None and plen == 0:
        #     attack(loc)
        #     print('*'*20, plen)
        #     # return loc
        if plen is not None and plen < splen:
            splen = plen
            next_steps = [t]
        elif plen == splen:
            next_steps.append(t)

    if not next_steps: return None
    next_loc = best_loc(next_steps)
    grid[loc] = '.'
    grid[next_loc] = subj
    hits[next_loc] = hits[loc]
    del hits[loc]
    return next_loc

def attack(loc, eattack):
    global hits, grid
    enemy = 'E' if grid[loc] == 'G' else 'G'
    x,y = loc
    targets = []
    for cand in [_loc for _loc in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if grid[_loc] == enemy]:
        targets.append(cand)
    if not targets: return False
    targets2 = []
    minhp = sys.maxsize
    for t in targets:
        if hits[t] < minhp:
            minhp = hits[t]
            targets2 = [t]
        elif hits[t] == minhp:
            targets2.append(t)
    target = best_loc(targets2)
    apow = 3 if enemy == 'E' else eattack
    hits[target]-= apow
    if hits[target] <= 0:
        if grid[target] == 'E': return 'end'
        del hits[target]
        grid[target] = '.'
    return True

def enemy_defeated():
    return not 'E' in [grid[loc] for loc in get_units()] or not 'G' in [grid[loc] for loc in get_units()]

def tick(eattack):
    seen = set()
    for unit in get_units():
        if unit not in hits or hits[unit] <= 0 or grid[unit] == '.' or unit in seen:
            continue
        found_enemy = False
        for _unit in get_units():
            if not _unit in hits or hits[_unit] <= 0 or grid[_unit] == '.': continue
            enemy = 'E' if grid[_unit] == 'G' else 'G'
            if get_open_locs(enemy): found_enemy = True
        if not found_enemy: return False
        res = attack(unit, eattack)
        if res == False:
            next_loc = move(unit)
            seen.add(next_loc)
            if next_loc:
                if attack(next_loc, eattack) == 'end': return 'end'
                if enemy_defeated():
                    return False
        elif res == 'end':
            return 'end'
        elif enemy_defeated():
            return False
    return True

done = False
global rounds
round = 0
startagain = False
eattack = 3
while True:
    round = 0
    eattack+= 1
    hitmap = defaultdict(int)
    print('Start sim with eattack %d' % eattack)
    with open('data/Day15') as f:
        global grid, hits
        grid = {}
        hits = {}
        y = 0
        for line in f:
            x = 0
            for c in line:
                grid[(x,y)] = c
                if c == 'E' or c =='G':
                    hits[(x,y)] = 200
                x+= 1
            y+= 1
        w = x
        h = y
    while True:
        # if round >= 69 and round <= 72:
        #     print('round %d' % round)
        #     print_grid()
        round+= 1
        res = tick(eattack)
        if res == False:
            done = True
        elif res == 'end':
            startagain = True
            break
        # hitmap[round] = {}
        # hitmap[round]['G']= sum([v for k,v in hits.items() if grid[k] == 'G' and v > 0])
        # hitmap[round]['E']= sum([v for k,v in hits.items() if grid[k] == 'E' and v > 0])
        # hitmap[round]['T']= sum([v for k,v in hits.items() if v > 0])
        if done:
            round-= 1
            hitpoints = 0
            for k,v in hits.items():
                if v > 0: hitpoints+= v
            score = round * hitpoints
            # print(hitmap)
            print('rounds: %d,   hit points: %d' % (round, hitpoints))
            print('Part 1: %d' % score)
            sys.exit()
        # if enemy_defeated(): done = True

print()
print('round %d' % round)
print()
print_grid()

# hitpoints = 0
# for k,v in hits.items():
#     if grid[k] == 'G' and v > 0: hitpoints+= v
# score = round * hitpoints
# print(hitmap)
# print('rounds: %d,   hit points: %d' % (round, hitpoints))
# print('Part 1: %d' % score)

#Part 1: 319410
#Part 2: 57642 too low

