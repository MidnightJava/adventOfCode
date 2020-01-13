import re

grid = []
doors = set()
keys = set()

f = open('2019/data/day18')
y = 0
for line in f:
    row = []
    for c in line.strip():
        if re.match(r"[A-Z]", c):
            doors.add(c)
        elif re.match(r"[a-z]", c):
            keys.add(c)
        row.append(c)
    print(len(row))
    grid.append(row)

for row in grid:
    print("".join(row))

print('keys', len(keys), keys)
print('doors', len(doors), doors)