'''
Created on Jan 2, 2017

@author: Mark
'''

#Copied this solution from https://www.reddit.com/r/adventofcode/comments/5hoia9/2016_day_11_solutions/db1zbu0/
#Just solves part 1
from itertools import combinations
import heapq

# hardcoded input
promethium, cobalt, curium, ruthenium, plutonium = 1, 2, 3, 4, 5
initial = (0, (
    tuple(sorted((promethium, -promethium))),
    tuple(sorted((cobalt, curium, ruthenium, plutonium))),
    tuple(sorted((-cobalt,-curium,-ruthenium,-plutonium))), ()
))

def correct(floor):
    if not floor or floor[-1] < 0: # no generators
        return True
    return all(-chip in floor for chip in floor if chip < 0)

frontier = []
heapq.heappush(frontier, (0, initial))
cost_so_far = {initial: 0}

while frontier:
    _, current = heapq.heappop(frontier)
    floor, floors = current
    if floor == 3 and all(len(f) == 0 for f in floors[:-1]): # goal!
        break

    directions = [dir for dir in (-1, 1) if 0 <= floor + dir < 4]
    moves = list(combinations(floors[floor], 2)) + list(combinations(floors[floor], 1))
    for move in moves:
        for direction in directions:
            new_floors = list(floors)
            new_floors[floor] = tuple(x for x in floors[floor] if x not in move)
            new_floors[floor+direction] = tuple(sorted(floors[floor+direction] + move))

            if not correct(new_floors[floor]) or not correct(new_floors[floor+direction]):
                continue

            next = (floor+direction, tuple(new_floors))
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost - len(new_floors[3])*10 # silly manually tweakable heuristic factor
                heapq.heappush(frontier, (priority, next))

print(cost_so_far[current], current)

# Copied this solution from https://www.reddit.com/r/adventofcode/comments/5hoia9/2016_day_11_solutions/db2ela7/

print "Part 1: "
print sum(2 * sum([2, 4, 4, 0][:x]) for x in range(1, 4)) - 3

print "Part 2: "
print sum(2 * sum([6, 4, 4, 0][:x]) for x in range(1, 4)) - 3