class Proc:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.relb = 0

    def get_params(self, modes):
        params = []
        i = 1
        for m in modes:
            params.append(self.code[self.pos+i] if m == 0 else (self.pos+i if m == 1 else self.code[self.pos+i] + self.relb))
            i+= 1
        return params

    def move(self, inp):
        while True:
            instr = str(self.code[self.pos])
            op = int(instr[-2]) * 10 + int(instr[-1]) if len(instr) > 1 else int(instr[0])
            modes = [
                int(instr[-3]) if len(instr) > 2 else 0,
                int(instr[-4]) if len(instr) > 3 else 0,
                int(instr[-5]) if len(instr) > 4 else 0
            ]
            p1,p2,p3 = self.get_params(modes) # pylint: disable=unbalanced-tuple-unpacking
            if op == 1: #ADD
                self.code[p3] = self.code[p1] + self.code[p2]
                self.pos+= 4
            elif op == 2: #MULT
                self.code[p3] = self.code[p1] * self.code[p2]
                self.pos+= 4
            elif op == 3: #INP
                self.code[p1] = int(inp)
                self.pos+= 2
            elif op == 4: #OUTP
                output = self.code[p1]
                self.pos+= 2
                break
            elif op == 5:#JMP IF TRUE
                self.pos = self.code[p2] if self.code[p1] else self.pos+3
            elif op == 6:#JMP IF FALSE
                self.pos = self.code[p2] if not self.code[p1] else self.pos+3
            elif op == 7:#LT
                self.code[p3] = 1 if self.code[p1] < self.code[p2] else 0
                self.pos+= 4
            elif op == 8:#EQ
                self.code[p3] = 1 if self.code[p1] == self.code[p2] else 0
                self.pos+= 4
            elif op == 9:#SET RELB
                self.relb+= self.code[p1]
                self.pos+= 2
            elif op == 99:
                output = "HALT"
                break
            else:
                print('Bad Instruction: %d' % op)
                break
        return output

min_x = int(1e6)
max_x = -int(1e6)
min_y = int(1e6)
max_y = -int(1e6)

OPP_MOVE = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

def move(x, y, direc):
    if direc == 1: y-= 1
    elif direc == 2: y+= 1
    elif direc == 3: x-= 1
    elif direc == 4: x+= 1
    else: print('Invalid direction %d' % direc)
    return (x, y)

def set_min_max_coords(x, y):
    global min_x, min_y, max_x, max_y
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

f = open('./2019/data/day15')
code = list(map(int, f.readline().split(',')))
[code.append(0) for _ in range(10000)]
p = Proc(code)
seen = set()
dists = set()
path = []
dist = 0
grid = {}

def test_move(direc):
    global grid
    res = p.move(direc)
    if res: p.move(OPP_MOVE[direc])
    return res != 0

x, y = (0, 0)
seen.add((x, y))
grid[(x,y)] = '.'
while True:
    moved = False
    for direc in range(1, 5):
        if test_move(direc):
            if not move(x,y, direc) in seen:
                dist+= 1
                res = p.move(direc)
                moved = True
                path.append((OPP_MOVE[direc], dist))
                x, y = move(x, y, direc)
                set_min_max_coords(x, y)
                seen.add((x, y))
                if res == 2:
                    dists.add(dist)
                    grid[(x,y)] = 'O'
                else:
                    grid[(x,y)] = '.'
                break
        else:
            grid[move(x, y, direc)] = '#'
    if not moved:
        if len(path):
            direc, dist = path.pop()
            p.move(direc)
            x, y = move(x, y, direc)
        else:
            break

print('Part 1: %d' % min(dists))

def print_grid():
    for y in range(min_y, max_y +1):
        for x in range(min_x, max_x + 1):
            print(grid.get((x,y),' '), end='')
        print()

# print_grid()

ox = True
count = 0
seen2 = set()
while ox:
    ox = False
    seen2 = set()
    for y in range(min_y, max_y +1):
        for x in range(min_x, max_x + 1):
            if grid.get((x,y), None) == 'O' and not (x,y) in seen2:
                neighbors = [n for n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]]
                for n in neighbors:
                    if grid.get(n, None) == '.':
                        grid[n] = 'O'
                        seen2.add(n)
                        ox = True
    count+= 1

print('Part 2: %d' % (count-1))

#Part 1: 266
#Part 2: 274