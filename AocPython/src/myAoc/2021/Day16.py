def process(bits):
    vbits = bits[:3]
    tbits = bits[3:6]
    bits = bits[6:]
    ver = int(vbits, 2)
    t = int(tbits, 2)
    if t == 4:
        done = False
        while not done:
            gbits= bits[:5]
            bits = bits[5:]
            if gbits[0] == '0': done = True
    else:
        ibit = bits[:1]
        bits = bits[1:]
        if int(ibit, 2) == 0:
            lbits = bits[:15]
            bits = bits[15:]
            l = int(lbits, 2)
            bits =bits[:l]
            ver+= process(bits)
        elif int(ibit, 2) == 1:
            lbits = bits[:11]
            bits = bits[11:]
            l = int(lbits, 2)
            ver+= process(bits)
        else:
            print("Invalid packet length")
    if len(bits):
        ver+= process(bits)
    return ver

for line in open('2021/data/day16a').readlines():
    msg = line.strip()
    bits =  bin(int(msg,16))[2:]
    vsum = process(bits)

    print('Part 1: %d' % vsum)


