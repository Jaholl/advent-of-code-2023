import re, time

start_time = time.time()
category = open("day5/input.txt", "r").read().split(":")

def source_destination_range_map(input):
  returnmap = {}
  destination = -1
  source = -1
  fullrange = -1
  for r in range(len(input)):
    if r % 3 == 0:
      destination = int(input[r])
    if r % 3 == 1:
      source = int(input[r])
    if r % 3 == 2:
      fullrange = int(input[r])
    if destination != -1 and source != -1 and fullrange != -1:
      returnmap[str(source) + ',' + str(fullrange)] = str(destination)
      destination = -1
      source = -1
      fullrange = -1
  return returnmap

def find_if_in_interval(item, list, nextList, jump):
  for key in list.keys():
    source, fullrange = key.split(',')
    if int(item) >= int(source) and int(item) < int(source) + int(fullrange):
      difference = int(item) - int(source)
      if 0 < int(fullrange) + int(source) - int(item):
        jump.append(int(fullrange) + int(source) - int(item))
      else:
        jump.append(1)
      return (int(list[key]) + difference)
  
  smallestjump = 99999999999
  for key in nextList.keys():
    nextsource, _ = key.split(',')
    if 0 < int(nextsource) - int(item) < smallestjump:
      smallestjump = int(nextsource) - int(item)
  jump.append(smallestjump)
  return (item)

categoryInput = []
for cat in category:
  categoryInput.append(re.findall("(\d+)", cat))

seeds_to_plant = []
seed = -1
fullrange = -1
for r in range(len(categoryInput[1])):
  if r % 2 == 0:
    seed = int(categoryInput[1][r])
  if r % 2 == 1:
    fullrange = int(categoryInput[1][r])
  if seed != -1 and fullrange != -1:
    seeds_to_plant.append((seed, fullrange))
    seed = -1
    fullrange = -1

seed_to_soil = source_destination_range_map(categoryInput[2])
soil_to_fertilizer = source_destination_range_map(categoryInput[3])
fertilizer_to_water = source_destination_range_map(categoryInput[4])
water_to_light = source_destination_range_map(categoryInput[5])
light_to_temperature = source_destination_range_map(categoryInput[6])
temperature_to_humidity = source_destination_range_map(categoryInput[7])
humidity_to_location = source_destination_range_map(categoryInput[8])

lowest_location = 99999999999999999999999999
for key, value in seeds_to_plant:
  index = key
  while index <= key+value:
    jump = []
    soil = find_if_in_interval(index, seed_to_soil, soil_to_fertilizer, jump)
    fertilizer = find_if_in_interval(soil, soil_to_fertilizer, fertilizer_to_water, jump)
    water = find_if_in_interval(fertilizer, fertilizer_to_water, water_to_light, jump)
    light = find_if_in_interval(water, water_to_light, light_to_temperature, jump)
    temp = find_if_in_interval(light, light_to_temperature, temperature_to_humidity, jump)
    hum = find_if_in_interval(temp, temperature_to_humidity, humidity_to_location, jump)
    loc = find_if_in_interval(hum, humidity_to_location, humidity_to_location, jump)

    if loc < lowest_location:
      lowest_location = loc
    index += min(jump)
    if (index == key+value):
      index += 1

print(lowest_location)
print("Process finished --- %s seconds ---" % round(time.time() - start_time, 4))