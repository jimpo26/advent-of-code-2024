import re

with open("input.txt", "r") as f:
    data = f.read().splitlines()


total = 0
line = "".join(data)
for match in re.finditer(r"(?<=do\(\))(.*?)(?=(?:don't\(\)))", "do()"+line+"don't()"):
    for mul in re.finditer(r"mul\(([0-9]+),([0-9]+)\)", match.group(1)):
        total += int(mul.group(1)) * int(mul.group(2))

print(total)
