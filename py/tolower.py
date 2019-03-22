p, t = [int(w) for w in input().split()]
count = 0
for i in range(p):
    valid = True
    for j in range(t):
        line = input()
        if not line[1:].islower():
            valid = False
    if valid:
        count = count + 1
print(count)