#!/usr/bin/python3
import time
from collections import deque
from scipy.optimize import linprog
import numpy as np

start_time = time.time()

DAY = '10'
TEST = False
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

    machine['buttons'] = []
    schematics = []
    for schematic in line[1:-1]:
        machine['buttons'].append([int(x) for x in schematic[1:-1].split(',')])
        s = ['0'] * numLights
        for index in schematic[1:-1].split(','):
            s[int(index)] = '1'
        schematics.append(int(''.join(s), base=2))
    machine['schematics'] = schematics
    machine['joltage'] = [int(x) for x in line[-1][1:-1].split(',')]

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
    buttons = machine['buttons']
    A = np.array([[int(i in button) for i in range(len(machine['joltage']))]
                  for button in buttons]).transpose()
    b = np.array(machine['joltage'])
    c = [1] * len(buttons)
    solution = linprog(c=c, A_eq=A, b_eq=b, integrality=1)
    runningSum += solution.fun
print("Part 2 answer:", int(runningSum))

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("  Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("  Completed in %.1f s" % elapsedTime)
