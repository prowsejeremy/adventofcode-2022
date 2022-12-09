with open ("data.txt", "r") as dataFile:
  rawData = dataFile.read().splitlines()

key = {
  "X" : "A", # Rock
  "Y" : "B", # Paper
  "Z" : "C" # Scissors
}

weakness = {
  "A" : "B",
  "B" : "C",
  "C" : "A"
}

playScore = {
  "A" : 1,
  "B" : 2,
  "C" : 3
}

resultScore = {
  "W" : 6,
  "D" : 3,
  "L" : 0
}

score = 0

for round in rawData:
  round.split()

  opponent = round[0]
  play = key[round[2]]

  # Add shape score
  score += playScore[play]

  if opponent == play: # Draw
    score += resultScore["D"]
  elif weakness[opponent] == play: # Win
    score += resultScore["W"]

print("///////////// TOTAL SCORE /////////////")
print(score)