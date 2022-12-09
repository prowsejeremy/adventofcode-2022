with open ("data.txt", "r") as dataFile:
  rawData = dataFile.read().splitlines()

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0
groupedRucksacks = []

def compareGroupedRucksacks(groupedRucksacks):
  for char1 in groupedRucksacks[0]:
    for char2 in groupedRucksacks[1]:
      if char1 == char2:
        for char3 in groupedRucksacks[2]:
          if char1 == char3:
            return alphabet.index(char1) + 1


for idx, rucksack in enumerate(rawData):

  groupedRucksacks.append(rucksack)
  
  if (idx + 1) % 3 == 0:

    total += compareGroupedRucksacks(groupedRucksacks)
    groupedRucksacks = []

print("///////////// TOTAL /////////////")
print(total)