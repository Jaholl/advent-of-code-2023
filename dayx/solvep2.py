import re, time

start_time = time.time()
file = open("dayx/input.txt", "r").readlines()

print("Process finished --- %s seconds ---" % round(time.time() - start_time, 4))