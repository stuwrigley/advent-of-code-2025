#!/usr/bin/python3
import time

start_time = time.time()

DAY = '07'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

beams = set()
beams.add(lines[0].index('S'))

# part 1
numSplits = 0
for row in lines[1:]:
    newBeams = set()
    for beam in beams:
        if row[beam] == '^':  # assume it won't go beyond the limits of the map
            newBeams.add(beam - 1)
            newBeams.add(beam + 1)
            numSplits += 1
        else:
            newBeams.add(beam)
    beams = newBeams
print("Part 1 answer:", numSplits)

# part 2
beams = {lines[0].index('S'): 1}
for row in lines[1:]:
    newBeams = beams.copy()
    for location, instances in beams.items():
        if instances > 0 and row[location] == '^':
            newBeams[location] = 0
            if location - 1 not in newBeams.keys():
                newBeams[location - 1] = 1
            else:
                newBeams[location - 1] = newBeams[location - 1] + instances
            if location + 1 not in newBeams.keys():
                newBeams[location + 1] = 1
            else:
                newBeams[location + 1] = newBeams[location + 1] + instances
    beams = newBeams
numBeams = 0
for location, instances in beams.items():
    numBeams += instances
print("Part 2 answer:", numBeams)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
