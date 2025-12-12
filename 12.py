#!/usr/bin/python3
import math
import time

start_time = time.time()

DAY = '12'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

presentSizes = []
regions = []
count = 0
for line in lines:
    if line == "":
        presentSizes.append(count)
        continue
    if line[1] == ":":  # this is a shape section
        count = 0
        continue
    if "x" in line:  # this is a region section
        splits = line.split(":")
        regions.append({'area': splits[0].rstrip(), 'contents': [int(x) for x in splits[1].split()]})
    else:  # this is a shape pattern line
        count += line.count('#')

# part 1
numRegionsFittingPresents = 0
for region in regions:
    area = math.prod([int(x) for x in region['area'].split('x')])
    totalPresentArea = sum(region['contents']) * 9
    numRegionsFittingPresents += area >= totalPresentArea
print("Part 1 answer:", numRegionsFittingPresents)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("  Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("  Completed in %.1f s" % elapsedTime)
