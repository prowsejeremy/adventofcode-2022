# Open data file
with open ("data.txt", "r") as dataFile:
  rawData = dataFile.read()
  rawArray = rawData.split()

# Define key variables
rows = []
columns = []
countedItems = []

# Build row and column lists from the raw data
holdingRow = []
rowIndex = 0

for index, row in enumerate(rawArray):
  for charIndex, char in enumerate(row):
    try:
      rows[index].append(int(char))
    except:
      rows.append([int(char)])

    try:
      columns[charIndex].append(int(char))
    except:
      columns.append([int(char)])


def getScore(current, row):
  score = 0
  for i in row:

    if (current <= i):
      score += 1
      break
    else:
      score += 1

  return score


def process(startIndex, row):

  if ((startIndex == 0) or (startIndex == (len(row)-1))):
    return 0
  else:

    current = row[startIndex]
    forwardScore = 0
    backwardScore = 0

    forwardScore = getScore(current, row[startIndex+1:])

    # Get items up to our starting index, and reverse the order
    # to simulate looping in reverse.
    reversed = row[:startIndex]
    reversed.reverse()

    backwardScore = getScore(current, reversed)
  
    return forwardScore * backwardScore


def main():
  scores = []

  for rowIndex, row in enumerate(rows):

    for rowItemIndex, rowItem in enumerate(row):
      
      # Rows
      rowScore = process(rowItemIndex, row)

      # Columns
      col = columns[rowItemIndex]
      colItemIndex = rowIndex

      colScore = process(colItemIndex, col)

      totalScore = rowScore * colScore
      scores.append(totalScore)

  print('Highest:', max(scores))


# Run
main()