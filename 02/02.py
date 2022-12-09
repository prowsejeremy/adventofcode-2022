with open ("data.txt", "r") as dataFile:
  rawData = dataFile.read().splitlines()

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
  result = round[2]

  if result == "X": # Loose
    play = weakness[weakness[opponent]]
  elif result == "Y": # Draw
    play = opponent
    score += resultScore["D"]
  else: # Win
    play = weakness[opponent]
    score += resultScore["W"]

  # Add shape score
  score += playScore[play]

print("///////////// TOTAL SCORE /////////////")
print(score)