
from collections import defaultdict

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

    def run(self, inp):
        global count
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
                self.code[p1] = inp
                self.pos+= 2
            elif op == 4: #OUTP
                output = self.code[p1]
                # if inp is not None: print(output, end='')
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

f = open('./2019/data/day11')
code = list(map(int, f.readline().split(',')))
[code.append(0) for _ in range(10000)]
p = Proc(code)

grid = defaultdict(int)
grid[(0,0)] = 1
seen = set()
color = 1
curr = (0,0)
count = 0
dir = 0 #0:up, 1:right, 2:down, 3:left
while color != 'HALT':
    color = p.run(grid[curr])
    grid[curr] = color
    if not curr in seen:
        count+= 1
        seen.add(curr)
    new_dir = p.run(None)
    if new_dir == 0: #turn left
        if dir == 0: #up
            curr = (curr[0]-1, curr[1])
            dir = 3
        elif dir == 1: #right
            curr = (curr[0], curr[1]-1)
            dir = 0
        elif dir == 2: #down
            curr = (curr[0]+1, curr[1])
            dir = 1
        elif dir == 3: #left
            curr = (curr[0], curr[1]+1)
            dir = 2
    elif new_dir == 1: #turn right
        if dir == 0: #up
            curr = (curr[0]+1, curr[1])
            dir = 1
        elif dir == 1: #right
            curr = (curr[0], curr[1]+1)
            dir = 2
        elif dir == 2: #down
            curr = (curr[0]-1, curr[1])
            dir = 3
        elif dir == 3: #left
            curr = (curr[0], curr[1]-1)
            dir = 0

print('Part 1: %d' % count)

#Part 1: 5794 too high not 5380
    