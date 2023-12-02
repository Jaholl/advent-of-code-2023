import re

input = open("day2/input", 'r')
lines = input.readlines()

blueMax = 14
greenMax = 13
redMax = 12

ids = []

for line in lines:

    gameRegex = "Game (\d+)"
    resultRegex = "((?:(\d+) (\w+)(?:,|)))+"
    gameId = int(re.search(gameRegex, line).group(1))
    result = re.findall(resultRegex, line)

    print(gameId)
    print(result)
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