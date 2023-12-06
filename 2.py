# Determine which games would have been possible if the bag had been loaded with only
#     12 red cubes,
#     13 green cubes, and
#     14 blue cubes.
# What is the sum of the IDs of those games?

import re
from itertools import compress

filename = "/Users/cyril/Documents/aoc23/input2.txt"

def getgamenumber(line):
	gametitle = re.findall(r'Game \d+(?=:)', line)
	gamenumber = re.findall(r'\d+', gametitle[0])
	result = int(gamenumber[0])
	return result

def getgames(line):
    gameline = re.findall(r'(?<=: ).*$', line)
    games = gameline[0].split('; ')
    reds   = [getamount(game, 'red')   for game in games]
    greens = [getamount(game, 'green') for game in games]
    blues  = [getamount(game, 'blue')  for game in games]
    return [reds, greens, blues]

def getamount(game, colour):
	colourfilter = '\d+ ' + colour
	filteredgame = re.findall(re.compile(colourfilter), game)
	if len(filteredgame) >= 1:
	    amount = re.findall(r'\d+', filteredgame[0])
	    result = int(amount[0])
	else:
		result = 0
	return result

def getmaximums(game):
	reds = game[0]
	greens = game[1]
	blues = game[2]
	maxreds = max(reds)
	maxgreens = max(greens)
	maxblues = max(blues)
	return maxreds, maxgreens, maxblues

def isgamepossible(game):
	red, green, blue = game
	if red <= 12 and green <= 13 and blue <= 14:
		return True
	else:
		return False

gamenumbers     = [getgamenumber(line)  for line in open(filename)]
games           = [getgames(line)       for line in open(filename)]
maximums        = [getmaximums(game)    for game in games]
checkedmaximums = [isgamepossible(game) for game in maximums]

validgameids = list(compress(gamenumbers, checkedmaximums))
solution = sum(validgameids)
print(solution)