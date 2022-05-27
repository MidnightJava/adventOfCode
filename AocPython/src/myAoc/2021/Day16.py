
vsum = 0

def process(bits, pkts):
    global vsum
    # while len(bits) and pkts >= 1:
    vbits = bits[:3]
    tbits = bits[3:6]
    ver= int(vbits, 2)
    print(f"Version {ver}")
    vsum+= ver
    t = int(tbits, 2)
    bits = bits[6:]
    if t == 4:
        done = False
        sum = ''
        while not done:
            gbits= bits[:5]
            bits = bits[5:]
            sum+= gbits[1:]
            if gbits[0] == '0':
                done = True
                bits = bits[5:]
                # while len(bits) % 4 != 0:
                #     bits = bits[:-1]
                # print(f"SUM {int(sum,2)}")
        # pkts-= 1
    else:
        ibit = bits[0]
        bits = bits[1:]
        if ibit == '0':
            lbits = bits[:15]
            bits = bits[15:]
            l = int(lbits, 2)
            process(bits[::], 1)
            pkts-= 1
        elif ibit == '1':
            lbits = bits[:11]
            bits = bits[11:]
            l = int(lbits, 2)
            process(bits[::], l)
            pkts-= 1
        else:
            print("Invalid packet length type ID")

    while len(bits) % 8 != 0:
        bits = bits[:-1]

    # print(bits)

for line in open('2021/data/day16b').readlines():
    vsum = 0
    msg = line.strip()
    bits =  bin(int(msg,16))[2:] #strip off leading '0b'
    while len(bits) % 4 != 0:
        bits = '0' + bits
    print(f"Initial bits: {bits}")
    process(bits[::], 1)

    print('Part 1: %d' % vsum)


