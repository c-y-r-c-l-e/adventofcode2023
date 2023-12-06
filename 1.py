# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
#
# For example:
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
#
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
#
# Consider your entire calibration document. What is the sum of all of the calibration values?

import re

filename = "/Users/cyril/Documents/aoc23/eightfivesssxxmgthreethreeone1sevenhnz.txt"

# with open(filename) as file:
#     for line in file:
#         print('\n')
#         print(line)
#         numbers = re.findall(r'\d', line)
#         print(numbers)
#         selectednumbers = numbers[0] + numbers[-1]
#         print(selectednumbers)
#         int(selectednumbers)

def getcalibrationvalues(line):
    numbers = re.findall(r'\d', line)
    selectednumbers = numbers[0] + numbers[-1]
    result = int(selectednumbers)
    return(result)

calibrationvalues = [getcalibrationvalues(line) for line in open(filename)]
print(calibrationvalues)
total = sum(calibrationvalues)
print("Sum of calibrationvalues:  " + str(total))