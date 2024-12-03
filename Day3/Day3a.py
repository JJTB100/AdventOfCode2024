import re
lines = open("input.txt", "r").read()

reg = re.findall("(mul)\((\d+),(\d+)\)|(do\(\))|(don't\(\))", lines)

total = 0
going = True
for match in reg:
    if match[3] == "do()":
        going = True
    elif match[4] == "don't()":
        going = False
    elif going:
        total += int(match[1]) * int(match[2])

print(total)
