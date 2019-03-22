n = int(input())
toks = input().split()
fishy = False
for i in range(n):
    if toks[i] != 'mumble':
        if int(toks[i]) != i + 1:
            fishy = True
            break
print('something is fishy' if fishy else 'makes sense')