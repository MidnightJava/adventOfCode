with open('./2019/data/day09a') as f:
    inp = f.readline().split(',')
    input = 1
    pos = 0
    relb = 0

    def get_inp(pos):
        if pos >= len(inp):
            for i in range(len(inp), pos+1):
                inp.append('0')
        return inp[pos]

    def set_inp(pos, val):
        if pos >= len(inp):
            for i in range(len(inp), pos+1):
                inp.append('0')
        inp[pos] = val

    def get_params(m1, m2, m3):
        if m1 == 0:
            p1 = get_inp(int(get_inp(pos+1)))
        elif m1 == 1:
            p1 = get_inp(pos+1)
        elif m1 == 2:
            p1 = str(int(get_inp(int(get_inp(pos+1)))) + relb)
        if m2 == 0:
            p2 = get_inp(int(get_inp(pos+2)))
        elif m2 == 1:
            p2 = get_inp(pos+2)
        elif m2 == 2:
            p2 = str(int(get_inp(int(get_inp(pos+2)))) + relb)
        if m3 == 0:
            p3 = int(get_inp(int(get_inp(pos+3))))
        elif m3 == 1:
            p3 = int(get_inp(pos+3))
        elif m3 == 2:
            p3 = int(get_inp(int(get_inp(pos+3)))) + relb
        return (p1, p2, p3)

    while get_inp(pos) != 99:
        instr = get_inp(pos)
        op = int(instr[-2]) * 10 + int(instr[-1]) if len(instr) > 1 else int(instr[0])
        m1 = int(instr[-3]) if len(instr) > 2 else 0
        m2 = int(instr[-4]) if len(instr) > 3 else 0
        m3 = int(instr[-5]) if len(instr) > 4 else 0
        if op == 1:
            p1, p2, p3 = get_params(m1, m2, m3)
            set_inp(p3, str(int(p1) + int(p2)))
            pos+= 4
        elif op == 2:
            p1, p2, p3 = get_params(m1, m2, m3)
            set_inp(p3, str(int(p1) * int(p2)))
            pos+= 4
        elif op == 3:
            p1, p2, p3 = get_params(m1, m2, m3)
            # if m1 == 0:
            #     set_inp(int(get_inp(int(get_inp(pos+1)))), str(input))
            # elif m1 == 1:
            #     set_inp(int(get_inp(pos+1)), str(input))
            # elif m1 == 2:
            #     set_inp(int(get_inp(int(get_inp(pos+1))+relb)), str(input))
            set_inp(int(p1), str(input))
            pos+= 2
        elif op == 4: #OUTP
            p1, p2, p3 = get_params(m1, m2, m3)
            output = p1
            # if m1 == 0:
            #     output = get_inp(int(p1))
            # elif m1 == 1:
            #     output = p1
            # elif m1 == 2:
            #     output = get_inp(int(p1) + relb)
            # if m1 == 0:
            #    out_addr = get_inp(int(get_inp(pos+1)))
            # elif m1 == 1:
            #     out_addr = get_inp(pos+1)
            # elif m1 == 2:
            #     out_addr = get_inp(int(get_inp(pos+1))+ relb)
            # output = get_inp(int(p1))
            # output = get_inp(int(out_addr))
            print('Output: %s, m1: %d' % (output, m1))
            pos+= 2
        elif op == 5:#JMP IF TRUE
            p1, p2, p3 = get_params(m1, m2, m3)
            pos = int(p2) if int(p1) != 0 else pos+3
        elif op == 6:#JMP IF FALSE
            p1, p2, p3 = get_params(m1, m2, m3)
            pos = int(p2) if int(p1) == 0 else pos+3
        elif op == 7:#LT
            p1, p2, p3 = get_params(m1, m2, m3)
            if int(p1) < int(p2):
                set_inp(p3, "1")
            else:
                set_inp(p3, "0")
            pos+= 4
        elif op == 8:#EQ
            p1, p2, p3 = get_params(m1, m2, m3)
            set_inp(p3, "1" if int(p1) == int(p2) else "0")
            pos+= 4
        elif op == 9:#SET RELB
            p1, p2, p3 = get_params(m1, m2, m3)
            # if m1 == 0:
            #     relb+= int(get_inp(int(get_inp(pos+1))))
            # elif m1 == 1:
            #     relb+= int(get_inp(pos+1))
            # elif m1 == 2:
            #      relb+= int(get_inp(int(get_inp(pos+1))+ relb))
            relb+= int(p1)
            pos+= 2
        elif op == 99:
            print('Halt: %s' % output)
            break
        else:
            print('Bad Instruction: %d' % op)
            break

#Ans > 203 not 34463338