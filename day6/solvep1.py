import re, time, math

start_time = time.time()
file = open("day6/input.txt", "r").readlines()

race_lengths = [int(d) for d in re.findall("\d+", file[0])]
record_lengths = [int(d) for d in re.findall("\d+", file[1])]

optimizations = []
for race_nmb in range(0, len(race_lengths)):
  race_optimize = 0
  for t in range(0, race_lengths[race_nmb] + 1):
    traveled_dist = t * (race_lengths[race_nmb] - t)
    if traveled_dist > record_lengths[race_nmb]:
      race_optimize += 1
  optimizations.append(race_optimize)

print(math.prod(optimizations))
print("Process finished --- %s seconds ---" % round(time.time() - start_time, 4))