'''
Created on Dec 8, 2016

@author: maleone
'''

from __future__ import print_function
import copy

def updateRect(screen, w, h):
    for y in xrange(int(h)):
        for x in xrange(int(w)):
            screen[y][x] = True
            
def rotate(screen, eq, shift):
    screenCopy = copy.deepcopy(screen)
    dim = (eq.split("=")[0], eq.split("=")[1])
    if dim[0] == "y":
        for x in xrange(50):
            screenCopy[int(dim[1])][(x + int(shift)) % 50] = screen[int(dim[1])][x]
    if dim[0] == "x":
        for y in xrange(6):
            screenCopy[(y + int(shift)) % 6][int(dim[1])] = screen[y][int(dim[1])]
    return screenCopy
    
def countPixels(screen):
    count = 0
    for y in xrange(6):
        for x in xrange(50):
            if screen[y][x]:
                count+= 1
    return count

def displayCode(screen):
    for y in xrange(6):
        for x in xrange(50):
            pixel = "X" if screen[y][x] else " "
            print(pixel, end="")
            if (x+ 1) % 5 == 0:
                print("  ", end = "")
        print()

with open("data/day08") as f:
    screen = []
    for y in xrange(6):
        row = []
        for x in xrange(50):
            row.append(False)
        screen.append(row)
    for line in f:
        words = line.strip().split()
        if len(words) == 2:
            updateRect(screen, *words[1].split("x"))
        elif len(words) == 5:
            screen = rotate(screen, words[2], words[4])
        else:
            print("error")
    print ("Pixel Count:", countPixels(screen), end ="\n\n")
    displayCode(screen)
        
#>100 < 195