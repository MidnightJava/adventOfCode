with open('./2019/data/day09') as f:
    inp = list(map(int, f.readline().split(',')))
    [inp.append(0) for rin in range(10000)]
    input = 1
    pos = 0
    relb = 0

    def get_params(m1, m2, m3):
        if m1 == 0:
            p1 = inp[inp[pos+1]]
        elif m1 == 1:
            p1 = inp[pos+1]
        elif m1 == 2:
            p1 = inp[int(inp[pos+1])] + relb
        if m2 == 0:
            p2 = inp[inp[pos+2]]
        elif m2 == 1:
            p2 = inp[pos+2]
        elif m2 == 2:
            p2 = inp[inp[pos+2]] + relb
        if m3 == 0:
            p3 = inp[inp[pos+3]]
        elif m3 == 1:
            p3 = inp[pos+3]
        elif m3 == 2:
            p3 = inp[inp[pos+3]] + relb
        return (p1, p2, p3)

    while inp[pos] != 99:
        instr = str(inp[pos])
        op = int(instr[-2]) * 10 + int(instr[-1]) if len(instr) > 1 else int(instr[0])
        m1 = int(instr[-3]) if len(instr) > 2 else 0
        m2 = int(instr[-4]) if len(instr) > 3 else 0
        m3 = int(instr[-5]) if len(instr) > 4 else 0
        if op == 1: #ADD
            # if mode = 1: p1 = pos+1 if mode = 0: p1 = inp[pos+1] if mode = 2: p1 = inp[pos+1] + relb
            # Then when processing opcode us inp[p1]
            p1 = pos+1 if m1 == 1 else inp[pos+1]
            p2 = pos+2 if m2 == 1 else inp[pos+2]
            p3 = pos+3 if m3 == 1 else inp[pos+3]
            if m1 == 2: p1 = inp[pos+1] + relb
            if m2 == 2: p2 = inp[pos+2] + relb
            if m3 == 2: p3 = inp[pos+3] + relb
            inp[p3] = inp[p1] + inp[p2]
            pos+= 4
        elif op == 2: #MULT
            p1 = pos+1 if m1 == 1 else inp[pos+1]
            p2 = pos+2 if m2 == 1 else inp[pos+2]
            p3 = pos+3 if m3 == 1 else inp[pos+3]
            if m1 == 2: p1 = inp[pos+1] + relb
            if m2 == 2: p2 = inp[pos+2] + relb
            if m3 == 2: p3 = inp[pos+3] + relb
            inp[p3] = inp[p1] * inp[p2]
            pos+= 4
        elif op == 3: #INP
            p1 = pos+1 if m1 == 1 else inp[pos+1]
            if m1 == 2: p1 = inp[pos+1] + relb
            inp[p1] = input
            pos+= 2
        elif op == 4: #OUTP
            p1 = pos+1 if m1 == 1 else inp[pos+1]
            if m1 == 2: p1 = inp[pos+1] + relb
            output = inp[p1]
            print('Part n: %d' % output)
            pos+= 2
            break
        elif op == 5:#JMP IF TRUE
            p1 = pos+1 if m1 == 1 else inp[pos+1]
            p2 = pos+2 if m2 == 1 else inp[pos+2]
            if m1 == 2: p1 = inp[pos+1] + relb
            if m2 == 2: p2 = inp[pos+2] + relb
            pos = inp[p2] if inp[p1] else pos+3
        elif op == 6:#JMP IF FALSE
            p1 = pos+1 if m1 == 1 else inp[pos+1]
            p2 = pos+2 if m2 == 1 else inp[pos+2]
            if m1 == 2: p1 = inp[pos+1] + relb
            if m2 == 2: p2 = inp[pos+2] + relb
            pos = inp[p2] if not inp[p1] else pos+3
        elif op == 7:#LT
            p1 = pos+1 if m1 == 1 else inp[pos+1]
            p2 = pos+2 if m2 == 1 else inp[pos+2]
            p3 = pos+3 if m3 == 1 else inp[pos+3]
            if m1 == 2: p1 = inp[pos+1] + relb
            if m2 == 2: p2 = inp[pos+2] + relb
            if m3 == 2: p3 = inp[pos+3] + relb
            if inp[p1] < inp[p2]:
                inp[p3] = 1
            else:
                inp[p3] = 0
            pos+= 4
        elif op == 8:#EQ
            p1 = pos+1 if m1 == 1 else inp[pos+1]
            p2 = pos+2 if m2 == 1 else inp[pos+2]
            p3 = pos+3 if m3 == 1 else inp[pos+3]
            if m1 == 2: p1 = inp[pos+1] + relb
            if m2 == 2: p2 = inp[pos+2] + relb
            if m3 == 2: p3 = inp[pos+3] + relb
            inp[p3] = 1 if inp[p1] == inp[p2] else 0
            pos+= 4
        elif op == 9:#SET RELB
            p1 = pos+1 if m1 == 1 else inp[pos+1]
            if m1 == 2: p1 = inp[pos+1] + relb
            relb+= inp[p1]
            pos+= 2
        elif op == 99:
            print('Halt: %s' % output)
            break
        else:
            print('Bad Instruction: %d' % op)
            break

#Part 1: 2436480432
#Part 2: 45710