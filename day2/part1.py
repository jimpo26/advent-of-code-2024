with open("input.txt", "r") as f:
    data = f.read().splitlines()

total = 0
for line in data:
    values = [int(x) for x in line.split(" ")]
    ok = True
    is_increasing = -1

    for i in range(len(values) - 1):
        if abs(values[i] - values[i+1]) > 3 or abs(values[i] - values[i+1]) < 1:
            ok = False
            break

        if values[i] - values[i+1] < 0:
            if is_increasing == 1:
                ok = False
                break
            is_increasing = 0
        elif values[i] - values[i+1] > 0:
            if is_increasing == 0:
                ok = False
                break
            is_increasing = 1

    if ok:
        print(values)
        total += 1

print(total)

