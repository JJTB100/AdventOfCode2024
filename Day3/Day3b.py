import re
lines = open("input.txt", "r").read()

reg = re.findall("(mul)\((\d+),(\d+)\)", lines)

total = 0
for match in reg:
        total += int(match[1]) * int(match[2])

print(total)
