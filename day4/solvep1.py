import re, time

start_time = time.time()
lines = open("day4/input.txt", "r").readlines()

total = 0
for line in lines:
    cardworth = 0
    input = line.split(":")[1]
    winnernumbers = input.split("|")[0]
    ournumbers = input.split("|")[1]
    winnernumbers = re.findall("\d+", winnernumbers)
    ournumbers = re.findall("\d+", ournumbers)

    for numb in ournumbers:
        if numb in winnernumbers:
            if cardworth == 0:
                cardworth = 1
            else:
                cardworth *= 2
    
    total += cardworth
print(total)
print("Process finished --- %s seconds ---" % round(time.time() - start_time, 4))