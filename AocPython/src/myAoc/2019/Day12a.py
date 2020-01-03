from collections import defaultdict
from math import atan2
from math import sqrt
import pprint
import sys
global moons

#Data
moons = [
    {"p": [13,9,5], "v": [0,0,0]},
    {"p": [8,14,-2], "v": [0,0,0]},
    {"p": [-5,4,11], "v": [0,0,0]},
    {"p": [2,-6,1], "v": [0,0,0]}
]
 #Example 1
moons = [
    {"p": [-1,0,2], "v": [0,0,0]},
    {"p": [2,-10,-7], "v": [0,0,0]},
    {"p": [4,-8,8], "v": [0,0,0]},
    {"p": [3,5,-1], "v": [0,0,0]}
]

#Example 2
# moons = [
#     {"p": [8,-10,0], "v": [0,0,0]},
#     {"p": [5,5,10], "v": [0,0,0]},
#     {"p": [2,-7,3], "v": [0,0,0]},
#     {"p": [9,-8,-3], "v": [0,0,0]}
# ]

def calc_energy():
    energy = 0
    for moon in moons:
        energy+= sum(list(map(lambda x: abs(x), moon["p"]))) * sum(list(map(lambda x: abs(x), moon["v"])))
    return energy

def update_pos():
    mult = 1
    snap = []
    for moon in moons:
        p = moon["p"]
        v = moon["v"]
        for i in range(3):
           p[i]+= (mult * v[i])
        snap.append({'p': (int(p[0]), int(p[1]), int(p[2])), 'v': (int(v[0]), int(v[1]), int(v[2]))})
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

#Check repeats of zero velocity for each moon
count = 1

last_0_count = 0
last_1_count = 0
last_2_count = 0
last_3_count = 0
while True:
    update_vel()
    snap = update_pos()
    if snap[0]['v'] == (0,0,0):
        print('Moon 1 zero celcoity repeat: %d' % (count - last_0_count))
        last_0_count = count
    if snap[1]['v'] == (0,0,0):
        print('Moon 2 zero celcoity repeat: %d' % (count - last_1_count))
        last_1_count = count
    if snap[2]['v'] == (0,0,0):
        print('Moon 3 zero celcoity repeat: %d' % (count - last_2_count))
        last_2_count = count
    if snap[3]['v'] == (0,0,0):
        print('Moon 4 zero celcoity repeat: %d' % (count - last_3_count))
        last_3_count = count
    count+= 1

# Check repeats of x,y,z indepependently for all 4 moons
count = 1
xs = [-1,2,4,3]
ys= [0,-10,-8,5]
zs = [2,-7,8,-1]
last_x_count = 0
last_y_count = 0
last_z_count = 0
while True:
    update_vel()
    snap = update_pos()
    _xs = [snap[i]['p'][0] for i in range(4)]
    _ys = [snap[i]['p'][1] for i in range(4)]
    _zs = [snap[i]['p'][2] for i in range(4)]
    if xs == _xs:
        print('xs repeat: %d' % (count - last_x_count))
        last_x_count = count
    if ys == _ys:
        print('ys repeat: %d ' % (count - last_y_count))
        last_y_count = count
    if zs == _zs:
        print('zs repeat: %d ' % (count - last_z_count))
        last_z_count = count
    count+= 1

#No help loking at x,y, and z independently for each moon.
#Moon1 repeats: x: 1,5  y: 1,27  z: 1,5,33
#Moon2 repeats: x: 1,4 y: 1,27 z: 1,43
#Moon3 repeats: x: 1,17 y: 1,9  z: 1,43
#Moon4 repeatsL x: 1,5 y: 1,27  z: 1,5,33

#Check repeats of max distance for each moon independently
while True:
    update_vel()
    snap = update_pos()[0]['p']
    snap_d = sum([abs(x) for x in snap])
    if snap_d == 347:
        print(count - last_count)
        last_count = count
    if snap_d > max_d:
        max_d = snap_d
        print('Max D: %d Delta: %d' % (snap_d, count - last_max_count))
        last_max_count = count
    if snap_d < min_d:
        min_d = snap_d
        print('Min D: %d Delta: %d' % (snap_d, count - last_min_count))
        last_min_count =  count
    if count == 1000:
        print('Part 1: %d' % calc_energy())
        # break
    count+= 1

# Example #1
# Moon 1: x: (-1, 5), y: (-9, 3),  z: (-6, 8)
# Moon 2: x: (0, 4),  y: (-10, 5), z: (-7, 7)
# Moon 3: x: (0, 4),  y: (-9, 3),  z: (-6, 8)
# Moon 4: x: (1, 3),  y: (-10, 5), z: (-7, 7)
# All Moons: x: (-1, 5), y: (-10, 5), z: (-7, 8)

# Example #2
# Moon 1: x: (-1, 5), y: (-9, 3),  z: (-6, 8)

#Periods of max dist

#Example 1
# moon1 353,571  moon2: 83,1681  moon3: 1585,1187 moon 4: 1,83
# Answer = 1585+1187

#Example 2
# moon1 dist = 347. Period = 


#REAL DATA

#Periods of max dist

# moon1 dist = 3414. Period = 4382881
# moon2 dist = 2875. Period = 2816247
# moon3 dist = 3065. Period = 2815321
# moon4 dist = 4078. Period = 4978827

# LCM = 1246393346021130240 (not correct)
