import re, time, math

start_time = time.time()
file = open("day6/input.txt", "r").readlines()

race_length = int("".join(re.findall("\d+", file[0])))
record_length = int("".join(re.findall("\d+", file[1])))

race_optimize = 0
for t in range(round((race_length + 1) / 2), 0, -1):
  traveled_dist = t * (race_length - t)
  if traveled_dist > record_length:
    race_optimize += 1
  else:
    break

for t in range(round((race_length + 1) / 2) + 1, race_length + 1, 1):
  traveled_dist = t * (race_length - t)
  if traveled_dist > record_length:
    race_optimize += 1
  else:
    break

print(race_optimize)
print("Process finished --- %s seconds ---" % round(time.time() - start_time, 4))