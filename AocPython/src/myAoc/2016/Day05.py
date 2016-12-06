'''
Created on Dec 5, 2016

@author: Mark
'''

import hashlib, time
doorId = "cxdnnyjw"

start_time = time.time()
p1 =""
p2 = "????????"
index = 0
while len(p1) < 8 or "?" in p2:
    inp = doorId+ str(index)
    index+= 1
    m = hashlib.md5()
    m.update(inp)
    if m.hexdigest()[0:5] == "00000":
        if len(p1) < 8:
            p1+= m.hexdigest()[5]
            print "Building Password 1:", p1
            if len(p1) == 8:
                elapsed_time = time.time() - start_time
                print "Part 1 completed in", "{:.2f}".format(elapsed_time), "seconds"
                print "PASSWORD 1:", p1
        pos = int(m.hexdigest()[5], 16)
        if "?" in p2:
            if pos >= 0 and pos <= 7:
                c = m.hexdigest()[6]
                if p2[pos] == "?":
                    p2 = p2[:pos] + c + p2[pos + 1:]
                    print "Building Password 2:", p2.rjust(17)
                    if not "?" in p2:
                        elapsed_time = time.time() - start_time
                        print "Part 2 completed in", "{:.2f}".format(elapsed_time), "seconds"
                        print "PASSWORD 2:", p2
