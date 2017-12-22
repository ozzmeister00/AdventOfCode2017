NORTH, S, W, E = (0, 1), (0, -1), (-1, 0), (1, 0)
turnLeft = {NORTH: W, W: S, S: E, E: NORTH}
ADJACENT = []
for x in range(-1, 2):
    for y in range(-1, 2):
        ADJACENT.append((x,y))

def spiralTo(value):
    dx, dy = S
    x, y = 0, 0
    matrix = {(0,0):1}
    count = 1
    while count < value:
        count += 1
        matrix[(x, y)] = count
        newDX, newDY = turnLeft[(dx, dy)]
        newX = x + newDX
        newY = y + newDY
        if (newX, newY) not in matrix:
            x, y = newX, newY
            dx, dy = newDX, newDY
        else:
            x, y = x + dx, y + dy


        print(x,y, count)

    print(x, y)
    return (abs(x) + abs(y))

def sumAdjacents(x, y, matrix):
    sum = 0
    for dx, dy in ADJACENT:
        if (dx + x, dy + y) in matrix:
            sum += matrix[(dx + x, dy + y)]

    return sum

def spiralSquare(value):
    dx, dy = S
    x, y = 0, 0
    matrix = {(0,0):1}
    count = 0
    while count < value + 1:
        newDX, newDY = turnLeft[(dx, dy)]
        newX = x + newDX
        newY = y + newDY
        if (newX, newY) not in matrix:
            x, y = newX, newY
            dx, dy = newDX, newDY
        else:
            x, y = x + dx, y + dy

        matrix[(x, y)] = sumAdjacents(x, y, matrix)
        count = matrix[(x, y)]
        print(x,y, count)
        if count > value:
            print(count)
            return


spiralSquare(325489)
