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


#knots = CircularList(range(0, 5))
#lengths = [3, 4, 1, 5]
# lengths = [206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3]
#
# for length in lengths:
#     if length:
#         print(knot)
#         segment = list(reversed(knot[pos:pos+length]))
#         print(length, segment)
#         if len(segment) != length:
#             raise Exception('Mismatched lengths')
#         for i, val in enumerate(segment):
#             knot[i + pos] = val
#
#     pos += length + skipSize
#     skipSize += 1

inString = '206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3'
#inString = '1,2,4'

asciLengths = asciize(inString)
added = [17, 31, 73, 47, 23]
asciLengths += added
numRounds = 64

pos = 0
skipSize = 0
knot = CircularList(range(0, 256))

for i in range(numRounds):
    print(asciLengths)
    for length in asciLengths:
        if length:
            segment = list(reversed(knot[pos:pos + length]))
            if len(segment) != length:
                raise Exception('Mismatched lengths')
            for i, val in enumerate(segment):
                knot[i + pos] = val

        pos += length + skipSize
        skipSize += 1


sparseHash = list(knot)

def densifySlice(start, stop, hashList):
    block = hashList[start:stop]
    out = block[0]
    for item in block[1:]:
        out = out ^ item
    return out

denseHash = []
for i in range(0, 256, 16):
    denseHash.append(densifySlice(i, i+16, sparseHash))

print(sparseHash)
print(denseHash)

outString = ''
for block in denseHash:
    a = hex(block)[2:]
    if len(a) == 1:
        a = '0' + a
    outString += a

print(len(outString), outString)

