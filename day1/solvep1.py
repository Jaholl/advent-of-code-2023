import re, time

start_time = time.time()
lines = open("day1/input.txt", "r").readlines()
        
found_numbers = []
for line in lines:
    match = re.findall("\d", line)
    found_numbers.append(int(str(match[0]) + str(match[-1])))

print(sum(found_numbers))
print("Process finished --- %s seconds ---" % round(time.time() - start_time, 4))