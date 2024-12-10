with open("input.txt", "r") as f:
    data = list(f.read())

s = ""
ids = 0
idx = 0
arr = [None] * 100_000
for i in range(len(data)):
    data[i] = int(data[i])
    if i % 2 != 0:
        for j in range(data[i]):
            arr[idx] = "."
            idx += 1
    else:
        for j in range(data[i]):
            arr[idx] = str(ids)
            idx += 1
        ids += 1

arr = arr[:idx]
left = 0
for v in range(len(arr) - 1, -1, -1):
    if arr[v] == ".":
        continue

    while arr[left] != "." and left < v:
        left += 1
    arr[left] = arr[v]
    if left > v:
        break
    arr[v] = "."

checksum = 0
print(arr)
for i in range(len(arr)):
    if arr[i] == ".":
        break
    checksum += i * (int(arr[i]))
print(checksum)
