'''
Created on Dec 16, 2016

@author: Mark
'''
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

print lcmm(*[1,5])
print lcmm(*[7,13,3,5,17,19,11,6,11,4,12])