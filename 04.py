#!/usr/bin/python3
import time
from functools import total_ordering

start_time = time.time()

DAY = '04'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

map = []
for line in lines:
    map.append([x for x in line])


def surroundingRolls(map, yPos, xPos):
    numRolls = 0
    for xOffset in [-1, 0, 1]:
        for yOffset in [-1, 0, 1]:
            if not (xOffset == 0 and yOffset == 0):
                searchY = yPos + yOffset
                searchX = xPos + xOffset
                if searchX < 0 or searchY < 0 or searchX >= len(map[0]) or searchY >= len(map):
                    continue
                numRolls += map[searchY][searchX] == '@'
    return numRolls


# part 1
accessibleRolls = set()
for yPos in range(len(lines)):
    for xPos in range(len(lines[0])):
        if map[yPos][xPos] == '@' and surroundingRolls(map, yPos, xPos) < 4:
            accessibleRolls.add((yPos, xPos))
print("Part 1 answer:", len(accessibleRolls))

# part 2
totalRollsRemoved = len(accessibleRolls)
while len(accessibleRolls) > 0:
    for loc in accessibleRolls:
        map[loc[0]][loc[1]] = '.'
    accessibleRolls = set()
    for yPos in range(len(lines)):
        for xPos in range(len(lines[0])):
            if map[yPos][xPos] == '@' and surroundingRolls(map, yPos, xPos) < 4:
                totalRollsRemoved += 1
                accessibleRolls.add((yPos, xPos))
print("Part 2 answer:", totalRollsRemoved)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
