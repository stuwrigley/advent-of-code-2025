#!/usr/bin/python3
import time

start_time = time.time()

DAY = '02'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

ranges = [x.strip() for x in lines[0].split(',')]

# part 1
runningSum = 0
for r in ranges:
    ids = r.split('-')
    for id in range(int(ids[0]), int(ids[1]) + 1):
        id = str(id)
        if len(id) % 2 == 0 and id[:int(len(id) / 2)] == id[int(len(id) / 2):]:
            runningSum += int(id)
print("Part 1 answer:", runningSum)


def isInvalid(id):
    for i in range(1, int(len(id) / 2) + 1):
        multiplier=int(len(id)/i)
        if id[:i]*multiplier==id:
            return True
    return False

# part 2
runningSum = 0
for r in ranges:
    ids = r.split('-')
    for id in range(int(ids[0]), int(ids[1]) + 1):
        if isInvalid(str(id)):
            runningSum += id
print("Part 2 answer:", runningSum)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
