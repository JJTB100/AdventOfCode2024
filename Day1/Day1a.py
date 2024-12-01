
with open("Day1/input.txt") as f:
    input = f.readlines()

firstList = [int(line[:5]) for line in input]
secondList = [int(line[-6:-1]) for line in input]

firstList.sort()
secondList.sort()

total = 0
for i in range(len(firstList)):
    total += abs(firstList[i]-secondList[i])

print(total)
