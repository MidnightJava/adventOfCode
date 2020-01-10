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

    def run(self, inp=None):
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
                self.code[p1] = inp.pop()
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

def print_grid(grid, max_x, max_y):
    print()
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(grid.get((x, y), ' '), end='')
        y+= 1
        print()
    print()

def intersection(grid, x, y, max_x, max_y):
        res = True
        if grid[(x,y)] == '#':
            if x == 0: res&= grid[(x+1,y)] == '#'
            elif x == max_x-1: res&= grid[(x-1,y)] == '#'
            else: res&= (grid[(x-1,y)] == '#' and grid[(x+1,y)] == '#')

            if y == 0: res&= grid[(x,y+1)] == '#'
            elif y == max_y-1: res&= grid[(x,y-1)] == '#'
            else: res&= (grid[(x,y-1)] == '#' and grid[(x,y+1)] == '#')
        else:
            res = False
        return res



def run(p, rules=None, part1=False):
    grid = {}
    y, x = 0, 0
    while True:
        res = p.run(rules)
        if res == 'HALT':
            break
        if res == 35: 
            grid[(x,y)] = '#'
            x+= 1
        elif res == 46:
            grid[(x,y)] = '.'
            x+= 1
        elif res == 60:
            grid[(x,y)] = '<'
            x+= 1
        elif res == 62:
            grid[(x,y)] = '>'
            x+= 1
        elif res == 94:
            grid[(x,y)] = '^'
            x+= 1
        elif res == 118:
            grid[(x,y)] = 'v'
            x+= 1
        elif res == 10:
            x = 0
            y+= 1
        elif res == 88:
            grid[(x,y)] = 'X'
            x+= 1
        else:
            grid[(x,y)] = chr(res)
            if res > 255: print('CHAR:', res)
            print(chr(res), end='')
        

    max_y = max(map(lambda x: x[1], grid.keys()))
    max_x = max(map(lambda x: x[0], grid.keys()))
    
    if part1:
        score = 0
        for y in range(max_y):
            for x in range(max_x):
                if intersection(grid, x, y, max_x, max_y): score+=(x*y)
            y+= 1

        print('Part 1: %d' % score)
    print_grid(grid, max_x, max_y)
    print()

f = open('./2019/data/day17')
code = list(map(int, f.readline().split(',')))
[code.append(0) for _ in range(10000)]
p = Proc(code)
run(p, part1=True)


f = open('./2019/data/day17')
code = list(map(int, f.readline().split(',')))
[code.append(0) for _ in range(10000)]
code[0] = 2
p = Proc(code)
rules = [65,44,66,44,67,10,76,10,49,44,49,44,49,10,49,44,49,44,49,10,121,10][::-1]
run(p, rules)
#Part 1: 6672

