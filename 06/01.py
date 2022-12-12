with open ("data.txt", "r") as dataFile:
  rawData = dataFile.read()

characterList = ""
characterIndex = 0

for idx, character in enumerate(rawData):
  if character in characterList:
    characterList = characterList[characterList.index(character)+1:]
  
  characterList += character
  
  if len(characterList) == 4:
    characterIndex = idx + 1
    break

print("//////////// CHARACTER INDEX ////////////")
print(characterList, characterIndex)

# #################
# SET SOLUTION
# #################

# with open ("data.txt", "r") as dataFile:
#   s = dataFile.read()

# def check(s, n):
#   for i in range(len(s)):
#     if len(set(s[i:i+n])) == n:
#       return i+n

# print(check(s, 4))