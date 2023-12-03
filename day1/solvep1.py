import re

file = open("day1/input.txt", "r")
lines = file.readlines()
        
found_numbers = []
for line in lines:
    match = re.findall("\d", line)
    found_numbers.append(int(str(match[0]) + str(match[-1])))
print(sum(found_numbers))
