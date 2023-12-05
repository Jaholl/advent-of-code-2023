import re, time

start_time = time.time()
lines = open("day4/input.txt", "r").readlines()

fixedMatrix = {}
total = 0
for line in lines:
    cardworth = 0
    ticketId = int(re.search("\d+", line).group())
    input = line.split(":")[1]
    winnernumbers = input.split("|")[0]
    ournumbers = input.split("|")[1]
    winnernumbers = re.findall("\d+", winnernumbers)
    ournumbers = re.findall("\d+", ournumbers)

    for numb in ournumbers:
        if numb in winnernumbers:
            cardworth += 1
    
    fixedMatrix[ticketId] = (1, cardworth)

for line in lines:
    ticketId = int(re.search("\d+", line).group())
    for i in range(1, fixedMatrix[ticketId][1] +1):
        if ticketId + i > len(lines):
            continue
        fixedMatrix[ticketId + i] = (fixedMatrix[ticketId + i][0] + fixedMatrix[ticketId][0], fixedMatrix[ticketId + i][1])

total = 0
for item in fixedMatrix.values():
    total += item[0]
print(total)
print("Process finished --- %s seconds ---" % round(time.time() - start_time, 4))