from collections import defaultdict

d = {}
lines = open('2021/data/day14').readlines()

temp = lines[0].strip()
for i in range(2, len(lines)):
    parts = lines[i].split('->')
    d[parts[0].strip()] = parts[1].strip()

for step in range(40):
    subs = []
    for i in range(0,len(temp)-1):
        subs.append(d[temp[i] + temp[i+1]])
    subs = subs[::-1]
    templ = list(temp)
    i = len(templ) - 1
    for sub in subs:
        templ.insert(i, sub)
        i-= 1
    temp = ''.join(templ)

f = defaultdict(int)
for c in temp: f[c]+= 1
res = max(f.values()) - min(f.values())
print('Part 1: %d' % res)

# Part 1: 2657