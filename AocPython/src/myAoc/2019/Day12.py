from math import gcd

moons = [
    {"p": [13,9,5], "v": [0,0,0]},
    {"p": [8,14,-2], "v": [0,0,0]},
    {"p": [-5,4,11], "v": [0,0,0]},
    {"p": [2,-6,1], "v": [0,0,0]}
]

def calc_energy():
    energy = 0
    for moon in moons:
        energy+= sum(list(map(lambda x: abs(x), moon["p"]))) * sum(list(map(lambda x: abs(x), moon["v"])))
    return energy

def update_pos(moons):
    snap = []
    for moon in moons:
        p = moon["p"]
        v = moon["v"]
        for i in range(3): p[i]+= v[i]
        snap.append(v)
    return snap
        
        

def update_vel(moons):
    new_moons = moons[:]
    i = 0
    for m1 in moons:
        vels = m1['v'][:]
        for axis in range(3):
            incr = 0
            for m2 in moons:
                if m2 != m1:
                        delt = m2["p"][axis] - m1["p"][axis]
                        if delt > 0: incr+= 1
                        elif delt < 0: incr-= 1
            vels[axis]+= incr
        new_moons[i]["v"] = vels
        i+= 1
    return new_moons

# Find period when all moons have zero x, y, and z velocity components, independently
count = 1
periods = [None, None, None]
while True:
    moons = update_vel(moons)
    snap = update_pos(moons)
    if count == 1000: print('Part 1: %d' % calc_energy())
    zipped = list(zip(*snap))
    for i in range(3):
        if zipped[i].count(0) == 4: periods[i] = count
    if not None in periods: break
    count+= 1

def lcm(a, b):  
     return a*b // gcd(a, b)

print('Part 2: %d'%  (lcm(lcm(periods[0], periods[1]), periods[2]) * 2))

# Part 1: 6490
# Part 2: 277068010964808