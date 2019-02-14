
from __future__ import print_function
from collections import deque, defaultdict
import sys, time

DEBUG = False

def print_grid():
    global h,w
    print('Round %d' % round)
    for y in range(h):
        print('%s) ' % str(y).zfill(2), end='')
        for x in range(w):
            print(grid[(x,y)], end='')
        print('  ', end='')
        units = {}
        for k,v in hits.items():
            if k[1] == y: units[k] = v
        for k,v in sorted(units.items(), key=lambda unit: unit[0][0]):
            print('%s(%d) ' % (grid[k], v), end='')
        print()
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

def reading_order(locs):
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
            if not neighbor in visited or visited[neighbor] > dist:
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
    target = reading_order(targets)
    
    x,y = loc
    splen = sys.maxsize
    next_steps = []
    for t in [coord for coord in [(x-1,y), (x+1,y),(x,y-1),(x,y+1)] if coord in grid and grid[coord] == '.']:
        plen = shortest_path_len(t, target)
        if plen is not None and plen < splen:
            splen = plen
            next_steps = [t]
        elif plen == splen:
            next_steps.append(t)

    if not next_steps: return None
    next_loc = reading_order(next_steps)
    grid[loc] = '.'
    grid[next_loc] = subj
    hits[next_loc] = hits[loc]
    del hits[loc]
    return next_loc

def attack(loc, elf_pwr, part2):
    global hits, grid
    enemy = 'E' if grid[loc] == 'G' else 'G'
    x,y = loc
    targets = []
    for cand in [_loc for _loc in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if grid[_loc] == enemy]:
        targets.append(cand)
    if not targets: return False
    targets2 = []
    minhp = sys.maxsize
    # Get target or targets with least hitpoints
    targets2 = [t for t in targets if hits[t] == min([v for k,v in hits.items() if k in targets])]
    target = reading_order(targets2)
    attck_pwr = 3 if enemy == 'E' else elf_pwr
    hits[target]-= attck_pwr
    if hits[target] <= 0:
        if part2 and grid[target] == 'E': return 'end'
        del hits[target]
        grid[target] = '.'
    return True

def enemy_defeated():
    return not 'E' in [grid[loc] for loc in get_units()] or not 'G' in [grid[loc] for loc in get_units()]

def tick(elf_pwr, part2):
    seen = set()
    for unit in get_units():
        if unit not in hits or hits[unit] <= 0 or unit in seen:
            continue
        if enemy_defeated(): return False
        res = attack(unit, elf_pwr, part2)
        if res == False:
            next_loc = move(unit)
            seen.add(next_loc)
            if next_loc:
                if attack(next_loc, elf_pwr, part2) == 'end': return 'end'
        elif res == 'end':
            return 'end'
    return True

def read_data():
    global grid, hits, w, h
    with open('2018/data/Day15') as f:
        grid = {}
        hits = {}
        for y, line in enumerate(f):
            for x, c in enumerate(line):
                grid[(x,y)] = c
                if c == 'E' or c =='G': hits[(x,y)] = 200
        w, h = x, y

done = False
elf_atck_pow = 3
part2 = False
loop = True
start_time = time.time()
while loop:
    round = 0
    read_data()

    while True:
        if DEBUG:
            print_grid()
            time.sleep(0.5)
        round+= 1
        res = tick(elf_atck_pow, part2)
        if res == False:
            round-= 1
            hitpoints = sum(hits.values())
            if DEBUG:
                print_grid()
                print('rounds: %d,   hit points: %d' % (round, hitpoints))
            if not part2:
                print('Part 1: %d (%d sec)' % (round * hitpoints, time.time() - start_time))
                if DEBUG: raw_input('Press Return to continue:')
                part2 = True
                elf_atck_pow = 16 #Found by binary search trials
            else:
                print('Part 2: %d (%d sec)' % (round * hitpoints, time.time() - start_time))
                loop = False
            break
        elif res == 'end':
            elf_atck_pow+= 1
            break
            

#Part 1: 319410
#Part 2: 63168

