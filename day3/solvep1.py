import re

file = open("day3/input", "r")
lines = file.read().split("\n")

matrix  = []
numbers = []
for line in lines[:-1]:
    matrix.append([*line])
    numbers.append([(m.span(), int(m.group())) for m in re.finditer("(\d+)", line)])

symbols = []
for xindex, x in enumerate(matrix):
    for yindex, y in enumerate(x):
        if (not re.compile('\.|\d').match(y)):
            symbols.append((xindex, yindex))

valid = []
for rowIndex, numb in enumerate(numbers):
    for n in numb:
        numbAdded = False
        for y in range(n[0][0], n[0][1]):
            if numbAdded:
                break
            for s in symbols:
                if rowIndex - 1 == s[0] and (y - 1 == s[1] or y == s[1] or y + 1 == s[1]):
                    valid.append(n[1])
                    numbAdded = True

                if rowIndex == s[0] and (y - 1 == s[1] or y == s[1] or y + 1 == s[1]):
                    valid.append(n[1])
                    numbAdded = True

                if rowIndex + 1 == s[0] and (y - 1 == s[1] or y == s[1] or y + 1 == s[1]):
                    valid.append(n[1])
                    numbAdded = True

                if numbAdded:
                    break
print(valid)
print(sum(valid))

# above = [(-1,-1), (-1, 0), (-1, 1)]
# same = [(0,-1), (0, 1)]
# below = [(1,-1), (1, 0), (1, 1)]

# for cords in symbols:
#     for dev in above:
#         if (re.compile('\d').match(matrix[cords[0]+dev[0]][cords[1]+dev[1]])):
#             print("Above: ", matrix[cords[0]+dev[0]][cords[1]+dev[1]])
#     for dev in same:
#         if (re.compile('\d').match(matrix[cords[0]+dev[0]][cords[1]+dev[1]])):
#             print("Same: ", matrix[cords[0]+dev[0]][cords[1]+dev[1]])
#     for dev in below:
#         if (re.compile('\d').match(matrix[cords[0]+dev[0]][cords[1]+dev[1]])):
#             print("Below: ", matrix[cords[0]+dev[0]][cords[1]+dev[1]])