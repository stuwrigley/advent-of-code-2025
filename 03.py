#!/usr/bin/python3
import time

start_time = time.time()

DAY = '03'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'
print("Day", DAY, "-", 'Test data' if TEST else 'Actual data')

with open(inputFilename) as f:
    lines = [[int(x) for x in line.rstrip()] for line in f]

# part 1
runningSum = 0
for bank in lines:
    firstDigit = max(bank[:-1])
    secondDigit = max(bank[bank.index(firstDigit) + 1:])
    runningSum += int(str(firstDigit) + str(secondDigit))
print("Part 1 answer:", runningSum)

# part 2
numBatteries = 12
runningSum = 0
for bank in lines:
    digits = ''
    previousDigitPosition = -1
    for remainingDigits in range(numBatteries, 0, -1):
        bankWindow = bank[previousDigitPosition + 1: len(bank) - remainingDigits + 1]
        currentDigit = max(bankWindow)
        previousDigitPosition += bankWindow.index(currentDigit) + 1
        digits += str(currentDigit)
    runningSum += int(digits)
print("Part 2 answer:", runningSum)

elapsedTime = (time.time() - start_time)
if elapsedTime < 1:
    print("Completed in %.0f ms" % (elapsedTime * 1000))
else:
    print("Completed in %.1f s" % elapsedTime)
