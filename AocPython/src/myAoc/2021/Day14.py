from collections import defaultdict

d = {}
lines = open('2021/data/day14').readlines()

temp = lines[0].strip()
for i in range(2, len(lines)):
    parts = lines[i].split('->')
    d[parts[0].strip()] = parts[1].strip()

# Brute force method. Works only for part 1
# for step in range(40):
#     subs = []
#     for i in range(0,len(temp)-1):
#         subs.append(d[temp[i] + temp[i+1]])
#     subs = subs[::-1]
#     templ = list(temp)
#     i = len(templ) - 1
#     for sub in subs:
#         templ.insert(i, sub)
#         i-= 1
#     temp = ''.join(templ)

# f = defaultdict(int)
# for c in temp: f[c]+= 1
# res = max(f.values()) - min(f.values())
# print('Part 1: %d' % res)

f1 = defaultdict(int)
f2 = defaultdict(int)
for c in temp: f1[c]+= 1
for i in range(len(temp)-1):
    f2[temp[i:i+2]]+= 1
for step in range(40):
    mods = []
    for key in f2.keys():
        sub = d[key]
        f1[sub]+= f2[key]
        k2 = key[0] + sub
        k3 = sub + key[1]
        mods.append((k2, f2[key]))
        mods.append((k3, f2[key]))
        mods.append((key, -f2[key]))
    for mod in mods:
        k,val = mod
        f2[k]+= val
    if step == 9:
        res = max(f1.values()) - min(f1.values())
        print('Part 1: %d' % res)

res = max(f1.values()) - min(f1.values())
print('Part 2: %d' % res)

# Part 1: 2657
# Part 2: 2911561572630