puzzleInput = '''0: 5
1: 2
2: 3
4: 4
6: 6
8: 4
10: 8
12: 6
14: 6
16: 8
18: 6
20: 9
22: 8
24: 10
26: 8
28: 8
30: 12
32: 8
34: 12
36: 10
38: 12
40: 12
42: 12
44: 12
46: 12
48: 14
50: 12
52: 14
54: 12
56: 14
58: 12
60: 14
62: 14
64: 14
66: 14
68: 14
70: 14
72: 14
76: 14
80: 18
84: 14
90: 18
92: 17'''

testInput = '''0: 3
1: 2
4: 4
6: 4'''


# { Layer : [CurrPos, [depthChart], maxValue }

def reverseIndex(inVal, maxVal):
    return inVal if inVal < maxVal else maxVal * 2 - inVal

def buildDepthChart(inVal):
    return list(range(0, inVal)) + list(range(inVal - 2, 0, -1))

def buildFirewalls(inString):
    out = {}
    for line in inString.split('\n'):
        tokens = line.split(': ')
        layer = int(tokens[0])
        depth = int(tokens[1])
        depthChart = buildDepthChart(depth)
        #out[layer] = [0, depthChart, len(depthChart), depth]
        out[layer] = depth

    return out


def moveScanners(scanners, currTime):
    for scanner in scanners:
        scanners[scanner][0] = scanners[scanner][1][currTime % scanners[scanner][2]]

    return scanners


def wasCaught(scanners, packet, currTime):
    if packet in scanners:
        scanDepth = scanners[packet]
        scanDepth = (scanDepth - 2) + scanDepth
        if currTime % scanDepth == 0:
            return packet

    return -1

def scannerAtPacket(depth, currTime):
    scanDepth =  (depth - 2) + depth
    if currTime % scanDepth == 0:
        return True

    return False



scanners = buildFirewalls(puzzleInput)
maxPos = max(scanners.keys())
endSeverity = 1
delay = 0

# while endSeverity:
#     severity = 0
#     delay += 1
#     currPos = -1
#     currTime = 0
#
#     while currPos < maxPos:
#
#         if currTime >= delay:
#             #print('time = ', currTime, ' and delay = ', delay)
#             currPos += 1
#
#         #print(currTime, currPos, scanners)
#
#         scanner = wasCaught(scanners, currPos, currTime)
#         if scanner > -1:
#             #print(delay, scanner, currTime)
#             severity += (currPos * scanners[scanner]) + 1
#             break
#
#         currTime += 1
#
#     endSeverity = severity

delay = 0
caught = True
while caught:
    for scanner in scanners:
        caught = scannerAtPacket(scanners[scanner], delay + scanner)
        if caught:
            break

    delay += 1

print(delay - 1)


