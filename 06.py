#!/usr/bin/python3
import time
import operator

operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

start_time = time.time()

DAY = '06'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line for line in f]

numbers = [[int(x) for x in line.split()] for line in lines[:-1]]
operators = lines[-1].split()

# part 1
runningSum = 0
for numberSetID, operation in enumerate(operators):
    op = operatorlookup.get(operation)
    setRunningValue = numbers[0][numberSetID]
    for numberID in range(1, len(numbers)):
        setRunningValue = op(setRunningValue, numbers[numberID][numberSetID])
    runningSum += setRunningValue
print("Part 1 answer:", runningSum)

# part 2
runningSum = 0
maxLen = max([len(x) for x in lines]) - 1  # -1 to remove carriage returns
operatorPositions = [idx for idx, item in enumerate(lines[-1]) if ' ' not in item]

numberSet = []
for position in range(maxLen - 1, -1, -1):
    if position + 1 not in operatorPositions:  # skip the blank columns
        thisNum = ''
        for row in range(len(lines) - 1):
            thisNum += lines[row][position] if lines[row][position].isnumeric() else ''
        numberSet.append(int(thisNum))
        if position in operatorPositions:
            op = operatorlookup.get(lines[-1][position])
            setRunningValue = numberSet[0]
            for number in numberSet[1:]:
                setRunningValue = op(setRunningValue, number)
            runningSum += setRunningValue
            numberSet = []
print("Part 2 answer:", runningSum)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
