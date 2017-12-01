def intifyString(inString):
    return [int(i) for i in inString]

def getHalfway(i, listLength):
    half = int(listLength / 2)
    halfAway = i + half
    if halfAway >= listLength:
        halfAway -= listLength

    return halfAway


def getValueOfStringHalfway(inString):
    val = 0
    intArray = intifyString(inString)
    for i, currentInt in enumerate(intArray):
        j = getHalfway(i, len(intArray))
        if currentInt == intArray[j]:
            val += currentInt

    return val


def getValueOfStringNext(inString):
    val = 0
    intArray = intifyString(inString)
    for i, currentInt in enumerate(intArray):
        if i == len(intArray) - 1:
            i = 0
        else:
            i += 1

        if currentInt == intArray[i]:
            val += currentInt

    return val


def main():
    print(getValueOfStringHalfway('1212'))

if __name__ == '__main__':
    main()
