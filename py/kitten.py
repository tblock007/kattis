k = int(input())
parent = [-1] * 101
while True:
    parsed = [int(w) for w in input().split()]
    if parsed[0] == -1:
        break
    for node in parsed[1:]:
        parent[node] = parsed[0]
path = []
while k != -1:
    path.append(k)
    k = parent[k]
print(*path)

