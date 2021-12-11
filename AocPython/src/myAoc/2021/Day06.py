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

def sim_fish(timer, days_left):
    # print(n,days_left)
    global num_fish
    # print(num_fish)
    if days_left == 0:
        print(num_fish)
        sys.exit(0)
    new_fish = int(math.floor((days_left - timer) / 7 ))
    if new_fish > 0:
        num_fish+= new_fish
        days = days_left - timer
        for i in range(new_fish):
            if days > 0:
                sim_fish(8 , days)
                days-= 7
            else:
                num_fish-= 1
                # print(days)

fish = map(lambda x: int(x), data)
num_fish = len(fish)
# for t in [3,4,3,1,2]:
for t in fish:
    sim_fish(t, 80)

print('Part 2: %d' % num_fish)



# Part 1: 359344
