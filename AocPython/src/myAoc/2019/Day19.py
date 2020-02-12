import re
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

def print_grid(grid, max_x, max_y):
    print()
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(grid.get((x, y), ' '), end='')
        y+= 1
        print()
    print()


f = open('./2019/data/day19')
code = list(map(int, f.readline().split(',')))
[code.append(0) for _ in range(10000)]
p = Proc(code)

count=0
start = y = 10000
rows = {}
while True:
    x = y
    xmin = None
    xmax = None
    while True:
        res = Proc(code.copy()).run([y,x])
        res = int(res)
        if res:
            count+= 1
            c = '#'
            if xmin is None:
                xmin = x
                rows[y] = [xmin]
        else:
            c = '.'
            if xmin:
                xmax = x
                rows[y].append(xmax)
                break
        # print(c, end = '')
        if not xmin and x > y:
            break
        if xmin and not xmax and x - xmin > 200:
            rows[y].append(x)
            break
        x+= 1
    
    # print()
    
    if y in rows and len(rows[y]) == 2 and rows[y][1] - rows[y][0] >= 100:
        print('Row %d' % y)
    if y in rows: print(y, len(rows[y]))
    y+= 1000
        # print(y, rows[y][0], rows[y][1], rows[y][1] - rows[y][0])
    # if len(rows[y]) == 2 and y > start+99 and len(rows[y-99]) == 2:
    #     r1 = rows[y]
    #     r2 = rows[y-99]
    #     if r2[0] > r1[0] and r2[1] < r1[1]:
    #         print('Found match at row %d' % y)
    #         break



    #     print('Current row: %s,  up100 row: %s' % (rows[y], rows[y-99]))
    #     r = rows[y]
    #     if r[1] - r[0] >= 100 and y >= 900 and rows[y-99][0] >= r[0] and rows[y-99][1] - rows[y-99][0] >= 100:
    #         print("part 2:", (x * 10000 + y - 100))
    #         break
    # if len(rows[y]) == 2 and rows[y][1] - rows[y][0] > 100:
    #     print(y, rows[y])

    # if y in rows: print(rows[y])
    # if y == 49:
    #     print('Part 1:', count)
    #     break
    # y+= 1
    # if xmax and xmin: print('DIFF', xmax - xmin)
    # if xmin: print((xmin, xmax))
