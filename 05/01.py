with open ("data.txt", "r") as dataFile:
  rawData = dataFile.read().splitlines()

with open ("steps.txt", "r") as stepsFile:
  stepsData = stepsFile.read().splitlines()

crateArray = []
topCrates = ""

for lineIdx, line in enumerate(rawData):
  column = 0
  if lineIdx+1 != len(rawData):
    for idx, character in enumerate(line):
      # Check if the character we are at in the line is multiple of 4
      # With a starting index of 2
      if ((idx + 2) % 4 == 0):
        # Create the nested lists in the first lines looping
        if lineIdx == 0:
          crateArray.append([])

        crate = line[idx-1:idx]
        if crate != ' ':
          crateArray[column].append(crate)
        column += 1

print("//////////// OG CRATE ARRAY ////////////")
print(crateArray, len(crateArray))

for step in stepsData:

  # Set indexes for the content in the step string
  midx = 5
  fidx = step.index(" from ")
  tidx = step.index(" to ")

  # Get the steps from the string
  m = int(step[midx:fidx])
  f = int(step[fidx+6:tidx]) - 1
  t = int(step[tidx+4:len(step)]) - 1

  for item in range(m):
    inTransit = crateArray[f].pop(0)
    crateArray[t].insert(0, inTransit)

print("//////////// NEW CRATE ARRAY ////////////")
print(crateArray, len(crateArray))

for crateColumn in crateArray:
  topCrates += crateColumn[0]

print("///////////// TOP CRATES /////////////")
print(topCrates)