with open("input.txt", "r") as f:
    data = f.read().splitlines()


def try_auto_adjusting(v, idx):
    return [*v[:idx], *v[idx+1:]]


def calculate(values):
    ok = True
    is_increasing = -1

    for i in range(len(values) - 1):
        if abs(values[i] - values[i + 1]) > 3 or abs(values[i] - values[i + 1]) < 1:
            ok = False
            break

        if values[i] - values[i + 1] < 0:
            if is_increasing == 1:
                ok = False
                break
            is_increasing = 0
        elif values[i] - values[i + 1] > 0:
            if is_increasing == 0:
                ok = False
                break
            is_increasing = 1

    return ok


total = 0
for line in data:
    v1 = [int(x) for x in line.split(" ")]
    r = calculate(v1)

    if r:
        print(v1)
        total += 1
        continue

    ii = 0
    while ii < len(v1):
        n = try_auto_adjusting(v1, ii)
        r = calculate(n)
        if r:
            print(v1)
            total += 1
            break
        ii += 1


print(total)