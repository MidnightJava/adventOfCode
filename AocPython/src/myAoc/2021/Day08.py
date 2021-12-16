digits = []
values = []

f = open('2021/data/day08')
for l in f.readlines():
    inp = l.split('|')
    digits.append(inp[0].split())
    values.append(inp[1].split())

count = 0
for v in values:
    for vv in v:
        if len(vv) == 2 or len(vv) == 3 or len(vv) == 4 or len(vv) == 7: count+= 1

print('Part 1: %d' % count)

# Part 1: >282