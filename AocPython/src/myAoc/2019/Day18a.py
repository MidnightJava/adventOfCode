import re
import heapq
import sys
from collections import deque
from collections import defaultdict
from itertools import permutations

import networkx as nx

_grid = {}
doors = dict()
_keys = dict()
rmap = {}

G = nx.DiGraph()

DEPTH = 3

target = 'afbjgnhdloepcikm' #c
# target = 'acfidgbeh' #d

f = open('2019/data/day18c')
y = 0
for line in f:
    x = 0
    for c in line.strip():
        if re.match(r"[A-Z]", c):
            doors[c] = (x, y)
            G.add_node((x,y))
        elif re.match(r"[a-z]", c):
            _keys[c] = (x, y)
            G.add_node((x,y))
        elif c== '@':
            entr = (x,y)
            G.add_node((x,y))
        elif c == '.':
            G.add_node((x,y))
        _grid[(x,y)] = c
        rmap[c] = (x,y)
        x+= 1
    x_max = x
    y+= 1
y_max = y

edges = 0
for y in range(y_max):
    for x in range(x_max):
        if _grid[(x,y)] != "#":
            for nbr in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if _grid.get(n) is not None and _grid.get(n) != '#']:
                edges+= 1
                G.add_edge((x,y), nbr)

def print_grid(grid):
    for y in range(y_max):
        for x in range(x_max):
            print(grid[(x,y)], end='')
        print()

print_grid(_grid)
print(doors)
print(_keys.keys())

def can_reach(key, start, grid):
    # global doors
    # grid = grid.copy()
    # dist = 0
    # queue = deque([(dist, start)])
    # visited = {}
    # while queue:
    #     dist, current = queue.popleft()
    #     if grid[current] == key:
    #         return True
    #     visited[current] = dist
    #     x,y = current
    #     for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] == '.' or re.match(r"[a-z]", grid[n])]:
    #         if not neighbor in visited or visited[neighbor] > dist: queue.append((dist+1, neighbor))
    # return False
    return True

# def reachable(keys, loc, grid):
#     keys = list(map(lambda x: grid[x], keys))
#     res = set()
#     for key in keys:
#         if can_reach(key, loc, grid.copy()): res.add(key)
#     # print('reachable', res)
#     return res

# def get_leaf_paths(start, grid, path, paths):
#     dist = 0
#     queue = deque([(dist, start, path, paths)])
#     visited = {}
#     while queue:
#         dist, current, path, paths = queue.popleft()
#         visited[current] = dist
#         if grid[current] != '.': path.append(grid[current])
#         x,y = current
#         leaf = True
#         for nbr in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]]:
#             if grid[nbr] == '.'  or re.match(r"[a-z]", grid[nbr])  or re.match(r"[A-Z]", grid[nbr]):
#                 if not nbr in visited or visited[nbr] > dist:
#                     leaf = False
#                     queue.append((dist+1, nbr, path, paths))
#         if leaf:
#             paths.append(path)
#             path = []
#     return paths

# _grid[entr] = '.'

def reachable(paths, key, grid):
    for path in paths:
        for k in path:
            if re.match(r"[A-Z]", k):
                break
            elif k == key:
                return True
    return False

def min_dist(dist, start, key, grid, keys_left, keypath):
    global doors
    queue = deque([( dist, start)])
    visited = {}
    while queue:
        dist, current = queue.popleft()

        if re.match(r"[a-z]", grid[current]):
            currentKey = grid[current]
            grid[current] = '.'
            # G.remove_node(current)
            keys_left.remove(currentKey)
            keypath.append(currentKey)
            loc = doors.get(currentKey.upper())
            if loc:
                grid[loc] = '.'
                # G.remove_node(loc)

            if currentKey == key: return dist


        visited[current] = dist
        x,y = current
        for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if re.match(r"[a-z]|\.", grid[n])]:
            if not neighbor in visited or visited[neighbor] > dist:
                queue.append((dist + 1, neighbor))


# def get_nearest_key(start, grid):
#     d = {}
#     dist = 0
#     queue = deque([(dist, start)])
#     visited = {}
#     while queue:
#         dist, current = queue.popleft()

#         if re.match(r"[a-z]", grid[current]):
#             return grid[current]

#         visited[current] = dist
#         x,y = current
#         for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if re.match(r"[a-z]|\.", grid[n])]:
#             if not neighbor in visited or visited[neighbor] > dist:
#                 queue.append((dist + 1, neighbor))


def get_nearest_key(start, grid):
    d = {}
    dist = 0
    queue = deque([(dist, start)])
    visited = {}
    while queue:
        dist, current = queue.popleft()

        if re.match(r"[a-z]", grid[current]):
            d[grid[current]] = dist

        visited[current] = dist
        x,y = current
        for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if re.match(r"[a-z]|\.", grid[n])]:
            if not neighbor in visited or visited[neighbor] > dist:
                queue.append((dist + 1, neighbor))

    for k,v in d.items():
        if v == min(d.values()): return k

def next_key(start, leaves, grid, G):
    """
    Get the reachable key corresponding to the door which is hiding the most keys, as seen from.
    start. If there are more than one such keys, return the one with the shortest path from start.
    A key is reachable if there is a path to it from start that does not pass through a door.
    """
    candidates = defaultdict(int)
    # print('leaves', list(map(lambda x: grid[x], leaves)))
    all_paths = []
    for leaf in leaves:
        paths = list(nx.all_shortest_paths(G, start, leaf))
        for path in paths:
            path = list(map(lambda x: grid[x], path))
            all_paths.append(path)
            # print(path)
            idx = 0
            for c in path[::-1]:
                if re.match(r"[a-z]|\.", c):
                    idx+= 1
                else:
                    if idx < candidates[c.upper()]: candidates[c.upper()] = idx
                    break
    next_keys = [k.lower() for k,v in candidates.items() if v == min(candidates.values()) and reachable(all_paths, k.lower(), grid)]
    min_idx = 1e6
    next_key = None
    if next_keys:
        # print('%d next keys found' % len(next_keys))
        for path in all_paths:
            for key in next_keys:
                if key in path and path.index(key) < min_idx:
                    min_idx = path.index(key)
                    next_key = key
    if next_key:
        return next_key
    else:
        return get_nearest_key(start, grid)

keys_left = set(_keys.keys())
dist = 0
_grid[entr] = '.'
start = entr
keypath = []
while keys_left:
    leaves = [x for x in G.nodes() if G.out_degree(x) == 1]
    leaves = list(filter(lambda x: _grid[x] != '.', leaves))
    key = next_key(start, leaves, _grid, G)
    dist+= min_dist(0, start, key, _grid, keys_left, keypath)
    start = rmap[key]

print("".join(keypath))
print('Part 1:', dist)

# Part 1 not 4620