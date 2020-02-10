import re
import heapq
from bitarray import bitarray, frozenbitarray

grid = {}
doors = dict()
keys = dict()

f = open('2019/data/day18d')
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

# def BFS(start, seen):
#     global ba, fba
#     x,y = start
#     queue = [(0,x,y,fba)]
#     while queue:
#         d,x,y,fba = heapq.heappop(queue)
#         ba =bitarray(fba)
#         if re.match(r"[a-z]", grid[(x,y)]):
#             ba[skeys.index(grid[(x,y)])] = True
#             if ba.count(False) == 0: return d
#         fba = frozenbitarray(ba)
#         if (x,y,fba) not in seen or seen[(x,y,fba)] > d:
#             seen[(x,y,fba)] = d
#             neighbors = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]]
#             for nb in neighbors:
#                 if (nb[0], nb[1], fba) not in seen or seen[(nb[0], nb[1], fba)] > d:
#                     if re.match(r"[a-z]|\.", grid[nb]) or (re.match(r"[A-Z]", grid[nb]) and fba[skeys.index(grid[nb].lower())]):
#                         heapq.heappush(queue, (d+1,nb[0],nb[1], fba))

grid[entr] = '.'
# d = BFS(entr, {})
# print('Part 1: %d' % d)

# Part 1: 4420

x,y = entr
entries = [(x-1, y-1), (x+1, y-1), (x-1,y+1), (x+1, y+1)]
for loc in entries: grid[loc] = '.'
grid[(x,y)] = grid[(x,y-1)] = grid[(x,y+1)] = grid[(x-1,y)] = grid[(x+1,y)] = '#'
ba.setall(False)

print_grid(grid)

def min_dist(start, keys, all_keys):
    global ba
    x,y = start
    seen = {}
    keysfound = set()
    queue = [(0,x,y,keysfound)]
    fak = frozenset(all_keys)
    while queue:
        d,x,y,fkf = heapq.heappop(queue)
        kf = set(fkf)
        if ogrid[(x,y)] in keys:
            kf.add(ogrid[(x,y)])
            # print('keys %s in d %d' % (kf, d))
            if len(kf) == len(keys): return d
        fkf = frozenset(kf)
        if (x,y,fkf, fak) not in seen or seen[(x,y,fkf, fak)] > d:
            seen[(x,y,fkf, fak)] = d
            neighbors = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]]
            for nb in neighbors:
                if (nb[0], nb[1],fkf, fak) not in seen or seen[(nb[0], nb[1], fkf, fak)] > d:
                    if re.match(r"[a-z]|\.", ogrid[nb]) or (re.match(r"[A-Z]", ogrid[nb]) and (grid[nb].lower() in all_keys or grid[nb].lower() in fkf)):
                        heapq.heappush(queue, (d+1,nb[0],nb[1],fkf))
    return  None

cached_paths = {}

def min_keys_path(start, lba, ba):
    fba = frozenbitarray(lba)
    nba = bitarray(len(lba))
    for i in range(len(nba)):
        if lba[i]:
            nba[i] = False
        else:
            nba[i] = ba[i]
    if not fba in cached_paths:
        keys = [skeys[i] for i,v in enumerate(lba.tolist()) if v]
        cached_paths[fba] = min_dist(start, keys, [skeys[i] for i,v in enumerate(nba.tolist()) if v])
    return cached_paths[fba]


def BFS2(locs, lbas):
    global ba
    o_locs = locs.copy()
    seens =[{}, {}, {}, {}]
    queues = []
    for i in range(4):
        x,y = locs[i]
        queue = [(0,x,y,frozenbitarray(lbas[i]))]
        queues.append(queue)
    ptr = 0
    dists = [0, 0, 0, 0]
    keypaths = {0: [], 1: [], 2: [], 3: []}
    while True:
        queue = queues[ptr]
        seen = seens[ptr]
        if not (re.match(r"[a-z]", grid[(x,y)]) and ba[skeys.index(grid[(x,y)])]):
            heapq.heappush(queue, (dists[ptr],locs[ptr][0], locs[ptr][1], frozenbitarray(lbas[ptr])))
        # print('Start robot %d' % ptr)
        while queue:
            d,x,y,fba = heapq.heappop(queue)
            lba = lbas[ptr]
            if re.match(r"[a-z]", grid[(x,y)]) and not ba[skeys.index(grid[(x,y)])]:
                locs[ptr] = (x, y)
                lba[skeys.index(grid[(x,y)])] = True
                ba[skeys.index(grid[(x,y)])] = True
                dists[ptr] = min_keys_path(o_locs[ptr], lba, ba) #this line breaks c and d (wrong answers)
                # dists[ptr] = d #this gives right answers for ab,b,c but we need to get multi-key distances for d
                print('Robot %d found key %s at distance %d' % (ptr, grid[(x,y)], dists[ptr]))
                keypaths[ptr].append(grid[(x,y)])
                if ba.count(True) == len(skeys):
                    print(dists)
                    print(keypaths)
                    return sum(dists)
                    # dist = 0
                    # for k,v in keypaths.items():
                    #     d =  min_dist(o_locs[k], v)
                    #     dist+= d
                    #     print('Robot %d found keys %s at distance %d' % (k, v, d))
                    # return dist
                #TODO We need to keep the keys in the grid for finding multi-key paths, but omitting the next line breaks the code for
                # an undiscoverable reason. So we use a copy of grid in min_dist
                grid[(x,y)] = '.'
                # break
            fba = frozenbitarray(ba)
            if (x,y,fba) not in seen or seen[(x,y,fba)] > d:
                seen[(x,y,fba)] = d
                neighbors = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]]
                for nb in [nb for nb in neighbors if nb not in locs]:
                    if (nb[0], nb[1], fba) not in seen or seen[(nb[0], nb[1], fba)] > d:
                        if re.match(r"[a-z]|\.", grid[nb]) or (re.match(r"[A-Z]", grid[nb]) and ba[skeys.index(grid[nb].lower())]):
                            # if not (re.match(r"[a-z]", grid[nb]) and fba[skeys.index(grid[nb])]):
                                heapq.heappush(queue, (d+1,nb[0],nb[1],fba))
        ptr = (ptr +1) % 4

ogrid = grid.copy()
lbas = [bitarray(len(keys)), bitarray(len(keys)), bitarray(len(keys)), bitarray(len(keys))]
for lba in lbas: lba.setall(False)
ba.setall(False)
d = BFS2(entries, lbas)
print('Part 2: %d' % d)

#Part 2: 3205 too high 1680 too low
"""
0: calcualte 22 instead of 20
1: calculate 14 instead of 18
2,3: correct
"""