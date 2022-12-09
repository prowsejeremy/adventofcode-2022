# Read file initially
with open ("data.txt", "r") as myfile:
  rawData = myfile.read().splitlines()

# Loop raw data
listOfElvesAndTheirFood = {}
elfCount = 0
foodTotal = 0

for entry in rawData:
  if entry != '':
    foodTotal += int(entry)
  else:
    listOfElvesAndTheirFood[elfCount] = foodTotal
    foodTotal = 0
    elfCount += 1

print("//////////// LIST OF ELVES AND THEIR FOOD ////////////")
print(listOfElvesAndTheirFood)

# Sort to get the most stacked elf
orderedElves = sorted( listOfElvesAndTheirFood.items(), key=lambda x: x[1], reverse=True )
mostStackedElf = orderedElves[0]

print("//////////// MOST STACKED ELF ////////////")
print(mostStackedElf)