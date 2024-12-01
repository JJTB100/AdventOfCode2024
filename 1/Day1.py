f = open("1/input.txt")
input = f.readlines()
firstList = []
secondList = []

for i in range(len(input)):
    firstList.append(int(input[i][0:5]))
    secondList.append(int(input[i][-6:-1]))

firstList.sort()
secondList.sort()

total=0
for i in range(len(firstList)):
    sim = 0
    for j in range(len(secondList)):
        if secondList[j] == firstList[i]:
            sim += 1
    total += firstList[i] * sim
    

print(total)