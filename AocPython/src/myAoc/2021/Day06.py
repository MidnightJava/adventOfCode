import math
import sys

data = open('2021/data/day06').readlines()[0].split(',')
# fish = map(lambda x: int(x), data)
# fish2 = []

# def more_fish(f):
#     if f == 0:
#         fish2.append(8)
#         return 6
#     else:
#         return f - 1

# for _ in range(80):
#     fish = map(more_fish, fish)
#     fish = fish + fish2
#     fish2 = []

# print('Part 1: %d' % len(fish))

global num_fish
num_fish = 0

def sim_fish(n, days_left):
    # print(n,days_left)
    global num_fish
    if days_left == 0:
        print(num_fish)
        sys.exit(0)
    new_fish = int(math.floor((days_left - n) / 7 ))
    num_fish+= new_fish
    days = days_left
    for i in range(new_fish):
        days-= 7
        if days > 0: sim_fish(8, days)

fish = map(lambda x: int(x), data)
# for f in [3,4,3,1,2]:
for f in fish:
    sim_fish(f, 80)

print('Part 2: %d' % num_fish)



# Part 1: 359344
