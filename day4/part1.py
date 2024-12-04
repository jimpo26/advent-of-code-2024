with open("input.txt", "r") as f:
    data = f.read().splitlines()

directions = {
    "N": [-1, 0],
    "S": [1, 0],
    "W": [0, -1],
    "E": [0, 1],
    "NE": [-1, 1],
    "NW": [-1, -1],
    "SW": [1, -1],
    "SE": [1, 1],
}
checks = {
    "X": "M",
    "M": "A",
    "A": "S",
    "S": None
}


def perform_search(m, ii, jj, check="M", d=None):
    if check is None:
        return 1
    found = 0
    if d is None:
        for k, v in directions.items():
            if ii + v[0] < 0 or jj + v[1] < 0 or ii + v[0] >= len(m) or jj + v[1] >= len(m[0]):
                continue
            if m[ii + v[0]][jj + v[1]] == check:
                found += perform_search(m, ii + v[0], jj + v[1], check=checks[check], d=k)
    else:
        if ii + directions[d][0] < 0 or jj + directions[d][1] < 0 or ii + directions[d][0] >= len(m) or jj + directions[d][1] >= len(m[0]):
            return 0
        if m[ii + directions[d][0]][jj + directions[d][1]] == check:
            return perform_search(m, ii + directions[d][0], jj + directions[d][1], check=checks[check], d=d)
    return found


total = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "X":
            total += perform_search(data, i, j)

print(total)
