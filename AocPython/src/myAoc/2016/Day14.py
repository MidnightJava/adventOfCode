'''
Created on Dec 15, 2016

@author: Mark
'''
import md5, re

hashes = {}
hashes2 = {}

def doHash(h, n):
    if n == 2016 and h in hashes2:
        return hashes2[h]
    origH = h
    for x in xrange(n):
        md = md5.new()
        md.update(h)
        h = md.hexdigest()
    hashes2[origH] = h
    return h

keys = []
index = 0
salt ="cuanljph"
for part in [(1, 0), (2, 2016)]:
    while len(keys) < 64:
        key = None
        while not key:
            k = None
            ch = None
            while not k:
                if index in hashes:
                    h = hashes[index]
                else:
                    md = md5.new()
                    md.update(salt + str(index))
                    h = md.hexdigest()
                    hashes[index] = h
                m = re.search(r'(.)\1{2,}', doHash(h, part[1])) 
                if m:
                    k = md.hexdigest()
                    ch = m.group(1)
                    break
                else:
                    index+= 1
            for x in xrange(1, 1001):
                if (index + x) in hashes:
                    h = hashes[index + x]
                else:
                    md = md5.new()
                    md.update(salt + str(index + x))
                    h = md.hexdigest()
                    hashes[index+ x] = h
                m = re.search(r"(" + ch + r")\1{4,}", doHash(h, part[1])) 
                if m:
                    key = k
            index+= 1
        print "Found key", key, len(keys)
        keys.append(key)
        
    print "Part", part[0], index - 1
    hashes = hashes2 = {}
    keys = []
    index = 0