def process(bits, num_p, num_b):
    vbits = bits[:3]
    tbits = bits[3:6]
    bits = bits[6:]
    ver = int(vbits, 2)
    t = int(tbits, 2)
    if num_p is not None:
        while num_p >= 1:
            if t == 4:
                done = False
                while not done:
                    gbits= bits[:5]
                    bits = bits[5:]
                    if gbits[0] == '0':
                        done = True
            else:
                ibit = bits[0]
                bits = bits[1:]
                if ibit == '0':
                    lbits = bits[:15]
                    bits = bits[15:]
                    l = int(lbits, 2)
                    ver+= process(bits, None, l)
                elif ibit == '1':
                    lbits = bits[:11]
                    bits = bits[11:]
                    l = int(lbits, 2)
                    ver+= process(bits, l, None)
                else:
                    print("Invalid packet length type ID")
            num_p-= 1
    else:
        while num_b >= 1:
            if t == 4:
                done = False
                while not done:
                    gbits= bits[:5]
                    if gbits[0] == '0': done = True
                    bits = bits[5:]
                    num_b-= 5
                    if done and num_b  > 0:
                        while num_b > 0:
                            num_b-= 1
                            bits = bits[:-1]
            else:
                ibit = bits[0]
                bits = bits[1:]
                num_b-= 1
                if ibit == '0':
                    lbits = bits[:15]
                    bits = bits[15:]
                    num_b-= 15
                    l = int(lbits, 2)
                    ver+= process(bits, None, l)
                elif ibit == '1':
                    lbits = bits[:11]
                    bits = bits[11:]
                    num_b-= 11
                    l = int(lbits, 2)
                    ver+= process(bits, l, None)
                else:
                    print("Invalid packet length type ID")
    return ver

for line in open('2021/data/day16a').readlines():
    msg = line.strip()
    bits =  bin(int(msg,16))[2:] #strip off leading '0b'
    while len(bits) % 4 != 0:
        bits = '0' + bits
    vsum = process(bits[::], 1, None)

    print('Part 1: %d' % vsum)


