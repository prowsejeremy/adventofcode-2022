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

# Sort to get the most stacked elf
orderedElves = sorted( listOfElvesAndTheirFood.items(), key=lambda x: x[1], reverse=True )

topThreeElvesFood = 0
for idx in range(3):
  topThreeElvesFood += orderedElves[idx][1]

print("//////////// MOST STACKED ELVES FOOD ////////////")
print(topThreeElvesFood)