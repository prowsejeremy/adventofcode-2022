with open ("data.txt", "r") as dataFile:
  rawData = dataFile.read().splitlines()

currentPath = ["/"]
directories = {}

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

    for i in range(len(currentPath)):
      dir = '/'.join(currentPath[0:len(currentPath)-i])

      if dir in directories:
        directories[dir] += fileSize


# #################################################
# Process the total of directories <= 100,000
# #################################################

totalOfDirectoriesUnder100k = 0
targetSize = 100000

for directory in directories:
  if directories[directory] <= targetSize:
    totalOfDirectoriesUnder100k += directories[directory]

print('totalOfDirectoriesUnder100k', totalOfDirectoriesUnder100k)