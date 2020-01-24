import re
import heapq
from collections import deque
from collections import defaultdict
from itertools import permutations

_grid = {}
doors = dict()
_keys = dict()

f = open('2019/data/day18c')
y = 0
for line in f:
    x = 0
    for c in line.strip():
        if re.match(r"[A-Z]", c):
            doors[c] = (x, y)
        elif re.match(r"[a-z]", c):
            _keys[c] = (x, y)
        elif c== '@': entr = (x,y)
        _grid[(x,y)] = c
        x+= 1
    x_max = x
    y+= 1
y_max = y

def print_grid(grid):
    for y in range(y_max):
        for x in range(x_max):
            print(grid[(x,y)], end='')
        print()

print_grid(_grid)
print(doors)
print(_keys.keys())
minimums = set()

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

def heuristic(key, loc):
    # key_loc = _keys[key]
    # return abs(key_loc[0] - loc[0]) + abs(key_loc[1] - loc[1])
    return 0

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

def can_reach(key, start, grid):
    global doors
    grid = grid.copy()
    queue = deque([(heuristic(key, start), start)])
    visited = set()
    while queue:
        _, current = queue.popleft()
        if grid[current] == key:
            return True
        visited.add(current)
        x,y = current
        for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] == '.' or grid[n] == key]:
            if not neighbor in visited: queue.append((heuristic(key, neighbor), neighbor))
    return False

def reachable(keys, loc, grid):
    res = set()
    for key in keys:
        if can_reach(key, loc, grid.copy()): res.add(key)
    # print('reachable', res)
    return res

remaining_keys = set()
def min_dist(dist, start, key, keys, grid):
    # if 154 in minimums:
    #     print('dist: %d, start: %s, key: %s, keys: %s' % (dist, start, key, keys))
    global doors
    queue = deque([(heuristic(key, start), dist, start)])
    visited = {}
    while queue:
        # print(len(queue), ' queue items')
        _, dist, current = queue.popleft()
        if grid[current] == key:
            currentKey = grid[current]
            grid[current] = '.'
            keys.remove(currentKey)
            loc = doors.get(currentKey.upper())
            if loc: grid[loc] = '.'
            # if len(keys) == 1:
            #     keys_left = [k for k in keys if _keys[k] in grid]
            #     lr = len(remaining_keys)
            #     for k in keys_left:
            #         remaining_keys.add(k)
            #     if len(remaining_keys) > lr:
            #         print('keys left',  remaining_keys)
            #     doors_left = [d[0] for d in doors.items() if re.match(r"[A-Z]", grid[d[1]])]
            #     if doors_left:
            #         print('doors left', doors_left)
            #         print_grid(grid)
            #     k = next(iter(remaining_keys))
            #     if k == 'p':
            #         print('reachable keys', reachable(keys, current, grid))
            #         print_grid(grid)
            #         lastDist = min_dist2(current, k, grid)
            #         dist+= lastDist
            #         minimums.add(dist)
            #         print(min(minimums))
            #         return

            if not keys:
                if not dist in minimums:
                    minimums.add(dist)
                    # print(min(minimums), minimums)
                    print(min(minimums))
                return

            reachable_keys = reachable(keys, current, grid.copy())
            # if not reachable_keys: return
            for rkey in reachable_keys:
                if rkey in keys:
                    min_dist(dist, current, rkey, keys.copy(), grid.copy())
            continue

        visited[current] = dist
        x,y = current
        for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] == '.' or grid[n] == key]:
            if not neighbor in visited or visited[neighbor] > dist:
                queue.append((heuristic(key, neighbor), dist + 1, neighbor))
    return


_grid[entr] = '.'

for key in reachable(_keys.keys(), entr, _grid):
   min_dist(0, entr, key, set(_keys.keys()), _grid.copy())

print('Part 1', min(minimums))

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