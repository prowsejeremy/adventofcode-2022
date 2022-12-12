with open ("data.txt", "r") as dataFile:
  rawData = dataFile.read()

characterList = ""
characterIndex = 0

for idx, character in enumerate(rawData):
  if character in characterList:
    characterList = characterList[characterList.index(character)+1:]
  
  characterList += character
  
  if len(characterList) == 14:
    # Not a 0 based index system for some reason
    characterIndex = idx + 1
    break

print("//////////// CHARACTER INDEX ////////////")
print(characterList, characterIndex)