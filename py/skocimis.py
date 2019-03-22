a, b, c = [int(w) for w in input().split()]
print(max(c - b - 1, b - a - 1))