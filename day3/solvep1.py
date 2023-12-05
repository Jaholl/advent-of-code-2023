import re, time

start_time = time.time()
lines = open("day3/input.txt", "r").read().split("\n")

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
print(sum(valid))
print("Process finished --- %s seconds ---" % round(time.time() - start_time, 4))