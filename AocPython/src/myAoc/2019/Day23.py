import queue
import sys
import time
import threading

queues = [queue.Queue() for _ in range(51)]

stop_threads = False
part1_done = False
last_y = None

class MsgHandler(threading.Thread):
    def run(self):
        global stop_threads, part1_done, last_y
        while not stop_threads:
            if not queues[50].empty():
                addr, x, y = queues[50].get()
                if addr <= 49:
                    queues[addr].put((x,y))
                elif addr == 255:
                    if not part1_done:
                        print('Part 1: %d\ttime %s' % (y, time.time() - start_time))
                        part1_done = True
                    all_idle = True
                    for p in procs:
                        if not p.idle: all_idle = False
                    if all_idle:
                        queues[0].put((x,y))
                        if last_y == y:
                            print('Part 2: %d\ttime: %s' % (y, time.time() - start_time))
                            stop_threads = True
                        last_y = y
            time.sleep(0)
MsgHandler().start()

output = None
class Proc:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.relb = 0
        self.addr = None
        self.read_addr = False
        self.inp = queue.Queue()
        self.out = []
        self.idle = True

    def get_params(self, modes):
        params = []
        i = 1
        for m in modes:
            params.append(self.code[self.pos+i] if m == 0 else (self.pos+i if m == 1 else self.code[self.pos+i] + self.relb))
            i+= 1
        return params

    def run(self, inp):
        self.addr = inp
        while not stop_threads:
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
                if not self.read_addr:
                    self.code[p1] = self.addr
                    self.read_addr = True
                elif not self.inp.empty():
                    self.code[p1] = self.inp.get()
                else:
                    q = queues[self.addr]
                    if not q.empty():
                        p = q.get()
                        self.code[p1] = p[0]
                        self.inp.put(p[1])
                    else:
                        self.code[p1] = -1
                        time.sleep(.001)
                self.idle = self.inp.empty() and queues[self.addr].empty()
            elif op == 4: #OUTP
                output = self.code[p1]
                self.out.append(output)
                if len(self.out) == 3:
                    queues[50].put((self.out[0], self.out[1], self.out[2]))
                    self.out = []
                    self.idle = self.inp.empty() and queues[self.addr].empty()
                else:
                    self.idle = False
                self.pos+= 2
                if not self.idle: time.sleep(.001)
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

f = open('./2019/data/day23')
code = list(map(int, f.readline().split(',')))
[code.append(0) for _ in range(10000)]
procs = [Proc(code.copy()) for _ in range(50)]
threads = []
start_time = time.time()
for i in range(50):
    def func():
        procs[i].run(i)
    threading.Thread(target=func).start()

# Part 1: 20225
# Part 2: 14348