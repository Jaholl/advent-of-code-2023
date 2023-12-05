import re, time

start_time = time.time()
lines = open("day2/input.txt", "r").readlines()

ids = []
for line in lines:
    blueMax = 14
    greenMax = 13
    redMax = 12
    resultRegex = "((?:(\d+) (\w+)(?:,|)))+"

    gameId = int(re.search("Game (\d+)", line).group(1))
    result = re.findall(resultRegex, line)

    doable = True
    for item in result:
        if item[2] == "blue" and int(item[1]) > blueMax:
            doable = False
            break
        if item[2] == "green" and int(item[1]) > greenMax:
            doable = False
            break
        if item[2] == "red" and int(item[1]) > redMax:
            doable = False
            break

    if doable:    
        ids.append(gameId)
print(sum(ids))
print("Process finished --- %s seconds ---" % round(time.time() - start_time, 4))