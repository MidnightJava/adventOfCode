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
            if len(kf) == len(keys):
                return (d, (x,y))
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
    dists2 = [0,0,0,0]
    while True:
        queue = queues[ptr]
        seen = seens[ptr]
        if not (re.match(r"[a-z]", grid[(x,y)]) and ba[skeys.index(grid[(x,y)])]):
            heapq.heappush(queue, (dists[ptr],locs[ptr][0], locs[ptr][1], frozenbitarray(lbas[ptr])))
        # print('Start robot %d' % ptr)
        keysfound = []
        dist = 0
        lba = bitarray(len(skeys))
        lba.setall(False)
        while queue:
            d,x,y,fba = heapq.heappop(queue)
            if re.match(r"[a-z]", grid[(x,y)]) and not ba[skeys.index(grid[(x,y)])]:
                keysfound.append(grid[(x,y)])
                locs[ptr] = (x, y)
                lba[skeys.index(grid[(x,y)])] = True
                ba[skeys.index(grid[(x,y)])] = True
                dist, last_loc = min_keys_path(o_locs[ptr], lba, ba) #this line breaks c and d (wrong answers)
                # dists[ptr] = d #this gives right answers for ab,b,c but we need to get multi-key distances for d
                print('Robot %d found key %s at distance %d' % (ptr, grid[(x,y)], dists[ptr]))
                # keypaths[ptr].append(grid[(x,y)])
                if ba.count(True) == len(skeys):
                    # print(dists)
                    # print(keypaths)
                    # return sum(dists)
                    dists2[ptr]+= dist
                    print(dists2)
                    tot_d = sum(dists2)
                    return tot_d
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
        
        if keysfound:
            dist, last_loc = min_keys_path(last_loc, lba, ba)
            print('robot %d found keys %s at distance %d,  Last loc %s' % (ptr, keysfound, dist, last_loc))
            dists2[ptr]+= dist
            o_locs[ptr] = last_loc
        ptr = (ptr +1) % 4

ogrid = grid.copy()
lbas = [bitarray(len(keys)), bitarray(len(keys)), bitarray(len(keys)), bitarray(len(keys))]
for lba in lbas: lba.setall(False)
ba.setall(False)
d = BFS2(entries, lbas)
print('Part 2: %d' % d)

#Part 2: 3205 too high 1680 too low not 2748
"""
0: calcualte 22 instead of 20
1: calculate 14 instead of 18
2,3: correct

#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba.#.BcIJ#
#############
#nK.L.#.G...#
#M###N#H###.#
#o#m..#i#jk.#
#############
Robot 0 found key a at distance 1
Robot 0 found key e at distance 3
Robot 0 found key b at distance 4
robot 0 found keys ['a', 'e', 'b']. Last loc (3, 3)
Robot 1 found key c at distance 2
Robot 1 found key h at distance 8
robot 1 found keys ['c', 'h']. Last loc (9, 1)
robot 2 found keys []. Last loc (9, 1)
Robot 3 found key i at distance 2
robot 3 found keys ['i']. Last loc (7, 7)
Robot 0 found key d at distance 6
Robot 0 found key f at distance 12
Robot 0 found key g at distance 22
robot 0 found keys ['d', 'f', 'g']. Last loc (1, 1)
robot 1 found keys []. Last loc (1, 1)
robot 2 found keys []. Last loc (1, 1)
Robot 3 found key k at distance 11
Robot 3 found key j at distance 12
robot 3 found keys ['k', 'j']. Last loc (9, 7)
robot 0 found keys []. Last loc (9, 7)
Robot 1 found key l at distance 14
robot 1 found keys ['l']. Last loc (11, 1)
Robot 2 found key n at distance 4
Robot 2 found key m at distance 12
Robot 2 found key o at distance 22
[22, 14, 22, 12]
{0: ['a', 'e', 'b', 'd', 'f', 'g'], 1: ['c', 'h', 'l'], 2: ['n', 'm', 'o'], 3: ['i', 'k', 'j']}
Part 2: 70
"""