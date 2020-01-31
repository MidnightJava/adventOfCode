import re
import heapq
import sys
from collections import deque
from collections import defaultdict
from itertools import permutations

import networkx as nx

sys.setrecursionlimit(10**4)

_grid = {}
doors = dict()
_keys = dict()

G = nx.Graph()

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
                G.add_edge(nbr, (x,y))
# print('%d edges' % edges)

def print_grid(grid):
    for y in range(y_max):
        for x in range(x_max):
            print(grid[(x,y)], end='')
        print()

print_grid(_grid)
print(doors)
print(_keys.keys())
# minimums = set()

# def distance(start, grid):
#     grid = grid.copy()
#     def func(key):
#         global doors
#         queue = deque([(0, start)])
#         visited = {}
#         while queue:
#             dist, current = queue.popleft()
#             if grid[current] == key:
#                 return dist
#             elif re.match(r"[a-z]", grid[current]):
#                 loc = doors.get(grid[current].upper())
#                 if loc: grid[loc] = '.'
#                 grid[current] = '.'
#             if current in visited:
#                 continue
#             visited[current] = dist
#             x,y = current
#             for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] == '.' or re.match(r"[a-z]", grid[n])]:
#                 if not neighbor in visited or visited[neighbor] > dist:
#                     queue.append((dist + 1, neighbor))
#         return 0
#     return func

# def heuristic(key, loc):
#     # key_loc = _keys[key]
#     # return abs(key_loc[0] - loc[0]) + abs(key_loc[1] - loc[1])
#     return 0

# def min_dist2(start, key, grid):
#     grid = grid.copy()
#     dist = 0
#     queue = deque([(dist, start)])
#     visited = dict()
#     while queue:
#         dist, current = queue.popleft()
#         if grid[current] == key:
#             return dist
#         # elif re.match(r"[a-z]", grid[current]):
#         #     loc = doors.get(grid[current].upper())
#         #     if loc: grid[loc] = '.'
#         #     grid[current] = '.'
#         # if current in visited:
#         #     continue
#         visited[current] = dist
#         x,y = current
#         for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] == '.' or grid[n] == key]:
#             if not neighbor in visited or visited[neighbor] > dist:
#                 queue.append((dist+1, neighbor))
#     return False

# def can_reach(key, start, grid):
#     global doors
#     grid = grid.copy()
#     queue = deque([(heuristic(key, start), start)])
#     visited = set()
#     while queue:
#         _, current = queue.popleft()
#         if grid[current] == key:
#             return True
#         visited.add(current)
#         x,y = current
#         for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] == '.' or grid[n] == key]:
#             if not neighbor in visited: queue.append((heuristic(key, neighbor), neighbor))
#     return False

# def reachable(keys, loc, grid):
#     res = set()
#     for key in keys:
#         if can_reach(key, loc, grid.copy()): res.add(key)
#     # print('reachable', res)
#     return res

# remaining_keys = set()
# def min_dist(dist, start, key, keys, grid, path):
#     global doors
#     queue = deque([(heuristic(key, start), dist, start)])
#     visited = {}
#     while queue:
#         # print(len(queue), ' queue items')
#         # if len(queue) > 6:
#         #     return
#         _, dist, current = queue.popleft()

#         if grid[current] == key:
#             path.append(key)
#             # print('path', path)
#             currentKey = grid[current]
#             grid[current] = '.'
#             keys.remove(currentKey)
#             loc = doors.get(currentKey.upper())
#             if loc: grid[loc] = '.'
#             # if len(keys) == 1:
#             #     keys_left = [k for k in keys if _keys[k] in grid]
#             #     lr = len(remaining_keys)
#             #     for k in keys_left:
#             #         remaining_keys.add(k)
#             #     if len(remaining_keys) > lr:
#             #         print('keys left',  remaining_keys)
#             #     doors_left = [d[0] for d in doors.items() if re.match(r"[A-Z]", grid[d[1]])]
#             #     if doors_left:
#             #         print('doors left', doors_left)
#             #         print_grid(grid)
#             #     k = next(iter(remaining_keys))
#             #     if k == 'p':
#             #         print('reachable keys', reachable(keys, current, grid))
#             #         print_grid(grid)
#             #         lastDist = min_dist2(current, k, grid)
#             #         dist+= lastDist
#             #         minimums.add(dist)
#             #         print(min(minimums))
#             #         return

