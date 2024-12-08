from itertools import permutations, combinations

with open("input.txt", "r") as f:
    data = f.read().splitlines()

locations = {}
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if not c.isalnum():
            continue
        if c not in locations:
            locations[c] = []

        locations[c].append((i, j))

total = 0
unique = set()
for k, v in locations.items():
    for pair in permutations(v, 2):
        diff_x, diff_y = abs(pair[0][0] - pair[1][0]), abs(pair[0][1] - pair[1][1])
        antinode = (0,0)
        if pair[0][0] < pair[1][0] and pair[0][1] > pair[1][1]:
            antinode = (pair[0][0] - diff_x, pair[0][1] + diff_y)
        elif pair[0][0] < pair[1][0] and pair[0][1] < pair[1][1]:
            antinode = (pair[0][0] - diff_x, pair[0][1] - diff_y)
        elif pair[0][0] > pair[1][0] and pair[0][1] < pair[1][1]:
            antinode = (pair[0][0] + diff_x, pair[0][1] - diff_y)
        elif pair[0][0] > pair[1][0] and pair[0][1] > pair[1][1]:
            antinode = (pair[0][0] + diff_x, pair[0][1] + diff_y)

        if 0 <= antinode[0] < len(data) and 0 <= antinode[1] < len(data[0]):
            before = len(unique)
            unique.add(antinode)
            if len(unique) != before:
                total += 1
            if data[antinode[0]][antinode[1]] == '.':
                s = list(data[antinode[0]])
                s[antinode[1]] = "#"
                data[antinode[0]] = s

print(total)
for line in data:
    print("".join(line))