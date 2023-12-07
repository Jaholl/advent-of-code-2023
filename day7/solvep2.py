import re, time
from operator import itemgetter

start_time = time.time()
lines = open("day7/input.txt", "r").readlines()

betmap = {}
hands = { 0 : [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [] }
for line in lines:
  cards = [int(c.replace('T', '10').replace('J', '1').replace('Q', '12').replace('K', '13').replace('A', '14')) for c in [*line.split(" ")[0]]]
  bet = int(line.split(" ")[1])
  betmap["".join(str(cards))] = bet
  mod = {}
  jokers = 0
  for card in cards:
    if card == 1:
      jokers += 1
      continue
    if card in mod.keys():
      mod[card] += 1
    else:
      mod[card] = 1
  
  unique_cards = len(mod.keys())
  for i in mod.keys():
    mod[i] += jokers

  if (unique_cards == 5): # high card
    hands[0].append(cards)
  elif (unique_cards == 4): # one pair
    hands[1].append(cards)
  elif (unique_cards == 3): # two pairs or three of a kind
    if 3 in mod.values():
      hands[3].append(cards)
    else:
      hands[2].append(cards)
  elif (unique_cards == 2): # full house or four of a kind
    if 4 in mod.values():
      hands[5].append(cards)
    else:
      hands[4].append(cards)
  elif (unique_cards == 1): # five of a kind
    hands[6].append(cards)

rank = []
for index in hands.keys():
  hands[index] = sorted(hands[index], key=itemgetter(0,1,2,3,4), reverse=True)
[rank.append(x) for x in hands[6]]
[rank.append(x) for x in hands[5]]
[rank.append(x) for x in hands[4]]
[rank.append(x) for x in hands[3]]
[rank.append(x) for x in hands[2]]
[rank.append(x) for x in hands[1]]
[rank.append(x) for x in hands[0]]

total = 0
for index, item in enumerate(rank):
  total += (len(rank) - index) * betmap["".join(str(item))]

print(total)
print("Process finished --- %s seconds ---" % round(time.time() - start_time, 4))