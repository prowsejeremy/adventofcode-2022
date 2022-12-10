with open ("data.txt", "r") as dataFile:
  rawData = dataFile.read().splitlines()

total = 0

for pair in rawData:

  pairs = pair.split(',')
  pairOne = pairs[0].split('-')
  pairTwo = pairs[1].split('-')

  a = int(pairOne[0])
  b = int(pairOne[1])
  c = int(pairTwo[0])
  d = int(pairTwo[1])

  if (
    (
      (c <= a <= d)
    and
      (c <= b <= d)
    )
  or
    (
      (a <= c <= b)
      and
      (a <= d <= b)
    )
  ):
    total += 1

print("///////////// TOTAL /////////////")
print(total)