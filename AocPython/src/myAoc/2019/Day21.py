import re
import sys
import time
from collections import defaultdict
from itertools import permutations

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
                self.pos+= 2
                if inp:
                    self.code[p1] = inp.pop()
                else:
                    break
            elif op == 4: #OUTP
                output = self.code[p1]
                self.pos+= 2
                if output <= 127:
                    # print(chr(output), end=' ')
                    pass
                else:
                    # print('Part 1:', output)
                    return 'DONE'
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
                # output = 'HALT'
                break
            else:
                print('Bad Instruction: %d' % op)
                break
        return output

def makeInstr(s):
    l = []
    for c in s:
        l.append(ord(c))
        # l.append(ord(','))
    l.append(10)
    return l[::-1]

f = open('./2019/data/day21')
code = list(map(int, f.readline().split(',')))
[code.append(0) for _ in range(10000)]

instructions = []
for op in (['NOT', 'OR', 'AND']):
    for r1 in ['A', 'B', 'C', 'D', 'T', 'J']:
        for r2 in ['T', 'J']:
            instructions.append([op, ' ', r1, ' ', r2])

# instructions = []
# for op in (['NOT', 'OR', 'AND']):
#     for r1 in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'T', 'J']:
#         for r2 in ['T', 'J']:
#             instructions.append([op, ' ', r1, ' ', r2])
# print(len(instructions))

for n in range(5,15):
    for p in permutations(instructions, n):
        proc = Proc(code.copy())
        for instr in p:
            proc.run(makeInstr("".join(instr)))
        res = proc.run(makeInstr('WALK'))
        if res == 'DONE':
            print('Part 1:', output)
            print(list(map(lambda x: "".join(x), p)))
            # sys.exit()

# Part 1: 19355364 ['NOT A T', 'NOT A J', 'NOT C T', 'OR T J', 'AND D J']
# Hole 1 or 3 spaces away and ground 4 spaces away