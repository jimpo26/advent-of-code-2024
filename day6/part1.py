with open("input.txt", "r") as f:
    matrix = f.read().splitlines()

for i in range(len(matrix)):
    matrix[i] = list(matrix[i])

directions = {
    "N": [-1, 0],
    "S": [1, 0],
    "W": [0, -1],
    "E": [0, 1]
}

next_direction = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N"
}

direction_start_mapping = {
    "^": "N",
    ">": "E",
    "v": "S",
    "<": "W"
}
x = set()


def move(m, d, ii, jj, t=0):
    while True:
        ii = ii + directions[d][0]
        jj = jj + directions[d][1]
        if ii < 0 or ii >= len(m) or jj < 0 or jj >= len(m[ii]):
            return t
        if m[ii][jj] == "#":
            return move(m, next_direction[d], ii - directions[d][0], jj - directions[d][1], t)
        m[ii][jj] = "X"
        x.add((ii, jj))
        t += 1


for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] in ["^", ">", "v", "<"]:
            move(matrix, direction_start_mapping[matrix[i][j]], i, j, 1)
            break
print(len(x))
