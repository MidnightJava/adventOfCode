'''
Created on Dec 18, 2015

@author: Mark
'''
from _collections import defaultdict
import re

_map = defaultdict(set)
res = set()
with open("replacements.txt") as f:
    for line in f:
        k, v = (line.split(r"=>"))
        _map[k.strip()].add(v.strip())

inp = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"

for k,s in _map.items():
    for v in s:
        for m in re.finditer(k,inp):
            res.add(inp[0:m.start()] + v + inp[m.end()::])
             
print len(res)

with open('replacements.txt', 'r') as myfile:
    input=myfile.read()
molecule = inp[::-1]
reps = {m[1][::-1]: m[0][::-1] 
        for m in re.findall(r'(\w+) => (\w+)', input)}
def rep(x):
    return reps[x.group()]

idSum = 0
while molecule != 'e':
    molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
    idSum += 1

print(idSum)