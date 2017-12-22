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
                return super(CircularList, self).__getitem__(slice(start, len(self))) + super(CircularList,
                                                                                              self).__getitem__(
                    slice(0, stop))
            else:
                print(start, stop)

            # otherwise, slice it normally
            return super(CircularList, self).__getitem__(slice(start, stop))

        return super(CircularList, self).__getitem__(index)

    def __setitem__(self, key, value):
        super(CircularList, self).__setitem__(key % len(self), value)


def buildSpinlock(reps):
    spinlock = CircularList([0])
    stepsPerInsert = 343
    spinSteps = reps
    index = 0

    for i in range(1, spinSteps + 1):
        index += stepsPerInsert
        index = (index % len(spinlock)) + 1
        spinlock.insert(index, i)
        index = spinlock.index(i)

    return spinlock

import time

start = time.time()

# TODO this will take about 20 minutes
#spinlock = buildSpinlock(50000000)

from collections import deque

puzzle = 343
spinlock = deque([0])

for i in range(1,50000001):
    spinlock.rotate(-puzzle)
    spinlock.append(i)

end = time.time()

print(end - start)
print(spinlock[spinlock.index(0) + 1])
