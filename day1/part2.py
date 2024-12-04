with open("input.txt", "r") as f:
    data = f.read().splitlines()

l1, l2 = [], []
for line in data:
    a, b = line.split("   ")
    l1.append(a)
    l2.append(b)

total = 0
for val in l1:
    total += int(val) * l2.count(val)

print(total)