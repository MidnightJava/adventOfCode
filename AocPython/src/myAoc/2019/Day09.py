with open('./2019/data/day09') as f:
    inp = f.readline().split(',')
    input = 1
    pos = 0
    relb = 0

    def check_code_length(pos):
        for i in range(len(inp), pos+1):
            inp.insert(i, '0')

    while get_inp(pos) != 99:
        instr = get_inp(pos)
        op = int(instr[-2]) * 10 + int(instr[-1]) if len(instr) > 1 else int(instr[0])
        m1 = int(instr[-3]) if len(instr) > 2 else 0
        m2 = int(instr[-4]) if len(instr) > 3 else 0
        m3 = int(instr[-5]) if len(instr) > 4 else 0
        if op == 1:
            if m1 == 0:
                check_code_length(int(inp[pos+1]))
                p1 = inp[int(get_inp(pos+1))]
            elif m1 == 1:
                p1 =  get_inp(pos+1)
            elif m1 == 2:
                p1 = str(relb + int(get_inp(pos+1)))
            if m2 == 0:
                p2 = inp[int(get_inp(pos+2))]
            elif m2 == 1:
                p2 =  get_inp(pos+2)
            elif m2 == 2:
                p2 = str(relb + int(get_inp(pos+2)))
            if m3 == 0:
                p3 = int(inp[int(get_inp(pos+3))])
            elif m3 == 2:
                p3 = relb + int(get_inp(pos+3))
            else:
                print('Invalid m3: %d' % m3)
            set_inp(p3, str(int(p1) + int(p2)))
            pos+= 4
        elif op == 2:
            if m1 == 0:
                p1 = inp[int(inp[pos+1])]
            elif m1 == 1:
                p1 =  inp[pos+1]
            elif m1 == 2:
                p1 = str(relb + int(inp[pos+1]))
            if m2 == 0:
                p2 = inp[int(inp[pos+2])]
            elif m2 == 1:
                p2 =  inp[pos+2]
            elif m2 == 2:
                p2 = str(relb + int(inp[pos+2]))
            if m3 == 0:
                check_code_length(int(inp[pos+3]))
                p3 = int(inp[int(inp[pos+3])])
            elif m3 == 2:
                p3 = relb + int(inp[pos+3])
            else:
                print('Invalid m3: %d' % m3)
            check_code_length(p3)
            inp[p3] = str(int(p1) * int(p2))
            pos+= 4
        elif op == 3:
            check_code_length(int(inp[pos+1]))
            if m1 == 0:
                inp[int(inp[pos+1])] = str(input)
            elif m1 == 2:
                check_code_length(relb + int(inp[pos+1]))
                inp[relb + int(inp[pos+1])] = str(input)
            pos+= 2
        elif op == 4:
            if m1 == 0:
                p1 = inp[int(inp[pos+1])]
            elif m1 == 1:
                p1 =  inp[pos+1]
            elif m1 == 2:
                p1 = str(relb + int(inp[pos+1]))
            output = p1
            print('Output: %s, m1: %d' % (output, m1))
            pos+= 2
        elif op == 5:
            if m1 == 0:
                p1 = inp[int(inp[pos+1])]
            elif m1 == 1:
                p1 =  inp[pos+1]
            elif m1 == 2:
                p1 = str(relb + int(inp[pos+1]))
            if m2 == 0:
                p2 = inp[int(inp[pos+2])]
            elif m2 == 1:
                p2 =  inp[pos+2]
            elif m2 == 2:
                p2 = str(relb + int(inp[pos+2]))
            pos = int(p2) if int(p1) else pos+3
        elif op == 6:
            if m1 == 0:
                p1 = inp[int(inp[pos+1])]
            elif m1 == 1:
                p1 =  inp[pos+1]
            elif m1 == 2:
                p1 = str(relb + int(inp[pos+1]))
            if m2 == 0:
                p2 = inp[int(inp[pos+2])]
            elif m2 == 1:
                p2 =  inp[pos+2]
            elif m2 == 2:
                p2 = str(relb + int(inp[pos+2]))
            pos = int(p2) if not int(p1) else pos+3
        elif op == 7:
            if m1 == 0:
                p1 = inp[int(inp[pos+1])]
            elif m1 == 1:
                p1 =  inp[pos+1]
            elif m1 == 2:
                p1 = str(relb + int(inp[pos+1]))
            if m2 == 0:
                p2 = inp[int(inp[pos+2])]
            elif m2 == 1:
                p2 =  inp[pos+2]
            elif m2 == 2:
                p2 = str(relb + int(inp[pos+2]))
            if m3 == 0:
                p3 = int(inp[int(inp[pos+3])])
            elif m3 == 2:
                p3 = relb + int(inp[pos+3])
            else:
                print('Invalid m3: %d' % m3)
            check_code_length(p3)
            if int(p1) < int(p2):
                inp[p3] = "1"
            else:
                inp[p3] = "0"
            pos+= 4
        elif op == 8:
            if m1 == 0:
                p1 = inp[int(inp[pos+1])]
            elif m1 == 1:
                p1 =  inp[pos+1]
            elif m1 == 2:
                p1 = str(relb + int(inp[pos+1]))
            if m2 == 0:
                p2 = inp[int(inp[pos+2])]
            elif m2 == 1:
                p2 =  inp[pos+2]
            elif m2 == 2:
                p2 = str(relb + int(inp[pos+2]))
            if m3 == 0:
                p3 = int(inp[int(inp[pos+3])])
            elif m3 == 2:
                p3 = relb + int(inp[pos+3])
            else:
                print('Invalid m3: %d' % m3)
            check_code_length(p3)
            inp[p3] = "1" if int(p1) == int(p2) else "0"
            pos+= 4
        elif op == 9:
            if m1 == 0:
                p1 = inp[int(inp[pos+1])]
            elif m1 == 1:
                p1 =  inp[pos+1]
            elif m1 == 2:
                p1 = str(relb + int(inp[pos+1]))
            relb+= int(p1)
            pos+= 2
        elif op == 99:
            break
        else:
            print('Bad Instruction: %d' % op)
            break

#Ans > 203