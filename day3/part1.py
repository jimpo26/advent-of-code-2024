import re

with open("input.txt", "r") as f:
    data = f.read().splitlines()


total = 0
for line in data:
    for match in re.finditer(r"mul\(([0-9]+),([0-9]+)\)", line):
        total += int(match.group(1)) * int(match.group(2))

print(total)
