"""
Input consists of movement commands. Calculate your final position after responding
to each command. Start frm zero. Report depth multiplied by horizontal position.

Part 1: Commands are:

- forward x: increase horizontal position by x units
- down x: increase depth by x units
- up x: decrease depth by x units

Part 2: COmamnds are:

- down X: increases your aim by X units.
- up X decreases your aim by X units.
- forward X does two things:
    - It increases your horizontal position by X units.
    - It increases your depth by your aim multiplied by X.
"""

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

# Part 1: 2147104
# PPart 2: 2044620088