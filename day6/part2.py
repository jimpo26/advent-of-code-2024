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


def move(m, d, ii, jj, t=0):
    while True:
        ii = ii + directions[d][0]
        jj = jj + directions[d][1]
        if ii < 0 or ii >= len(m) or jj < 0 or jj >= len(m[ii]):
            return t
        if m[ii][jj] == "#":
            return move(m, next_direction[d], ii - directions[d][0], jj - directions[d][1], t)
        t += 1


ok = 0
x, y = 0, 0
for k in range(len(matrix)):
    for l in range(len(matrix)):
        if matrix[k][l] == ".":
            matrix[k][l] = "#"
            x = k
            y = l
        b = False
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] in ["^", ">", "v", "<"]:
                    try:
                        move(matrix, direction_start_mapping[matrix[i][j]], i, j, 1)
                    except:
                        ok += 1
                    b = True
                    break
            if b:
                break
        if k == x and l == y:
            matrix[k][l] = "."
    print("doing line ", k)

# why not brute-forcing it all?
print(ok)
