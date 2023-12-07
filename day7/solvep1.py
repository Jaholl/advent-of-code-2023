import re, time
from operator import itemgetter

start_time = time.time()
lines = open("day7/sample.txt", "r").readlines()

hands = { 0 : [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
for line in lines:
  cards = [int(c.replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')) for c in [*line.split(" ")[0]]]
  bet = int(line.split(" ")[1])

  mod = {}
  for card in cards:
    if card in mod.keys():
      mod[card] += 1
    else:
      mod[card] = 1
  
  unique_cards = len(mod.keys())
  if (unique_cards == 5): # high card
    hands[0].append((cards, bet))
  elif (unique_cards == 4): # one pair
    hands[1].append((cards, bet))
  elif (unique_cards == 3): # two pairs or three of a kind
    if 3 in mod.values():
      hands[3].append((cards, bet))
    else:
      hands[2].append((cards, bet))
  elif (unique_cards == 2): # full house or four of a kind
    if 4 in mod.values():
      hands[5].append((cards, bet))
    else:
      hands[4].append((cards, bet))
  elif (unique_cards == 1): # five of a kind
    hands[6].append((cards, bet))

# rank = []
# for index in range(0, 7):
#   for hand in hands[index]:
#     rankvalue = 0
#     for card in range(0, len(hand[0])):
#       rankvalue += hand[0][card]
#     rank.append((rankvalue, hand[1]))

rank = []
hands[6].sort(key=lambda x: x[0])
hands[5].sort(key=lambda x: x[0])
hands[4].sort(key=lambda x: x[0])
hands[3].sort(key=lambda x: x[0])
print(hands[2])
rank.append(sorted(hands[2], key=itemgetter(0,1,2,3,4)))
hands[1].sort(key=lambda x: x[0])

# total = 0
# rank.sort(reverse=True)
# for index, item in enumerate(rank):
#   total += (len(rank) - index) * item[1]
print(hands)
print("Process finished --- %s seconds ---" % round(time.time() - start_time, 4))