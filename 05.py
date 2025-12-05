#!/usr/bin/python3
import time

start_time = time.time()

DAY = '05'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

ranges = []
rangeLimits = set()
ingredients = []

for line in lines:
    if '-' in line:
        limits = line.split('-')
        ranges.append(range(int(limits[0]), int(limits[1]) + 1))
        rangeLimits.add((int(limits[0]), int(limits[1])))
    elif line == '':
        continue
    else:
        ingredients.append(int(line))

# part 1
numFresh = 0
for ingredient in ingredients:
    for freshRange in ranges:
        if ingredient in freshRange:
            numFresh += 1
            break
print("Part 1 answer:", numFresh)


# part 2
numFresh = 0
rangesMergedLastTime = True
while rangesMergedLastTime:
    rangesMergedLastTime = False
    newRangeLimits = rangeLimits.copy()
    for r1 in rangeLimits:
        if rangesMergedLastTime:
            break
        for r2 in rangeLimits:
            if r1 != r2:
                if r2[0] <= r1[0] <= r2[1] or r2[0] <= r1[1] <= r2[1]:
                    newRange = (min(r1[0], r2[0]), max(r1[1], r2[1]))
                    newRangeLimits.remove(r1)
                    newRangeLimits.remove(r2)
                    newRangeLimits.add(newRange)
                    rangesMergedLastTime = True
                    break
    rangeLimits = newRangeLimits.copy()
for r in rangeLimits:
    numFresh += r[1] - r[0] + 1
print("Part 2 answer:", numFresh)


elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
