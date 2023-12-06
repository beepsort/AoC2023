lines= ""

with open('1.txt') as f:
    lines = f.readlines()

def onlydigits(line):
    return list(filter(str.isdigit, line))

def sumfirstlast(linedigits):
    return int(linedigits[0] + linedigits[-1])

linedigits = map(onlydigits, lines)
linedigits = list(filter(None, linedigits))
linesums = list(map(sumfirstlast, linedigits))
total = sum(linesums)
print(total)
