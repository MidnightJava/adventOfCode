'''
Created on Dec 20, 2015

@author: Mark
'''
import math
import itertools
from collections import defaultdict
import timeit

# def primeFactors(n):
#     primes = set()
#     for i in xrange(2, n):
#         if n % i == 0:
#             primes.add(i)
#             primes = primes | primeFactors(i)
#     primes.add(1)
#     primes.add(n)
#     return primes
# 
# def func(n, i):
#     return reduce(lambda x,y: x +y if math.sqrt(y) % math.sqrt(y) != 0 else x + 2*y, primeFactors(i)) * 10
# 
# def func2(n):
#     m = int(n/2)
#     x = func(n, m)
#     while x != n:
#         if x > n:
#             m = m + int((x-n)/2)
#         else:
#             m = m - int((n-x)/2)
#         x = func(n, m)
#         print x
#     return m
    
# def func(n):
#     i = 400000
#     x = 0
#     primes = []
#     while x < n:
#         primes = primeFactors(i)
#         x = reduce(lambda x,y: x +y if math.sqrt(y) % math.sqrt(y) != 0 else x + 2*y, primes) * 10
#         i += 1
#     return i-1

def primesInRange(m, n, part2):
#     print "get primes in range",m,n-1
    mult = 11 if part2 else 10
    a = dict([(i,mult) for i in xrange(1, n+1)])
    sortyByFreqThenAlpha = m
    while sortyByFreqThenAlpha <= n:
        j = sortyByFreqThenAlpha
        while j <= n:
            if part2 and j >= sortyByFreqThenAlpha + 50*sortyByFreqThenAlpha:
                break
            a[j] += sortyByFreqThenAlpha*mult
            j += sortyByFreqThenAlpha
        sortyByFreqThenAlpha += 1
    return a.itervalues()

def presents(n, part2):
    idSum = 0
    start = 2
    sieve = 1000000
    x = 0
    while idSum <= n:
        primes = primesInRange(start, start + sieve, part2)
        for sortyByFreqThenAlpha in primes:
            x += 1
            if sortyByFreqThenAlpha >= n:
                return x
        return "solution not found", sortyByFreqThenAlpha,x

start = timeit.default_timer()
print "Sieve method part 1:", presents(33100000, False)
stop = timeit.default_timer()
print "Time:", stop - start

start = timeit.default_timer()
print "Sieve method part 2", presents(33100000, True)
stop = timeit.default_timer()
print "Time:", stop - start


target = 33100000

#Brute force methods Copied firm reddit user khenti-amentiu, with slight mods

def part1(upperBound):
    houses = defaultdict(int)

    for elf in xrange(1, target):
        for house in xrange(elf, upperBound, elf):
            houses[house] += elf*10

            if houses[elf] >= target:
                return elf

def part2(upperbound):
    houses = defaultdict(int)

    for elf in xrange(1, target):
        for house in xrange(elf, min(upperbound, elf + elf*50), elf):
            houses[house] += elf*11

            if houses[elf] >= target:
                return elf

start = timeit.default_timer()
print "Brute force, part 1:", part1(1000000)
stop = timeit.default_timer()
print "Time:", stop - start

start = timeit.default_timer()
print "Brute force, part 1:", part2(1000000)
stop = timeit.default_timer()
print "Time:", stop - start
