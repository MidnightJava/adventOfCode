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

    def run(self):
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

f = open('./2019/data/day17')
code = list(map(int, f.readline().split(',')))
[code.append(0) for _ in range(10000)]
p = Proc(code)

grid = {}
y, x = 0, 0
max_x = None
while True:
    res = p.run()
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
        max_x = max_x or x
        x = 0
        y+= 1
    else:
        print('Bad result', res)

max_y = y-1

# for y in range(max_y):
#     for x in range(max_x):
#         print(grid[(x, y)], end='')
#     y+= 1

def intersection(x, y):
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
    
score = 0
for y in range(max_y):
    for x in range(max_x):
        if intersection(x, y): score+=(x*y)
    y+= 1

print('Part 1: %d' % score)

#Part 1: 6672

