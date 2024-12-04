with open("input.txt", "r") as f:
    data = f.read().splitlines()

valid = {
    "M.S.A.M.S": 1,
    "M.M.A.S.S": 1,
    "S.M.A.S.M": 1,
    "S.S.A.M.M": 1
}


def search(m, ii, jj):
    s = [*m[ii][jj:jj + 3], *m[ii + 1][jj:jj + 3], *m[ii + 2][jj:jj + 3]]
    print(s)
    s[1] = "."
    s[3] = "."
    s[5] = "."
    s[7] = "."
    return valid.get("".join(s), 0)

total = 0
for i in range(len(data) - 2):
    for j in range(len(data[i]) - 2):
        total += search(data, i, j)

print(total)
