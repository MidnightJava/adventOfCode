pos = 0
depth = 0

with open('2021/data/day02') as f:
    for line in f:
        cmd, ns = line.split()
        n = int(ns)
        if cmd == 'forward':
            pos+= n
        elif cmd == 'down':
            depth+= n
        elif cmd == 'up':
            depth-= n

print('Part 1: %d' % (depth * pos))

pos = 0
depth = 0
aim = 0

with open('2021/data/day02') as f:
    for line in f:
        cmd, ns = line.split()
        n = int(ns)
        if cmd == 'forward':
            pos+= n
            depth+= (aim * n)
        elif cmd == 'down':
            aim+= n
        elif cmd == 'up':
            aim-= n

print('Part 2: %d' % (depth * pos))

# Part 2 < 3900982024