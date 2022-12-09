with open ("data.txt", "r") as dataFile:
  rawData = dataFile.read().splitlines()

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0

def compareCompartments(compartmentOne, compartmentTwo):
  for char1 in compartmentOne:
    for char2 in compartmentTwo:
      if char1 == char2:
        return alphabet.index(char1) + 1

for rucksack in rawData:

  rucksackCompartmentSize = len(rucksack)//2

  compartmentOne = rucksack[:rucksackCompartmentSize]
  compartmentTwo = rucksack[rucksackCompartmentSize:]

  total += compareCompartments(compartmentOne, compartmentTwo)

print("///////////// TOTAL /////////////")
print(total)