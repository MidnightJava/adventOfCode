
vsum = 0

def process(bits):
    if len(bits) <= 11: return
    global vsum
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
            gbits = bits[:5]
            bits = bits[5:]
            sum+= gbits[1:]
            if gbits[0] == '0':
                done = True
                if len(bits):
                    process(bits[::])
                # while len(bits) % 4 != 0:
                #     bits = bits[:-1]
                
        return int(sum,2)
    else:
        ibit = bits[0]
        bits = bits[1:]
        if ibit == '0':
            lbits = bits[:15]
            bits = bits[15:]
            l = int(lbits, 2)
            process(bits[::])
        elif ibit == '1':
            lbits = bits[:11]
            bits = bits[11:]
            l = int(lbits, 2)
            process(bits[::])
        else:
            print("Invalid packet length type ID")

    # while len(bits) % 8 != 0:
    #     bits = bits[:-1]

for line in open('2021/data/day16').readlines():
    vsum = 0
    msg = line.strip()
    bits =  bin(int(msg,16))[2:] #strip off leading '0b'
    while len(bits) % 4 != 0:
        bits = '0' + bits
    print(f"Initial bits: {bits}")
    process(bits[::])

    print('Part 1: %d' % vsum)

# Part 1: 979
