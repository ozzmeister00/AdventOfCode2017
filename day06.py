banksInput = '''11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11'''

numMemoryBanks = 16
memoryBank = [int(i) for i in banksInput.split('\t')]

#memoryBank = [0, 2, 7, 0]

states = [list(memoryBank)]

cycles = 0

def stateExisted(memBank, states):
    if memoryBank in states[:-1]:
        return True

    return False

while not stateExisted(memoryBank, states):
    mostBlocks = max(memoryBank)
    index = memoryBank.index(mostBlocks)
    memoryBank[index] = 0
    distributionIndex = (index + 1) % numMemoryBanks
    while mostBlocks:
        memoryBank[distributionIndex] += 1
        # wrap around indexing
        distributionIndex = (distributionIndex + 1) % numMemoryBanks
        mostBlocks -= 1

    cycles += 1

    states.append(list(memoryBank))

print(cycles)

# get distance between same states
index = states.index(memoryBank)
print(cycles - index)
