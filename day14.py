# hash inputs are a key string, a dash, and a number from 0 to 127 corresponding to the row

# flqrgnkx-0

# each row is tracked by a 128 bit-long knot hash (32 hex digits)
# each hexidecimal bit to its binary value (high bit first)



class CircularList(list):
    def __init__(self, *args):
        super(CircularList, self).__init__(*args)

    def __getitem__(self, index):
        if isinstance(index, int):
            index = index % len(self)
        elif isinstance(index, slice):
            # make sure these wrap around correctly
            start = index.start % len(self)
            stop = index.stop % len(self)

            # if they cross over the end of the list, keep going
            if stop <= start:
                return super(CircularList, self).__getitem__(slice(start, len(self))) + super(CircularList, self).__getitem__(slice(0, stop))

            # otherwise, slice it normally
            return super(CircularList, self).__getitem__(slice(start, stop))

        return super(CircularList, self).__getitem__(index)

    def __setitem__(self, key, value):
        super(CircularList, self).__setitem__(key % len(self), value)

def asciize(inStr):
    return [ord(i) for i in inStr]

def leftJustify(inStr, padChar='0', num=4):
    while len(inStr) < num:
        inStr = padChar + inStr
    return inStr

def binarize(inKey):
    outBits = ''
    for i in inKey:
        outBits += leftJustify(bin(int(i, 16))[2:])

    return outBits

def rowKey(inKey, i):
    return '{}-{}'.format(inKey, i)


def generateSparseHash(inKey):
    numRounds = 64
    pos = 0
    skipSize = 0
    knot = CircularList(range(0, 256))

    for i in range(numRounds):
        for length in inKey:
            if length:
                segment = list(reversed(knot[pos:pos + length]))
                if len(segment) != length:
                    raise Exception('Mismatched lengths')
                for i, val in enumerate(segment):
                    knot[i + pos] = val

            pos += length + skipSize
            skipSize += 1

    sparseHash = list(knot)

    return sparseHash

def densifySlice(start, stop, hashList):
    block = hashList[start:stop]
    out = block[0]
    for item in block[1:]:
        out = out ^ item
    return out

def generateDenseHash(sparseHash):
    denseHash = []
    for i in range(0, 256, 16):
        denseHash.append(densifySlice(i, i+16, sparseHash))
    return denseHash

def generateKnotHash(inKey):
    asciLengths = asciize(inKey)
    numRounds = 64
    added = [17, 31, 73, 47, 23]
    asciLengths += added

    sparse = generateSparseHash(asciLengths)
    dense = generateDenseHash(sparse)

    outString = ''
    for block in dense:
        a = hex(block)[2:]
        if len(a) == 1:
            a = '0' + a
        outString += a

    return outString

#key = 'flqrgnkx'
key = 'nbysizxe'

def generateBitsFromHash(key):
    outBits = []

    for i in range(0, 128):
        knotHash = generateKnotHash(rowKey(key, i))
        print(knotHash)
        outBits.append(binarize(knotHash))

    bitString = ''.join(outBits)
    print(bitString.count('1'))

    return outBits

def buildRegion(startX, startY, gridMap, regionedBits, region=[]):
    neighbors = [(0, 1),
                 (0, -1),
                 (1, 0),
                 (-1, 0)
                 ]

    region.append((startX, startY))
    for nX, nY in neighbors:
        seekX = startX + nX
        seekY = startY + nY
        if seekX > -1 and seekX < len(gridMap[0]) and seekY > -1 and seekY < len(gridMap):
            if (seekX, seekY) not in region and (seekX, seekY) not in regionedBits:
                if gridMap[seekX][seekY] == '1':
                    region = buildRegion(seekX, seekY, gridMap, regionedBits, region=region)

    return region

def getCountOfRegions(bitLists):

    regionCount = 0
    regionedBits = []
    regions = []

    for x in range(0, len(bitLists[0])):
        for y in range(0, len(bitLists)):
            if (x, y) not in regionedBits and bitLists[x][y] == '1':
                regionCount += 1
                newRegion = buildRegion(x, y, bitLists, regionedBits, region=[])
                regionedBits += newRegion
                regions.append(newRegion)

    print(regionCount)

outBits = generateBitsFromHash(key)

getCountOfRegions(outBits)
