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

def find_if_in_interval(item, list):
  for key in list.keys():
    source, fullrange = key.split(',')
    if int(item) >= int(source) and int(item) < int(source) + int(fullrange):
      difference = int(item) - int(source)
      return (int(list[key]) + difference)
  
  return (item)


categoryInput = []
for cat in category:
  categoryInput.append(re.findall("(\d+)", cat))

seeds_to_plant = re.findall("(\d+)", category[1])

seed_to_soil = source_destination_range_map(categoryInput[2])
soil_to_fertilizer = source_destination_range_map(categoryInput[3])
fertilizer_to_water = source_destination_range_map(categoryInput[4])
water_to_light = source_destination_range_map(categoryInput[5])
light_to_temperature = source_destination_range_map(categoryInput[6])
temperature_to_humidity = source_destination_range_map(categoryInput[7])
humidity_to_location = source_destination_range_map(categoryInput[8])

lowest_location = 99999999999999999999999999
for seed in seeds_to_plant:
  soil = find_if_in_interval(seed, seed_to_soil)
  fertilizer = find_if_in_interval(soil, soil_to_fertilizer)
  water = find_if_in_interval(fertilizer, fertilizer_to_water)
  light = find_if_in_interval(water, water_to_light)
  temp = find_if_in_interval(light, light_to_temperature)
  hum = find_if_in_interval(temp, temperature_to_humidity)
  loc = find_if_in_interval(hum, humidity_to_location)

  if loc < lowest_location:
    lowest_location = loc

print(lowest_location)
print("Process finished --- %s seconds ---" % round(time.time() - start_time, 4))