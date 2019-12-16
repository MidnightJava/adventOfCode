
from collections import defaultdict
import time

count = 0
cmd = []
score = 0
grid = defaultdict(int)
ball = (0,0)
inp = 0
paddle = (0,0)
times = [1, 0.5, 0.2, 0.1, 0.06, 0]
speed = 4
mode = 1 # 0: auto no display, 1: auto display, 2: Semi-Manual 3: Manual
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
                if mode == 2 or mode == 3:
                    _inp = input('>')
                    if mode == 2:
                        inp = ball[0] - paddle[0]
                    else:
                        inp = 0 if _inp == '' else int(_inp)
                    self.code[p1] = inp
                else:
                    inp = ball[0] - paddle[0]
                self.code[p1] = inp
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

def print_grid():
    char_map = [' ', '|', '#', '—', 'o']
    max_x = max(list(map(lambda x: x[0], grid.keys())))
    max_y = max(list(map(lambda x: x[1], grid.keys())))
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(char_map[grid[(x,y)]], end='')
        print()

f = open('./2019/data/day13')
code = list(map(int, f.readline().split(',')))
[code.append(0) for _ in range(10000)]
code[0] = 2
p = Proc(code)
first_draw = False
part2 = False
while True:
    res = p.run()
    count+= 1
    if res == 'HALT':
        if len([c for c in grid.values() if c == 2]) == 0:
            if mode > 0 and first_draw:
                print_grid()
                print('Score: %d' % (score))
            else:
                print('Part 2: %d' % (score))
            break
    cmd.append(res)
    if count % 3 == 0:
        #Reporting score
        if cmd[0] == -1 and cmd[1] == 0:
            score_delt = cmd[2] - score
            score = cmd[2]
            if mode > 0:
                print_grid()
            cmd = []
            first_draw = True
            if not part2:
                print('Part 1: %d' % len([c for c in grid.values() if c == 2]))
                part2 = True
        else:
            grid[(cmd[0], cmd[1])] = cmd[2]
            if cmd[2] == 3:
                paddle = (cmd[0], cmd[1])
            elif cmd[2] == 4:
                if first_draw and ball[1] >= paddle[1]:
                    break
                ball = (cmd[0], cmd[1])
                if mode > 0 and first_draw:
                    print_grid()
                    print('Score: %d' % score)
                    print()
                    print()
                    time.sleep(times[speed])
            cmd = []
        
#Part 1: 363
#Part 17159