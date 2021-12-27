from collections import defaultdict

d = {}
lines = open('2021/data/day14').readlines()

temp1 = lines[0].strip()
for i in range(2, len(lines)):
    vals = lines[i].split('->')
    d[vals[0].strip()] = vals[1].strip()

f1 = defaultdict(int) # freq table for single characters
f2 = defaultdict(int) # freq table for contiguous 2-character values
for c in temp1: f1[c]+= 1
for i in range(len(temp1)-1): f2[temp1[i:i+2]]+= 1

for step in range(40):
    mods = []
    # Remove count of existing 2-char keys and add entries for two keys with
    # inserted product character, with same count.
    for key in f2.keys():
        sub = d[key]
        n = f2[key]
        f1[sub]+= n
        k2 = key[0] + sub
        k3 = sub + key[1]
        # Track dict mods to apply after iterating
        mods.append((k2, n))
        mods.append((k3, n))
        mods.append((key, -n))

    for k,val in mods: f2[k]+= val

    if step == 9:
        res = max(f1.values()) - min(f1.values())
        print('Part 1: %d' % res)

res = max(f1.values()) - min(f1.values())
print('Part 2: %d' % res)

# Part 1: 2657
# Part 2: 2911561572630