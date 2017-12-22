class Generator(object):
    def __init__(self, startingValue, factor):
        self.factor = factor
        self.previousValue = startingValue
        self.divisor = 2147483647

    def getNewValue(self):
        newValue = (self.previousValue * self.factor) % self.divisor
        self.previousValue = newValue
        return newValue

def leftJustify(inStr, padChar='0', num=16):
    inStr = inStr[2:]
    while len(inStr) < num:
        inStr = padChar + inStr
    return inStr

def binarize(inVal):
    #return leftJustify(bin(inVal[2:]))
    return bin(inVal)[2:].zfill(16)

def binComp(a, b):
    return a[-16:] == b[-16:]

def newValue(factor, currValue):
    return (currValue * factor) % 2147483647

iterations = 10000

genA = Generator(65, 16807)
genB = Generator(8921, 48271)

a = newValue(16807, 699)
b = newValue(48271, 124)

#a = newValue(16807, 65)
#b = newValue(48271, 8921)

judge = 0

import time

start = time.time()

values = {'a':[],
          'b':[]}

checkedIndex = 0

def indeciesToCheck(currIndex, valuesA, valuesB):
    return len(valuesA) > currIndex and len(valuesB) > currIndex

#for i in range(iterations):
while checkedIndex < 5000000:
    a = newValue(16807, a)
    b = newValue(48271, b)

    if a % 4 == 0:
        values['a'].append(a)
    if b % 8 == 0:
        values['b'].append(b)

    while indeciesToCheck(checkedIndex, values['a'], values['b']):
        #print('checking index ', checkedIndex)
        if binComp(binarize(values['a'][checkedIndex]), binarize(values['b'][checkedIndex])):
            judge += 1
        checkedIndex += 1

end = time.time()

print(judge)
print(end - start)
