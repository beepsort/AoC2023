from functools import reduce

lines = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()
#lines= ""
#
with open('1.txt') as f:
    lines = f.readlines()
#print(lines)

numwords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def findFirstNum(line):
    def findNum(num):
        return line.find(num)
    return list(map(findNum, numwords))

def findLastNum(line):
    def findNum(num):
        return line.rfind(num)
    return list(map(findNum, numwords))

def replaceLowest(line):
    firsts = findFirstNum(line)
    numsAndPos = [[pos,num] for pos,num in zip(range(1,10),firsts)]
    def dropNegative(numAndPos):
        return numAndPos[1]>=0
    numsAndPos = list(filter(dropNegative, numsAndPos))
    def reduceMinPred(a, b):
        return a if a[1] < b[1] else b
    if len(numsAndPos) > 0:
        lowest = reduce(reduceMinPred, numsAndPos)
        index = lowest[1]
        digit = lowest[0]
        line = line[:index] + str(digit) + line[index+1:]
    return line

def replaceHighest(line):
    lasts = findLastNum(line)
    numsAndPos = [[pos,num] for pos,num in zip(range(1,10),lasts)]
    def dropNegative(numAndPos):
        return numAndPos[1]>=0
    numsAndPos = list(filter(dropNegative, numsAndPos))
    def reduceMaxPred(a, b):
        return a if a[1] > b[1] else b
    if len(numsAndPos) > 0:
        highest = reduce(reduceMaxPred, numsAndPos)
        index = highest[1]
        digit = highest[0]
        line = line[:index] + str(digit) + line[index+1:]
    return line

def onlydigits(line):
    return list(filter(str.isdigit, line))

def sumfirstlast(linedigits):
    return int(linedigits[0] + linedigits[-1])

lines = list(map(str.lower, lines))
#print("lower:" + str(lines))
lines = list(map(replaceLowest, lines))
#print("lowest replaced:" + str(lines))
lines = list(map(replaceHighest, lines))
#print("highest replaced:" + str(lines))
linedigits = map(onlydigits, lines)
#print(linedigits)
linedigits = list(filter(None, linedigits))
#print(linedigits)
linesums = list(map(sumfirstlast, linedigits))
#print(linesums)
total = sum(linesums)
print(total)
