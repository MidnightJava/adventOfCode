from functools import reduce
vsum = 0

ops = []
vals = []
value = 0

class Packet:
    def __init__(self):
        self.parent = None
        self.type = None
        self.version = 0
        self.value = 0
        self.op = None
        self.subpackets = []
        self.blength = None
        self.pcount = None

def calc_value(op, vals):
    global value
    if op == 0:
        value+= sum(vals)
    elif op == 1:
        value+= reduce(lambda v,a: v*a, vals)
    elif op == 2:
        value+= min(vals)
    elif op == 3:
        value+= max(vals)
    elif op == 5:
        value = value + 1 if vals[0] > vals[1] else 0
    elif op == 6:
        value = value + 1 if vals[0] < vals[1] else 0
    elif op == 7:
        value = value + 1 if vals[0] == vals[1] else 0

def process(bits, pkt, blen, pcnt):
    # while (blen is None or blen > 0) and (pcnt is None or pcnt > 0):
        global vsum
        # print(vsum)
        child = Packet()
        child.parent = pkt
        pkt.subpackets.append(child)
        global vals
        if len(bits) <= 11: return
        vbits = bits[:3]
        tbits = bits[3:6]
        ver= int(vbits, 2)
        pkt.version = ver
        # print(f"Version {ver}")
        vsum+= ver
        t = int(tbits, 2)
        child.type = t
        bits = bits[6:]
        if blen is not None: blen-= 6
        if t == 4:
            # print('TYPE 4')
            done = False
            sum = ''
            while not done:
                gbits = bits[:5]
                bits = bits[5:]
                if blen is not None: blen-= 5
                sum+= gbits[1:]
                if gbits[0] == '0':
                    done = True
                    
            child.value = int(sum,2)

        else:
            child_blen = None
            child_pcnt = None
            # print(f"\tType {t}")
            ibit = bits[0]
            bits = bits[1:]
            if blen is not None: blen-= 1
            if ibit == '0':
                lbits = bits[:15]
                bits = bits[15:]
                if blen is not None: blen-= 15
                child_blen = int(lbits, 2)
            elif ibit == '1':
                lbits = bits[:11]
                bits = bits[11:]
                if blen is not None: blen-= 11
                child_pcnt = int(lbits, 2)
        
        if pcnt is not None: pcnt-= 1
        if (len(bits)):
            process(bits[::], child, blen, pcnt)
        

        
        

for line in open('2021/data/day16').readlines():
    vsum = 0
    msg = line.strip()
    bits =  bin(int(msg,16))[2:] #strip off leading '0b'
    while len(bits) % 4 != 0:
        bits = '0' + bits
    print(f"Initial bits: {bits}")
    root = Packet()
    process(bits[::], root, None, 1)

    print('Part 1: %d' % vsum)

    print(f"Part 2: {value}")

    nodes = [root]
    while len(nodes):
        node = nodes.pop()
        # if node.type != 4: print(f"Found node type {node.type}")
        if len(node.subpackets) > 1: print(f"Found node with {len(node.subpackets)} subpackets")
        for n in node.subpackets:
            nodes.insert(0, n)

# Part 1: 979
