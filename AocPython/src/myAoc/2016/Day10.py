'''
Created on Dec 11, 2016

@author: Mark
'''
from collections import defaultdict
import re

part1Done = part2Done = False

def doBot(bots, outputs, bot, low, high, lowToBot, highToBot):
    global part1Done
    global part2Done
    if len(bots[bot]) == 2:
        if lowToBot:
            bots[low].append(min(bots[bot]))
            bots[bot].remove(min(bots[bot]))
        else:
            outputs[low].append(min(bots[bot]))
            bots[bot].remove(min(bots[bot]))
        if highToBot:
            bots[high].append(max(bots[bot]))
            bots[bot].remove(max(bots[bot]))
        else:
            outputs[high].append(max(bots[bot]))
            bots[bot].remove(max(bots[bot]))
        if 61 in bots[low] and 17 in bots[low]:
            print "The bot is", low
            part1Done = True
            if part2Done:
                exit()
        elif 61 in bots[high] and 17 in bots[high]:
            print "The bot is", high
            part1Done = True
            if part2Done:
                exit()
       
        if len(outputs["0"]) == 1 and len(outputs["1"]) == 1 and len(outputs["2"]) == 1:
            print "output product", outputs["0"][0] * outputs["1"][0] * outputs["2"][0]
            part2Done = True
            if part1Done:
                exit()

                    
with open("data/day10") as f:
    bots = defaultdict(list)
    outputs = defaultdict(list)
    values = list()
    for line in f:
        if line.startswith("value"):
            bot, value = re.search("value\s+(\d+)\s+goes to bot\s+(\d+)", line).group(2,1)
            bots[bot].append(int(value))
        elif line.startswith("bot"):
            values.append(line)
            
    while True:
        for s in values:
            s = s.strip()
            bot = low = high = None
            m = re.search("bot\s+(\d+)\s+gives low to bot\s+(\d+)\s+and high to bot\s+(\d+)", s)
            if m:
                bot, low, high = m.group(1, 2, 3)
                doBot(bots, outputs, bot, low, high, True, True)
            else:
                m = re.search("bot\s+(\d+)\s+gives low to output\s+(\d+)\s+and high to bot\s+(\d+)", s)
                if m:
                    bot, low, high = m.group(1, 2, 3)
                    doBot(bots, outputs, bot, low, high, False, True)
                else:
                    m = re.search("bot\s+(\d+)\s+gives low to bot\s+(\d+)\s+and high to output\s+(\d+)", s)
                    if m:
                        bot, low, high = m.group(1, 2, 3)
                        doBot(bots, outputs, bot, low, None, True, False)
