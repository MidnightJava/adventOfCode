from collections import defaultdict
from math import atan2
from math import sqrt
import pprint
import sys
global moons

PRECISION=4
# moons = [
#     {"p": [13,9,5], "v": [0,0,0]},
#     {"p": [8,14,-2], "v": [0,0,0]},
#     {"p": [-5,4,11], "v": [0,0,0]},
#     {"p": [2,-6,1], "v": [0,0,0]}
# ]

# moons = [
#     {"p": [-1,0,2], "v": [0,0,0]},
#     {"p": [2,-10,-7], "v": [0,0,0]},
#     {"p": [4,-8,8], "v": [0,0,0]},
#     {"p": [3,5,-1], "v": [0,0,0]}
# ]

moons = [
    {"p": [8,-10,0], "v": [0,0,0]},
    {"p": [5,5,10], "v": [0,0,0]},
    {"p": [2,-7,3], "v": [0,0,0]},
    {"p": [9,-8,-3], "v": [0,0,0]}
]

def calc_energy():
    energy = 0
    for moon in moons:
        energy+= sum(list(map(lambda x: abs(x), moon["p"]))) * sum(list(map(lambda x: abs(x), moon["v"])))
    return energy

def calc_energy2():
    energy = [0,0,0,0]
    i = 0
    for moon in moons:
        energy[i] = sum(list(map(lambda x: abs(x), moon["p"]))) * sum(list(map(lambda x: abs(x), moon["v"])))
        i+= 1
    return energy

def update_pos(mult=1):
    mult = 1
    snap = []
    for moon in moons:
        p = moon["p"]
        v = moon["v"]
        for i in range(3):
           p[i]+= (mult * v[i])
        print(p, v)
        # snap.append({'p': (p[0], p[1], p[2]), 'v': (v[0], v[1], v[2])})
        # snap.append(round(sqrt(p[0]**2 + p[1]**2 + p[2]**2), PRECISION))
        # snap.append(atan2(p[1], p[0]))
        snap.append((p[0], p[1], p[2]))
        # snap.append(abs(p[0]) + abs(p[1]) + abs(p[2]))
    # print(snap[0])
    print()
    return snap
        
        

def update_vel():
    global moons
    new_moons = moons[:]
    i = 0
    for m1 in moons:
        vels = m1['v'][:]
        for axis in range(3):
            incr = 0
            for m2 in moons:
                if m2 != m1:
                        delt = m2["p"][axis] - m1["p"][axis]
                        if delt > 0:
                            incr+= 1
                        elif delt < 0:
                            incr-= 1
            vels[axis]+= incr
        new_moons[i]["v"] = vels
        i+= 1
    moons = new_moons



# for n in range(1000):
#     # global moons
#     update_vel()
#     update_pos()
    
# print('Part 1: : %d' % calc_energy())

# snaps = [
#     set([(-1,0,2,0,0,0)]),
#     set([(2,-10,-7,0,0,0)]),
#     set([(4,-8,8,0,0,0)]),
#     set([(3,5,-1,0,0,0)])
# ]

initial_state = [
    {"p": (13,9,5), "v": (0,0,0)},
    {"p": (8,14,-2), "v": (0,0,0)},
    {"p": (-5,4,11), "v": (0,0,0)},
    {"p": (2,-6,1), "v": (0,0,0)}
    # round(sqrt(13**2 + 9**2 + 5**2), PRECISION),
    # round(sqrt(8**2 + 14**2 + 2**2), PRECISION),
    # round(sqrt(5**2 + 4**2 + 11**2), PRECISION),
    # round(sqrt(2**2 + 6**2 +1), PRECISION)
    # atan2(9, 13),
    # atan2(14, 8,),
    # atan2(4, -5),
    # atan2(-6, 2)
]

# snaps = [
#     set([atan2(9, 13)]),
#     set([atan2(14, 8)]),
#     set([atan2(4, -5)]),
#     set([atan2(-6, 2)])
# ]

snaps = set()

count = 1
count2 = 1
seen = [
    defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
]

# i = 1
# res = update_pos(1)
# while True:
#     i+= 1
#     update_vel()
#     res2 = update_pos(i)
#     if res == res2:
#         print(i)
#         break
#     res = res2
#     if i % 1000000 == 0:
#         print('Checking %d' % i)
#     i+=1

freqs = defaultdict(list)
found = 0
while True:
    update_vel()
    snap = update_pos()
    energy = calc_energy2()

    # for i in range(4):
        # if snap[i] == snaps[i]:
        #     print('Moon %d repeats position at count %d' % (i, count))
    # for i in range(4):
    #     if snap[i] == snaps[i]:
    #         print('moon %d repeated orbit after : %d' % (i, count))
    #     else:
    #         snaps[i].add(snap[i])
    

    # i = 1
    # for i in range(4):
    #     # if snap[i] in snaps[i]:
    #     if len(seen[i][snap[i]['v']]):
    #         if count % seen[i][snap[i]['v']][-1] == 0:
    #             print('moon %d is repeating velocity at : %d' % (i, count))
    #             count2 = count
    #             seen[i][snap[i]['v']].append(count)
    #     else:
    #         seen[i][snap[i]['v']].append(count)
    # if count == 1000000:
    #     for k,v in seen[i].items():
    #         if len(v) > 3:
    #             print('%s has %d values %s' % (k, len(v), v))
    #     break

    # for i in range(4):
    #     if snap[i]['p'] == initial_state[i]['p']:
    #         # print('moon %d repeated initial radius after : %d' % (i, count))
    #         freqs[i].append(count)
    #         pprint.PrettyPrinter().pprint(freqs.items())

    # found = [0,0,0,0]
    # for i in range(4):
    i = 0
    if (i, energy[i]) in snaps:
        if count % 74 == 0:
            print('Moon %d repeats energy %d at %d' % (i, energy[i], count))
            # found[i] = 1
            found+= 1
    else:
        snaps.add((i, energy[i]))
    count+= 1
    # if sum(found) == 4:
    #     break
    if found == 50: break

print(high_z)
print(max_z)
# print(moons)

# def lcm(x, y):  
#     if x > y:  
#         greater = x  
#     else:  
#         greater = y  
#     while(True):  
#         if((greater % x == 0) and (greater % y == 0)):  
#             lcm = greater  
#             break  
#         greater += 1  
#     return lcm 
#pos
# rpts = [45, 46, 799, 1164]
#320862420
#vel
# rpts=[46,88,237,427]
#204826776
# p2 = lcm(rpts[0], rpts[1])
# p2 = lcm(p2, rpts[2])
# p2 = lcm(p2, rpts[3])

# part2 = lcm(204826776, 320862420)
print("Part 2: %d" % count)



#Part 1: 6490
#Part 2: 238,120,344,304,920 too low 863,592,666,407,024,130 too high