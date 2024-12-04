with open("input.txt", "r") as f:
    data = f.readlines()

l1, l2 = [], []
for l in data:
    a, b = l.split("   ")
    l1.append(a)
    l2.append(b)

    l1.sort()
    l2.sort()

total = 0
for i in range(len(l1)):
    total += abs(int(l1[i]) - int(l2[i]))

print(total)