#             if not keys:
#                 if not dist in minimums:
#                     minimums.add(dist)
#                     print(min(minimums))
#                 return dist

#             reachable_keys = reachable(keys, current, grid.copy())
#             # if not reachable_keys: return 1e12
#             # print('%d reachable keys' % len(reachable_keys))
#             for rkey in list(reachable_keys)[:DEPTH]:
#                 # print('\ttry key', rkey)
#                 d = min_dist(dist, current, rkey, keys.copy(), grid.copy(), path.copy())
#             # continue

#         visited[current] = dist
#         x,y = current
#         for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] == '.' or grid[n] == key]:
#             if not neighbor in visited or visited[neighbor] > dist:
#                 queue.append((heuristic(key, neighbor), dist + 1, neighbor))

#     if "".join(path) in target:
#         print('Path', path)
#     return 1e12


# _grid[entr] = '.'

# print('reachable', reachable(_keys.keys(), entr, _grid))
# for key in reachable(_keys.keys(), entr, _grid):
#     print('Try key', key)
#     min_dist(0, entr, key, set(_keys.keys()), _grid.copy(),[])

# print('Part 1', min(minimums))

paths = []
_grid[entr] = '.'

def min_dist(loc, key, path, locs, keys, seen, grid):
    global doors
    while True:
        if re.match(r"[a-z]", grid[loc]):
            keys.add(grid[loc])
            path.append(grid[loc])
            seen.add(loc)
        elif re.match(r"[A-Z]", grid[loc]):
            path.append(grid[loc])
            seen.add(loc)

        if key == grid[loc]:
            print('RETURNING')
            paths.append(path)
            path = []
            seen = set()
            return
        elif re.match(r"[a-z]", grid[loc]):
            print(key, grid[loc])

        x,y = loc
        neighbors = [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] != '#' and not n in seen]
        if not neighbors:
            if path: keys.discard(path.pop())
            if locs:
                loc = locs.pop()
        else:
            loc = neighbors[0]
            locs.append(loc)

for key in _keys.keys():
    print('trying key', key)
    min_dist(entr, key, [], [], set(), set(), _grid)

# print(len(paths), 'Paths')
for path in paths:
    print(path)

# def min_dist(start, grid):
#     global doors
#     paths = []
#     path = []
#     queue = [(start)]
#     keys_seen = set()
#     while queue:
#         current = heapq.heappop(queue)

#         if len(keys_seen) == len(_keys):
#             print('All keys collected')
#             if path in paths: return paths
#             paths.append(path)
#             path = []
#             keys_seen = set()
#         if re.match(r"[a-z]", grid[current]) or re.match(r"[A-Z]", grid[current]):
#             if re.match(r"[a-z]", grid[current]): keys_seen.add(grid[current])
#             if grid[current] != '.': path.append(grid[current])

#         x,y = current
#         for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] != '#']:
#             heapq.heappush(queue, (neighbor))
#     return paths


# def search(start, key, path):
#     if start in path or _grid[start] == '#':
#         return

#     if _grid[start] != '.': path.append(_grid[start])
#     if _grid[start] == key:
#         yield path
#     else:
#         x, y = start
#         for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if _grid[n] != '#']:
#             for possible_path in search(neighbor, key, list(path)):
#                 yield possible_path
        

# print('%d paths found' % len(min_dist(entr, _grid.copy())))
# for key in _keys.keys():
#     print('trying key %s' % key)
#     print('%d paths found' % len(min_dist(0, entr, key, _grid.copy())))
#         print(path)
#     print(_paths[0])

# for key in sorted(_keys.keys()):
#     print('Trying key %s' % key)
#     for path in nx.all_simple_paths(G, entr, _keys[key]):
#         path = filter(lambda x: _grid[x] != '.', path)
#         print("".join(list(map(lambda x: _grid[x], path))))
    # print(len(list(nx.all_simple_paths(G, entr, _keys[key]))))

# print('Part 1', min(path_lens))
# Part 1: 2453 too low
#   not 
#   4666,
#   4812,
#   4870,
#   5066
#   5154,
#   5414,
#   5594,
#   5678,
#   5698,
#   5770,
#   5782,
#   6010,
#   7198,
#   19404,
#   22605,
#   32500,
#   35701,
#   67942