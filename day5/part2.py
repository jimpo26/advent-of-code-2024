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
incorrects = []


def perform(arr, replace=True):
    err = []
    global total
    for line in arr:
        keep = True
        values = line.split(",")
        for i in range(len(values)):
            if values[i] in d:
                for j in range(i + 1, len(values)):
                    # controllo che values[j] venga prima di quelli che DEVONO venire dopo rispetto a lui
                    if values[j] in d[values[i]]:
                        keep = True
                    else:
                        if replace:
                            tmp = values[j]
                            values[j] = values[i]
                            values[i] = tmp
                        keep = False
                        break
            else:
                keep = True

            if not keep:
                break
        if keep:
            total += int(values[(len(values) - 1) // 2])
        else:
            err.append(",".join(values))
    return err


incorrects = perform(pages.splitlines())
total = 0
while len(incorrects) > 0:
    res = perform(incorrects, True)
    incorrects = res.copy()
print(total)

# that's funny because in the example input there is an edge case that is not present in the real input lol
