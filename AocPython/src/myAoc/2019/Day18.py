import re
import heapq
from collections import deque
from itertools import permutations

grid = {}
doors = dict()
keys = set()

f = open('2019/data/day18a')
y = 0
for line in f:
    x = 0
    for c in line.strip():
        if re.match(r"[A-Z]", c):
            doors[c] = (x, y)
        elif re.match(r"[a-z]", c):
            keys.add(c)
        elif c== '@': entr = (x,y)
        grid[(x,y)] = c
        x+= 1
    x_max = x
    y+= 1
y_max = y

def print_grid(grid):
    for y in range(y_max):
        for x in range(x_max):
            print(grid[(x,y)], end='')
        print()

print_grid(grid)
print(doors)
print(keys)
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

def can_reach(key, start, grid):
    global doors
    grid = grid.copy()
    queue = deque([(0, start)])
    visited = {}
    while queue:
        dist, current = queue.popleft()
        if grid[current] == key:
            return True
        # elif re.match(r"[a-z]", grid[current]):
        #     loc = doors.get(grid[current].upper())
        #     if loc: grid[loc] = '.'
        #     grid[current] = '.'
        if current in visited:
            continue
        visited[current] = dist
        x,y = current
        for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] == '.' or grid[n] == key]:
            if not neighbor in visited or visited[neighbor] > dist:
                queue.append((dist + 1, neighbor))
    return False

def reachable(keys, loc, grid):
    res = set()
    for key in keys:
        if can_reach(key, loc, grid.copy()): res.add(key)
    return res

# def min_dist(dist, start, key, keys, grid):
#     keys = set(keys)
#     global minimums
#     queue = deque([(dist, start)])
#     visited = {}
#     while queue:
#         dist, current = queue.popleft()
#         if grid[current] == key:
#             keys.discard(key)
#             # print('%d keys left' % len(keys))
#             if not len(keys):
#                 print('min d', dist)
#                 minimums.add(dist)
#                 return
#             grid[current] = '.'
#             loc = doors.get(key.upper())
#             if loc: grid[loc] = '.'
#             # for _keys in permutations(reachable(keys, current, grid)):
#             for key in sorted(keys, key=distance(current, grid), reverse=True):
#                 min_dist(dist, current, key, list(keys).copy(), grid.copy())
#         elif re.match(r"[a-z]", grid[current]) and grid[current] in keys:
#             keys.discard(grid[current])
#             if not len(keys):
#                 print('min d', dist)
#                 minimums.add(dist)
#                 return
#             loc = doors.get(grid[current].upper())
#             if loc: grid[loc] = '.'
#             grid[current] = '.'
#         if current in visited:
#             continue
#         visited[current] = dist
#         x,y = current
#         for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] == '.' or grid[n] in keys]:
#             if not neighbor in visited or visited[neighbor] > dist:
#                 queue.append((dist + 1, neighbor))

def min_dist(dist, start, key, keys, grid):
    # print('in min_dist')
    queue = deque([(dist, start)])
    visited = {}
    while queue:
        # print(len(queue), ' queue items')
        dist, current = queue.popleft()
        if grid[current] == key:
            currentChar = grid[current]
            grid[current] = '.'
            keys.discard(currentChar)
            if len(keys) == 0:
                if not dist in minimums:
                    minimums.add(dist)
                    print(min(minimums), minimums)
                return
            loc = doors.get(currentChar.upper())
            if loc: grid[loc] = '.'

            reachable_keys = reachable(keys, current, grid.copy())
            for key in reachable_keys:
                min_dist(dist, current, key, keys.copy(), grid.copy())
        # if current in visited:
        #     continue
        visited[current] = dist
        x,y = current
        for neighbor in [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] == '.' or grid[n] == key]:
            if not neighbor in visited or visited[neighbor] > dist:
                queue.append((dist + 1, neighbor))


grid[entr] = '.'
# for _keys in permutations(reachable(keys, (x,y), grid)):
#implement function dist
# for key in sorted(keys, key=distance((x,y), grid), reverse=True):
#     min_dist(0, (x,y), key, keys, grid)

for key in reachable(keys, entr, grid.copy()):
   min_dist(0, entr, key, keys.copy(), grid.copy())

print('Part 1', min(minimums))

# print('reachable', reachable(keys, entr, grid))

# seen = set()
# x,y = entr
# grid[(x,y)] = '.'
# queue = deque([(x,y)])
# d = 0
# while len(queue)>0:
#     x,y = queue.popleft()
#     if (x,y) in seen:
#         continue
#     seen.add((x,y))
#     neighbors = [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if grid[n] == '.' or re.match(r"[a-z]", grid[n])]
#     d+= 1
#     for nb in neighbors:
#         c = grid[nb]
#         if re.match(r"[a-z]", c):
#             _x, _y = doors[c.upper()]
#             grid[(_x, _y)] = '.'
#             grid[nb] = '.'
#             seen = set()
#             keys.remove(c)
#             if len(keys) == 0: print('min path', d)
#         queue.append((nb[0], nb[1]))


# print('min path', d)

#Part 1: 2453 too low not 67942, 22605, 19404, 32500, 35701