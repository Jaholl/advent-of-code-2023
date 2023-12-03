import re
import math

file = open("day3/input.txt", "r")
lines = file.read().split("\n")

matrix  = []
numbers = []
for line in lines[:-1]:
    matrix.append([*line])
    numbers.append([(m.span(), int(m.group())) for m in re.finditer("(\d+)", line)])

symbols = []
for xindex, x in enumerate(matrix):
    for yindex, y in enumerate(x):
        if (re.compile('\*').match(y)):
            symbols.append((xindex, yindex))

valid = {}
for rowIndex, numb in enumerate(numbers):
    for n in numb:
        numbAdded = False
        for y in range(n[0][0], n[0][1]):
            if numbAdded:
                break
            for s in symbols:
                if rowIndex - 1 == s[0] and (y - 1 == s[1] or y == s[1] or y + 1 == s[1]):
                    if str(str(s[0]) + "," + str(s[1])) in valid.keys():
                        valid[str(s[0]) + "," + str(s[1])] += [(n[1])]
                    else:
                        valid[str(s[0]) + "," + str(s[1])] = [(n[1])]
                    numbAdded = True

                if rowIndex == s[0] and (y - 1 == s[1] or y + 1 == s[1]):
                    if str(str(s[0]) + "," + str(s[1])) in valid.keys():
                        valid[str(s[0]) + "," + str(s[1])] += [(n[1])]
                    else:
                        valid[str(s[0]) + "," + str(s[1])] = [(n[1])]
                    numbAdded = True

                if rowIndex + 1 == s[0] and (y - 1 == s[1] or y == s[1] or y + 1 == s[1]):
                    if str(str(s[0]) + "," + str(s[1])) in valid.keys():
                        valid[str(s[0]) + "," + str(s[1])] += [(n[1])]
                    else:
                        valid[str(s[0]) + "," + str(s[1])] = [(n[1])]
                    numbAdded = True

                if numbAdded:
                    break

total = []
for key in valid.keys():
    if len(valid[key]) == 2:
        total.append(math.prod(valid[key]))
print(sum(total))
