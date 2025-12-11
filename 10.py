#!/usr/bin/python3
import time
from collections import deque

start_time = time.time()

DAY = '10'
TEST = True
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip().split() for line in f]

machines = []
for line in lines:
    machine = dict()
    numLights = len(line[0]) - 2
    machine['numLights'] = numLights

    t = ['0'] * numLights
    target = line[0][1:-1]
    for index in range(numLights):
        if target[index] == '#':
            t[int(index)] = '1'
    machine['target'] = int(''.join(t), base=2)

    machine['jolts'] = []
    schematics = []
    for schematic in line[1:-1]:
        s = ['0'] * numLights
        for index in schematic[1:-1].split(','):
            s[int(index)] = '1'
        schematics.append(int(''.join(s), base=2))
        machine['jolts'].append([int(x) for x in s])
    machine['schematics'] = schematics
    machine['joltage'] = line[-1]

    machines.append(machine)

# part 1
runningSum = 0
for machine in machines:
    stillToProcess = deque([(machine['target'], 0)])
    seen = set()
    seen.add(machine['target'])
    while stillToProcess:
        target, numFlips = stillToProcess.popleft()
        numFlips += 1
        for schematic in machine['schematics']:
            flipped = target ^ schematic
            if flipped == 0:
                runningSum += numFlips
                stillToProcess = deque()
                break
            else:
                if flipped not in seen:
                    stillToProcess.append((flipped, numFlips))
                    seen.add(flipped)
print("Part 1 answer:", runningSum)
elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("  Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("  Completed in %.1f s" % elapsedTime)

# part 2
runningSum = 0
for machine in machines:
    target = [int(x) for x in machine['joltage'][1:-1].split(',')]
    candidates = machine['jolts']

    stillToProcess = deque([([0] * machine['numLights'], 0)])

    while stillToProcess:
        curCounts, numPresses = stillToProcess.popleft()
        if curCounts > target:
            continue
        numPresses += 1
        for candidate in candidates:
            newCounts = [sum(x) for x in zip(curCounts, candidate)]
            if newCounts == target:
                runningSum += numPresses
                # print("This machine's solution:",numPresses)
                stillToProcess = deque()
                break
            else:
                stillToProcess.append((newCounts, numPresses))

print("Part 2 answer:", runningSum)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("  Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("  Completed in %.1f s" % elapsedTime)
