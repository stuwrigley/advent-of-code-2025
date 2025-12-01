#!/usr/bin/python3
import time

start_time = time.time()

DAY = '01'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

# part 1
pointer = 50
zeroStops = 0
zeroPositions = 0
for line in lines:
    rotationAmount = int(line[1:])

    zeroPositions += rotationAmount // 100
    rotationAmount = rotationAmount % 100

    if line[0] == 'L':
        rotationAmount = int(rotationAmount * -1)

    if (pointer + rotationAmount <= 0 < pointer) or (pointer + rotationAmount >= 100):
        zeroPositions += 1

    pointer = (pointer + rotationAmount) % 100
    zeroStops += pointer == 0

print("Part 1 answer:", zeroStops)
print("Part 2 answer:", zeroPositions)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
