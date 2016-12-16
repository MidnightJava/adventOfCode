'''
Created on Dec 15, 2016

@author: Mark
'''
import md5, re

def doHash(h, n):
    for x in xrange(n):
        md = md5.new()
        md.update(h)
        h = md.hexdigest()
    return h

keys = []
index = 0
salt ="cuanljph"
while len(keys) < 64:
    key = None
    while not key:
        k = None
        ch = None
        while not k:
            md = md5.new()
            md.update(salt + str(index))
            h = md.hexdigest()
            m = re.search(r'(.)\1{2,}', doHash(h, 2016)) 
            if m:
                k = md.hexdigest()
                ch = m.group(1)
                break
            else:
                index+= 1
        for x in xrange(1, 1001):
            md = md5.new()
            md.update(salt + str(index + x))
            h = md.hexdigest()
            m = re.search(r"(" + ch + r")\1{4,}", doHash(h, 2016)) 
            if m:
                key = k
        index+= 1
    print "Found key", key, len(keys)
    keys.append(key)
    
print index - 1