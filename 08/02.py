# Open data file
# Number 5 on the 4th row has the best score
with open ("data-test.txt", "r") as dataFile:
  rawData = dataFile.read()

# Define key variables
rows = []
columns = []
countedItems = []

# Build row and column lists from the raw data
holdingRow = []
rowIndex = 0
for index, char in enumerate(rawData):
  if (char != '\n'):
    charObj = {index:int(char)}
    holdingRow.append(charObj)
    try:
      columns[rowIndex].append(charObj)
    except:
      columns.append([charObj])
    
    rowIndex += 1
  elif (char == '\n'):
    rows.append(holdingRow)
    holdingRow=[]
    rowIndex = 0


def checkAndAppend(item, highestItem):
  itemID = int(list(item.keys())[0])
  itemVal = int(list(item.values())[0])
  if (highestItem < itemVal):
    if (not itemID in countedItems):
      countedItems.append(itemID)
    highestItem = itemVal
  
  return highestItem


def processList(list):
  highestItem = -1
  for item in list:
    highestItem = checkAndAppend(item, highestItem)


# Iterate over rows
for row in rows:
  processList(row)
  processList(reversed(row))

# Iterate over columns
for column in columns:
  processList(column)
  processList(reversed(column))

print("Total items visible:", len(countedItems))