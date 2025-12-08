#!/usr/bin/python3
import time

start_time = time.time()

DAY = '08'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

junctionBoxes = [[int(x) for x in y.split(',')] for y in lines]


def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5


# part 1 and 2
junctionBoxDistances = {}
for junctionBox1 in junctionBoxes:
    for junctionBox2 in junctionBoxes:
        if junctionBox1 != junctionBox2:
            if (tuple(junctionBox1), tuple(junctionBox2)) not in junctionBoxDistances.keys() and (tuple(junctionBox2), tuple(junctionBox1)) not in junctionBoxDistances.keys():
                junctionBoxDistances[(tuple(junctionBox1), tuple(junctionBox2))] = distance(junctionBox1, junctionBox2)

sortedJunctionBoxDistances = dict(sorted(junctionBoxDistances.items(), key=lambda item: item[1]))

circuits = []
maxConnections = 10 if TEST else 1000
count = 0
for junctionBox1, junctionBox2 in sortedJunctionBoxDistances:
    count += 1
    alreadyInCircuit = False
    for circuit in circuits:
        alreadyInCircuit = junctionBox1 in circuit or junctionBox2 in circuit
        if alreadyInCircuit:
            circuit.add(junctionBox1)
            circuit.add(junctionBox2)
            break

    if alreadyInCircuit:
        # need to check if any of the new points are already in another circuit. if so, merge...
        overlappingCircuits = []
        for circuit in circuits:
            if junctionBox1 in circuit or junctionBox2 in circuit:
                overlappingCircuits.append(circuit)
        if len(overlappingCircuits) > 1:
            mergedCircuit = set()
            for circuit in overlappingCircuits:
                circuits.remove(circuit)
                mergedCircuit = mergedCircuit.union(circuit)
            circuits.append(mergedCircuit)
    else:
        newCircuit = set()
        newCircuit.add(junctionBox1)
        newCircuit.add(junctionBox2)
        circuits.append(newCircuit)
    if count == maxConnections: # part 1
        circuitLengths = []
        for circuit in circuits:
            circuitLengths.append(len(circuit))
        circuitLengths.sort(reverse=True)
        runningMult = circuitLengths[0] * circuitLengths[1] * circuitLengths[2]
        print("Part 1 answer:", runningMult)
    if len(circuits) == 1 and len(circuits[0]) == len(junctionBoxes): # part 2
        print("Part 2 answer:", junctionBox1[0] * junctionBox2[0])
        break

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
