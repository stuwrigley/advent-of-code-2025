#!/usr/bin/python3
import time
import shapely
from shapely.geometry.polygon import Polygon

start_time = time.time()

DAY = '09'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    corners = [tuple([int(x) for x in line.rstrip().split(',')]) for line in f]


def area(corner1, corner2):
    return (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)


# part 1
largestArea = 0
for corner1ID in range(len(corners)):
    for corner2ID in range(corner1ID + 1, len(corners)):
        currentArea = area(corners[corner1ID], corners[corner2ID])
        if currentArea > largestArea:
            largestArea = currentArea
print("Part 1 answer:", largestArea)

# part 2
polygon = Polygon(corners)
largestArea = 0
for corner1ID in range(len(corners)):
    for corner2ID in range(corner1ID + 1, len(corners)):

        smallestX = min(corners[corner1ID][0], corners[corner2ID][0])
        largestX = max(corners[corner1ID][0], corners[corner2ID][0])
        smallestY = min(corners[corner1ID][1], corners[corner2ID][1])
        largestY = max(corners[corner1ID][1], corners[corner2ID][1])

        currentRect = shapely.box(smallestX, smallestY, largestX, largestY)
        if polygon.covers(currentRect):
            currentArea = area(corners[corner1ID], corners[corner2ID])
            if currentArea > largestArea:
                largestArea = currentArea
print("Part 2 answer:", largestArea)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
