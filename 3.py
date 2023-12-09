# any number adjacent to a symbol, even diagonally, is a "part number" and should be
#   included in your sum. (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, two numbers are not part numbers because they are not adjacent
#   to a symbol: 114 (top right) and 58 (middle right). Every other number is
#   adjacent to a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of
#   the part numbers in the engine schematic?

import re
import numpy as np

filename = "/Users/cyril/Documents/aoc23/input3.txt"

schematic = np.array([list(line) for line in open(filename)])[:,0:140]
print(schematic)

relevance = np.zeros(schematic.shape, dtype=int)
numbers   = np.empty(schematic.shape, dtype=str)

for y in np.arange(0, len(schematic)):
    for x in np.arange(0, len(schematic[y])):
        if re.fullmatch(r'^\d$', schematic[y][x]):
            left       = schematic[y][x-1]   if x-1 >= 0                                              else ''
            upperleft  = schematic[y-1][x-1] if y-1 >= 0                 and x-1 >= 0                 else ''
            upper      = schematic[y-1][x]   if y-1 >= 0                                              else ''
            upperright = schematic[y-1][x+1] if y-1 >= 0                 and x+1 <  len(schematic[y]) else ''
            right      = schematic[y][x+1]   if x+1 <  len(schematic[y])                              else ''
            lowerright = schematic[y+1][x+1] if y+1 <  len(schematic)    and x+1 <  len(schematic[y]) else ''
            lower      = schematic[y+1][x]   if y+1 <  len(schematic)                                 else ''
            lowerleft  = schematic[y+1][x-1] if y+1 <  len(schematic)    and x-1 >= 0                 else ''
            surroundings = left + upperleft + upper + upperright + right + lowerright + lower + lowerleft
            if re.search(r'[\#\$\%\&\*\+\-\/\=\@]', surroundings):
                relevance[y][x] = 1
            if re.fullmatch(r'[0-9]', left):
                if re.fullmatch(r'[0-9]', right):
                    numbers[y][x] = 'm'
                else:
                    numbers[y][x] = 'e'
            else:
                numbers[y][x] = 's'
        else:
            numbers[y][x] = ' '

print(relevance)
print(numbers)

count = 0
for check in np.arange(1, 10):
    for y in np.arange(0, len(numbers)):
        for x in np.arange(0, len(numbers[y])):
            if re.match(r'[sme]', numbers[y][x]):
                if relevance[y][x] == 0:
                    if x-1 >= 0:
                        if relevance[y][x-1] == 1:
                            count += 1
                            relevance[y][x] = 1
                    if x+1 < len(numbers[y]):
                        if relevance[y][x+1] == 1:
                            count += 1
                            relevance[y][x] = 1
    print("Changes after check " + str(check) + ": " + str(count))
    if count == 0:
        break
    else:
        count = 0

print(relevance)

for y in np.arange(0, len(numbers)):
    for x in np.arange(0, len(numbers[y])):
        if re.match(r'[sme]', numbers[y][x]):
            if relevance[y][x] == 0:
                numbers[y][x] = ' '

print(numbers)

parts = []
for y in np.arange(0, len(numbers)):
    for x in np.arange(0, len(numbers[y])):
        if re.match(r's', numbers[y][x]):
            if x+1 < len(numbers[y]):
                if re.match(r' ', numbers[y][x+1]):
                    parts.append(int(schematic[y][x]))
                elif re.match(r'e', numbers[y][x+1]):
                    parts.append(int(str(schematic[y][x]) + str(schematic[y][x+1])))
                elif re.match(r'm', numbers[y][x+1]):
                    if x+2 < len(numbers[y]):
                        if re.match(r'e', numbers[y][x+2]):
                            parts.append(int(str(schematic[y][x]) + str(schematic[y][x+1]) + str(schematic[y][x+2])))
                        elif re.match(r'm', numbers[y][x+2]):
                            if x+3 < len(numbers[y]):
                                if re.match(r'e', numbers[y][x+3]):
                                    parts.append(int(str(schematic[y][x]) + str(schematic[y][x+1]) + str(schematic[y][x+2]) + str(schematic[y][x+3])))
                                elif re.match(r'm', numbers[y][x+3]):
                                    print("\n\n     Found a 5-digit number :(    \n\n\n")
                                    quit()
                                else:
                                    print("this condition should not happen 1")
                            else:
                                print("this condition should not happen 2")
                        elif re.match(r' ', numbers[y][x+2]):
                            parts.append(int(str(schematic[y][x]) + str(schematic[y][x+1]) + str(schematic[y][x+2])))
                        else:
                            print("this condition should not happen 3")
                    else:
                        print("this condition should not happen 4")
                else:
                    print("this condition should not happen 5")
            else:
                print("this condition should not happen 6")

print(parts)

result = sum(parts)

print(result)