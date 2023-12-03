import re

input = open("day2/input.txt", 'r')
lines = input.readlines()

ids = []
for line in lines:
    blueMax, greenMax, redMax = 0
    gameRegex = "Game (\d+)"
    resultRegex = "((?:(\d+) (\w+)(?:,|)))+"

    gameId = int(re.search(gameRegex, line).group(1))
    result = re.findall(resultRegex, line)

    for item in result:
        if item[2] == "blue" and int(item[1]) > blueMax:
            blueMax = int(item[1])
        if item[2] == "green" and int(item[1]) > greenMax:
            greenMax = int(item[1])
        if item[2] == "red" and int(item[1]) > redMax:
            redMax = int(item[1])
            
    ids.append(blueMax*greenMax*redMax)
print(sum(ids))