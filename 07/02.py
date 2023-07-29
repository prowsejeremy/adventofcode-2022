with open ("data.txt", "r") as dataFile:
  rawData = dataFile.read().splitlines()

currentPath = ["/"]
directories = {}

totalSpaceAvailable = 70000000
minimumAvailableSpace = 30000000

# #########################
# Process the command...
# #########################

def handleCommand():
  global currentPath
  
  # NEW COMMAND
  # HANDLE CHANGING DIRECTORIES
  if splitLine[1] == "cd":
    newLocation = splitLine[2]
    
    if newLocation == "..":
      currentPath.pop()
    elif newLocation == "/":
      currentPath = ["/"]
    else:
      currentPath.append(newLocation)
      newDir = '/'.join(currentPath)
      if not directories.get(newDir):
        directories[newDir] = 0

# #########################
# Loop the Data...
# #########################

for line in rawData:
  splitLine = line.split()
  
  # New command
  if splitLine[0] == "$":
    handleCommand()
    continue
  elif splitLine[0] != "dir":
    # we have a file!
    fileSize = int(splitLine[0])
    totalSpaceAvailable -= fileSize

    for i in range(len(currentPath)):
      dir = '/'.join(currentPath[0:len(currentPath)-i])

      if dir in directories:
        directories[dir] += fileSize


# #################################################
# Find best directory for deletion
# #################################################

spaceToFind = minimumAvailableSpace - totalSpaceAvailable
bestDirsForDeletion = []

for directory in directories:
  if directories[directory] >= spaceToFind:
    bestDirsForDeletion.append(directories[directory])

bestDirForDeletion = min(bestDirsForDeletion)

print('bestDirForDeletion', bestDirForDeletion)