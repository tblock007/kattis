input()
valid = [int(b) for b in input().split() if int(b) != -1]
print(sum(valid) / len(valid))