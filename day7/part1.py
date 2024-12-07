from itertools import product

with open("input.txt", "r") as f:
    data = f.read().splitlines()

total = 0
c = 0
for line in data:
    c += 1
    test, values = line.split(":")
    test = int(test)
    values = values.strip().split(" ")

    for combination in product(*(['+*'] * (len(values) - 1))):
        res = int(values[0])
        for i in range(len(combination)):
            match combination[i]:
                case '+':
                    res += int(values[i+1])
                case '*':
                    res *= int(values[i+1])
        if res == test:
            total += test
            break
    print("doing line", c)

print(total)