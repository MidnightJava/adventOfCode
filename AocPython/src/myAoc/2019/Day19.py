import re
import sys
import time
from collections import defaultdict

intersections = set()
loc = None

output = None
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

    def run(self, inp=[]):
        global output
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
                if not inp: break
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
                output = 'HALT'
            else:
                print('Bad Instruction: %d' % op)
                break
        return output

f = open('./2019/data/day19')
code = list(map(int, f.readline().split(',')))
[code.append(0) for _ in range(10000)]
p = Proc(code)

count=0
y = 0
rows = {}
last_x = 0
candidate = None
candidates = defaultdict(list)
start_time = time.time()
while True:
    x = last_x
    xmin = None
    xmax = None
    while True:
        res = Proc(code.copy()).run([y,x])
        res = int(res)
        if res:
            if x < 50 and y < 50: count+= 1
            c = '#'
            if xmin is None:
                xmin = x
        else:
            c = '.'
            if xmin is not None:
                xmax = x
                break
        # print(c, end = '')
        if not xmin and x > y:
            break
        x+= 1
    if xmin is not None: last_x = xmin 

    if xmin is not None and xmax is not None:
        if xmax - xmin >= 100:
            _x = xmax - 100
            for k,v in sorted(candidates.items(), key=lambda x: x[0], reverse=True):
                if k >= xmin:
                    for _y in sorted(v):
                        if y - _y >= 99:
                            print("part 2: %d", (xmin * 10000 + _y))
                            sys.exit()
            
            candidates[_x].append(y)
               

    if y == 49:
        print('Part 1: %d' % count)
        y = 1450
    else:
        y+= 1

# Part 1: 150
# Part 2: 12201460
