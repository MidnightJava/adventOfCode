
global moons
moons = [
    {"p": [13,9,5], "v": [0,0,0]},
    {"p": [8,14,-2], "v": [0,0,0]},
    {"p": [-5,4,11], "v": [0,0,0]},
    {"p": [2,-6,1], "v": [0,0,0]}
]

# moons = [
#     {"p": [-1,0,2], "v": [0,0,0]},
#     {"p": [2,-10,-7], "v": [0,0,0]},
#     {"p": [4,-8,8], "v": [0,0,0]},
#     {"p": [3,5,-1], "v": [0,0,0]}
# ]

def calc_energy():
    energy = 0
    for moon in moons:
        energy+= sum(list(map(lambda x: abs(x), moon["p"]))) * sum(list(map(lambda x: abs(x), moon["v"])))
    return energy

def update_pos():
    snap = []
    for moon in moons:
        p = moon["p"]
        v = moon["v"]
        for i in range(3):
           p[i]+= v[i]
        snap.append((p[0], p[1], p[2]))
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



for n in range(1000):
    # global moons
    update_vel()
    update_pos()
    
print('Part 1: : %d' % calc_energy())

moons = [
    {"p": [13,9,5], "v": [0,0,0]},
    {"p": [8,14,-2], "v": [0,0,0]},
    {"p": [-5,4,11], "v": [0,0,0]},
    {"p": [2,-6,1], "v": [0,0,0]}
]

snaps = [
    set([(13,9,5)]),
    set([(8,14,-2)]),
    set([(-5,4,11)]),
    set([(2,-6,1)])
]

count = 1
count2 = 1
seen = set()
while True:
    update_vel()
    snap = update_pos()
    # energy = calc_energy()
    i = 0
    # for i in range(4):
    if snap[i] in snaps[i]:
    # if energy in seen:
        print('moon %d repeated energy after : %d, since last repeat : %d' % (i, count, count-count2))
        count2 = count
    else:
        snaps[i].add(snap[i])
        # seen.add(energy)
    count+= 1

def lcm(x, y):  
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm 

rpts = [8909451, 14842822, 22810758, ]
p2 = lcm(rpts[0], rpts[1])
p2 = lcm(p2, rpts[2])
p2 = lcm(p2, rpts[3])
print("Part 2: %d" % p2)

#Part 1: 6490