'''
Created on Dec 12, 2015

'''
import json

def day12(ignoreRed):
    def sum_numbers(obj):
        if type(obj) == type(dict()):
            if ignoreRed and "red" in obj.values():
                return 0
            return sum(_map(sum_numbers, obj.values()))

        if type(obj) == type(list()):
            return sum(_map(sum_numbers, obj))

        if type(obj) == type(0):
            return obj

        return 0

    data = json.loads(open('json.txt', 'r').read())
    return sum_numbers(data)

print "All:", day12(False)
print "Ignore red:", day12(True)