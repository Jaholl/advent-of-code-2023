import re

file = open("day3/input", "r")
lines = file.read().split("\n")

matrix  = []
for line in lines[:-1]:
    matrix.append([*line])

symbols = []
for xindex, x in enumerate(matrix):
    for yindex, y in enumerate(x):
        if (not re.compile('\.|\d').match(y)):
            symbols.append((xindex, yindex))

for cords in symbols:
    if (re.compile('\d').match(matrix[cords[0]-1][cords[1]-1])):
        print(matrix[cords[0]-1][cords[1]-1])