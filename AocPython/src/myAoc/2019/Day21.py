import re
import sys
import time
from collections import defaultdict
from itertools import permutations
from bitarray import bitarray

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
                    print(chr(output), end=' ')
                    pass
                else:
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

# instructions = []
# for op in (['NOT', 'OR', 'AND']):
#     for r1 in ['A', 'B', 'C', 'D', 'T', 'J']:
#         for r2 in ['T', 'J']:
#             instructions.append([op, ' ', r1, ' ', r2])

# instructions = []
# for op in (['NOT', 'OR', 'AND']):
#     for r1 in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'T', 'J']:
#         for r2 in ['T', 'J']:
#             instructions.append([op, ' ', r1, ' ', r2])
# print(len(instructions))

proc = Proc(code.copy())
for instr in [ 'NOT A J', 'NOT C T', 'OR T J', 'AND D J']:
    proc.run(makeInstr(instr))
res = proc.run(makeInstr('WALK'))
if res == 'DONE': print('Part 1:', output)

# regs = 'ABCDEFGHI'
# for i in range(2**9):
#     n = "{0:b}".format(i).rjust(9, '0')
#     ba = bitarray(n)
#     holes = [regs[i] for i in range(9) if not ba[i]]
#     ground = [regs[i] for i in range(9) if ba[i]]
#     instrs = []
#     instrs2 = []
#     if holes:
#         instrs.append('NOT %s J' % holes[0])
#         instrs2.append('NOT %s J' % holes[0])
#         for i in range(1, len(holes)):
#             instrs.append('NOT %s T' % holes[i])
#             instrs2.append('NOT %s T' % holes[i])
#             instrs.append('OR T J')
#             instrs2.append('AND T J')
#         for i in range(len(ground)):
#             instrs.append('AND %s J' % ground[i])
#             instrs2.append('OR %s T' % ground[i])
#             instrs2.append('AND T J')
#         instrs.append('NOT A T')
#         instrs2.append('NOT A T')
#         instrs.append('OR T J')
#         instrs2.append('OR T J')
#         instrs.append('AND D J')
#         instrs2.append('AND D J')

#         proc = Proc(code.copy())
#         for instr in instrs:
#             # print(instr)
#             proc.run(makeInstr(instr))
#         res = proc.run(makeInstr('RUN'))
#         if res == 'DONE':
#             print('Part 2:', output)
#             sys.exit()

#         proc = Proc(code.copy())
#         for instr in instrs2:
#             # print(instr)
#             proc.run(makeInstr(instr))
#         res = proc.run(makeInstr('RUN'))
#         if res == 'DONE':
#             print('Part 2:', output)
#             sys.exit()

instrs = [
    'OR A J',
    'AND B J',
    'AND C J',
    'AND G J',
    'NOT J J',
    'OR A T',
    'AND B T',
    'AND F T',
    'NOT T T',
    'AND T J',
    'NOT A T',
    'AND T J',
    'NOT E T',
    'OR T J',
    'AND D J'
]

proc = Proc(code.copy())
for instr in instrs:
    # print(instr)
    proc.run(makeInstr(instr))
res = proc.run(makeInstr('RUN'))
if res == 'DONE':
    print('Part 2:', output)


# def replace_x(regs, indexes, i):
#     global instrs 
#     instrs[indexes[i][0]] = instrs[indexes[i][0]].replace('X', regs[i][0]  )
#     instrs[indexes[i][1]] = instrs[indexes[i][1]].replace('X', regs[i][1]  )

# # registers = [('A','E'), ('C', 'G'), ('B', 'F'), ('D', 'H')]
# # indexes = [(0,1), (3,4), (6,7), (9,10)]
# # for reg_p in permutations(registers):
# #     for i in range(4):
# #         replace_x(reg_p, indexes, i)

# #     proc = Proc(code.copy())
# #     for instr in instrs:
# #         # print(instr)
# #         proc.run(makeInstr(instr))
# #     res = proc.run(makeInstr('RUN'))
# #     if res == 'DONE':
# #         print('Part 2:', output)
# #         sys.exit()

"""
Alternate Part1: (hole at 1,2, or 3 and ground at 4)[ 'NOT A J', 'NOT B T', 'OR T J''NOT C T', 'OR T J', 'AND D J']
boolean: (NOT A OR NOT B OR NOT C) and D

Part 2:
Try:
((ground at 4 and ground at 8) or (hole at 1))

OR D T
AND H T
OR T J
NOT A T
OR T J

TRY:

not(1 and 2 and 3 and 7) and not(1 and 2 and 6) and not(1 and 5) and 4
'OR A J',
'AND B J',
'AND C J',
'AND G J',
'NOT J J',
'OR A T',
'AND B T',
'AND F T',
'NOT T T',
'AND T J',
'NOT A T',
'AND T J',
'NOT E T',
'OR T J',
'AND D J'



'NOT T T',
'OR T J',
'NOT B T',
'OR B T',
'AND F T',
'NOT T T',
'AND T J',
'OR A T',
'AND E T'
'NOT T T',
'AND T J',
'AND D J'
'NOT A T',
'OR T J'

(4 and 8) and not (3 and 7) and not (2 and 6) or not (1 and 5)
(4 and 8) and (not 3 or not 7) and (not 2 or not 6) and (not 1 or not 5) or not 1
'OR D T',
'AND H T',
'OR T J',
'OR C T',
'AND G T',
'NOT T T',
'AND T J',
'OR B T',
'AND F T',
'NOT T T',
'AND T J',
'OR A T',
'AND E T',
'NOT T T',
'AND T J'

'OR D T',
'AND H T',
'OR T J',
'NOT C T',
'NOT G T',
'AND T J',
'NOT B T',
'NOT F T',
'AND T J',
'NOT A T',
'NOT E T',
'AND T J',
'NOT A T',
'OR T J'

(1 and 5) and (not 3 or not 7) and (not 2 or not 6) and (not 4 or not 8) or not 1
indexes: (0,1), (3,4), (6,7), (9,10)
'OR X T',
'AND X T',
'OR T J',
'NOT X T',
'NOT X T',
'AND T J',
'NOT X T',
'NOT X T',
'AND T J',
'NOT X T',
'NOT X T',
'AND T J',
'NOT A T',
'OR T J'

not 1 or (not(2 and 6) and not (3 and 7) and not(4 and 8) and not (5 and 9))
'OR B T',
'AND F T',
'NOT T T',
'AND T J',
'OR C T',
'AND G T',
'NOT T T',
'AND T J',
'OR D T',
'AND H T',
'NOT T T',
'AND T J',
'NOT A T',
'OR T J'
"""
# proc = Proc(code)
# for instr in ['NOT A T', 'NOT A J', 'NOT C T', 'OR T J', 'AND D J']:
#     proc.run(makeInstr(instr))
# proc.run(makeInstr('RUN'))

# Brute force part 1 solution
# for n in range(5,15):
#     for p in permutations(instructions, n):
#         proc = Proc(code.copy())
#         for instr in p:
#             proc.run(makeInstr("".join(instr)))
#         res = proc.run(makeInstr('WALK'))
#         if res == 'DONE':
#             print('Part 1:', output)
#             print(list(map(lambda x: "".join(x), p)))
#             # sys.exit()

# Part 1: 19355364 ['NOT A J', 'NOT C T', 'OR T J', 'AND D J']
# Hole 1 or 3 spaces away and ground 4 spaces away