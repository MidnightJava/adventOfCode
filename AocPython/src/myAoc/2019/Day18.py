import re
import heapq
from bitarray import bitarray, frozenbitarray
from collections import defaultdict

grid = {}
doors = dict()
keys = dict()

f = open('2019/data/day18')
y = 0
for line in f:
    x = 0
    for c in line.strip():
        if re.match(r"[A-Z]", c):
            doors[c] = (x, y)
        elif re.match(r"[a-z]", c):
            keys[c] = (x, y)
        elif c== '@':
            entr = (x,y)
        grid[(x,y)] = c
        x+= 1
    x_max = x
    y+= 1
y_max = y

ba = bitarray(len(keys))
ba.setall(False)
fba = frozenbitarray(ba)
skeys = sorted(keys.keys())

def print_grid(grid):
    for y in range(y_max):
        for x in range(x_max):
            print(grid[(x,y)], end='')
        print()

def BFS(start, seen):
    global ba, fba
    x,y = start
    queue = [(0,x,y,fba)]
    while queue:
        d,x,y,fba = heapq.heappop(queue)
        ba =bitarray(fba)
        if re.match(r"[a-z]", grid[(x,y)]):
            ba[skeys.index(grid[(x,y)])] = True
            if ba.count(False) == 0: return d
        fba = frozenbitarray(ba)
        if (x,y,fba) not in seen or seen[(x,y,fba)] > d:
            seen[(x,y,fba)] = d
            neighbors = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]]
            for nb in neighbors:
                if (nb[0], nb[1], fba) not in seen or seen[(nb[0], nb[1], fba)] > d:
                    if re.match(r"[a-z]|\.", grid[nb]) or (re.match(r"[A-Z]", grid[nb]) and fba[skeys.index(grid[nb].lower())]):
                        heapq.heappush(queue, (d+1,nb[0],nb[1], fba))

grid[entr] = '.'
d = BFS(entr, {})
print('Part 1: %d' % d)

# print_grid(grid)

##############
#   PART 2   #
##############

def min_path(start, keys, all_keys):
    """
    Return the distance and final node of the smallest path, beginning at start,
    which collects all <keys>. Doors corresponding to enries in <all_keys> should
    be considered open.
    """
    global ba
    x,y = start
    seen = {}
    keysfound = set()
    queue = [(0,x,y,keysfound)]
    fak = frozenset(all_keys)
    while queue:
        d,x,y,fkf = heapq.heappop(queue)
        kf = set(fkf)
        if grid[(x,y)] in keys:
            kf.add(grid[(x,y)])
            if len(kf) == len(keys):
                return (d, (x,y))
        fkf = frozenset(kf)
        if (x,y,fkf, fak) not in seen or seen[(x,y,fkf, fak)] > d:
            seen[(x,y,fkf, fak)] = d
            neighbors = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]]
            for nb in neighbors:
                if (nb[0], nb[1],fkf, fak) not in seen or seen[(nb[0], nb[1], fkf, fak)] > d:
                    if re.match(r"[a-z]|\.", grid[nb]) or (re.match(r"[A-Z]", grid[nb]) and (grid[nb].lower() in all_keys or grid[nb].lower() in fkf)):
                        heapq.heappush(queue, (d+1,nb[0],nb[1],fkf))
    return  None

cached_paths = {}

def min_keys_path(start, lba, ba):
    keys_to_collect = [skeys[i] for i,v in enumerate(lba.tolist()) if v]
    keys_already_collected = [skeys[i] for i,v in enumerate(ba.tolist()) if v]
    return min_path(start, keys_to_collect, keys_already_collected)


def BFS2(locs):
    # Keys collected by all robots
    global ba
    # Keys collected by the currently executing robot
    lba = bitarray(len(skeys))
    lba.setall(False)
    x,y = locs[0]
    ptr = 0
    dists = [0,0,0,0]
    seen = {}
    queue = [(0,x,y,frozenbitarray(lba))]
    while True:
        heapq.heappush(queue, (0, locs[ptr][0], locs[ptr][1], frozenbitarray(lba)))
        lba.setall(False)
        while queue:
            d,x,y,fba = heapq.heappop(queue)
            if re.match(r"[a-z]", grid[(x,y)]) and not ba[skeys.index(grid[(x,y)])]:
                lba[skeys.index(grid[(x,y)])] = True
                ba[skeys.index(grid[(x,y)])] = True
                # print('Robot %d found key %s' % (ptr, grid[(x,y)]))
            fba = frozenbitarray(ba)
            if (x,y,fba) not in seen or seen[(x,y,fba)] > d:
                seen[(x,y,fba)] = d
                neighbors = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]]
                for nb in [nb for nb in neighbors if nb not in locs]:
                    if (nb[0], nb[1], fba) not in seen or seen[(nb[0], nb[1], fba)] > d:
                        if re.match(r"[a-z]|\.", grid[nb]) or (re.match(r"[A-Z]", grid[nb]) and ba[skeys.index(grid[nb].lower())]):
                            heapq.heappush(queue, (d+1,nb[0],nb[1],fba))
        
        # Get min path to collect all keys available in this iteration
        if lba.count(True):
            dist, last_loc = min_keys_path(locs[ptr], lba, ba)
            # print('robot %d found keys %s at distance %d,  Last loc %s' % (ptr, [skeys[i] for i,v in enumerate(lba) if v], dist, last_loc))
            dists[ptr]+= dist
            locs[ptr] = last_loc
            if ba.count(True) == len(skeys): return sum(dists)

        ptr = (ptr +1) % 4


x,y = entr
entries = [(x-1, y-1), (x+1, y-1), (x-1,y+1), (x+1, y+1)]
for loc in entries: grid[loc] = '.'
grid[(x,y)] = grid[(x,y-1)] = grid[(x,y+1)] = grid[(x-1,y)] = grid[(x+1,y)] = '#'
ba.setall(False)
d = BFS2(entries)
print('Part 2: %d' % d)

# Part 1: 4420
# Part 2: 2128