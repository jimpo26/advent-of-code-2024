with open("input.txt", "r") as f:
    order, pages = f.read().split("\n\n")

order = order.splitlines()
d = dict()
d1 = dict()

for rule in order:
    a, b = rule.split("|")
    if a not in d:
        d[a] = []
    d[a].append(b)

    if b not in d1:
        d1[b] = []
    d1[b].append(a)

total = 0
for line in pages.splitlines():
    keep = True
    values = line.split(",")
    for i in range(len(values)):
        if values[i] in d:
            for j in range(i + 1, len(values)):
                if values[j] in d[values[i]]:
                    keep = True
                else:
                    keep = False
                    break
        else:
            keep = True

        if not keep:
            break

        if values[i] in d1:
            for j in range(len(d1[values[i]])):
                if d1[values[i]][j] in values[i + 1:]:
                    keep = False
                    break

        if not keep:
            break
    if keep:
        total += int(values[(len(values) - 1) // 2])

print(total)
