from itertools import permutations

with open("input.txt", "r") as f:
    data = f.read().splitlines()


def calculate_antinodes(p, nodes=None):
    if nodes is None:
        nodes = []
    diff_x, diff_y = abs(p[0][0] - p[1][0]), abs(p[0][1] - p[1][1])
    if p[0][0] < 0 or p[0][0] > len(data) or p[0][1] < 0 or p[0][1] > len(data[0]):
        return nodes

    if p[0][0] < p[1][0] and p[0][1] > p[1][1]:
        nodes.append((p[0][0] - diff_x, p[0][1] + diff_y))
    elif p[0][0] < p[1][0] and p[0][1] < p[1][1]:
        nodes.append((p[0][0] - diff_x, p[0][1] - diff_y))
    elif p[0][0] > p[1][0] and p[0][1] < p[1][1]:
        nodes.append((p[0][0] + diff_x, p[0][1] - diff_y))
    elif p[0][0] > p[1][0] and p[0][1] > p[1][1]:
        nodes.append((p[0][0] + diff_x, p[0][1] + diff_y))
    elif p[0][0] < p[1][0] and p[0][1] == p[1][1]:
        nodes.append((p[0][0] - diff_x, p[0][1]))
    elif p[0][0] > p[1][0] and p[0][1] == p[1][1]:
        nodes.append((p[0][0] + diff_x, p[0][1]))
    elif p[0][0] == p[1][0] and p[0][1] < p[1][1]:
        nodes.append((p[0][0], p[0][1] - diff_y))
    elif p[0][0] == p[1][0] and p[0][1] > p[1][1]:
        nodes.append((p[0][0], p[0][1] + diff_y))
    return calculate_antinodes((nodes[-1], p[0]), nodes)



locations = {}


def calculate_locations():
    global locations
    locations = {}
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if not c.isalnum():
                continue
            if c not in locations:
                locations[c] = []
            locations[c].append((i, j))
            s = list(data[i])
            s[j] = "."
            data[i] = "".join(s)


total = 0
unique = set()
not_unique = []

def do():
    global total
    calculate_locations()
    for k, v in locations.items():
        for pair in permutations(v, 2):
            antinodes = calculate_antinodes(pair)
            for antinode in antinodes:
                if 0 <= antinode[0] < len(data) and 0 <= antinode[1] < len(data[0]):
                    before = len(unique)
                    unique.add(antinode)
                    not_unique.append(antinode)
                    if len(unique) != before:
                        total += 1
                    s = list(data[antinode[0]])
                    s[antinode[1]] = k
                    data[antinode[0]] = "".join(s)


do()
for v in locations.values():
    for n in v:
        unique.add(n)
print(len(unique))
