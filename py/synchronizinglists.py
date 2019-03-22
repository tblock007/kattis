first = True
while True:
    n = int(input())
    if n == 0: break
    if not first:
        print()
    else:
        first = False
    a = [int(input()) for i in range(n)]
    b = [int(input()) for i in range(n)]
    pairs = {key: value for (key, value) in zip(sorted(a), sorted(b))}
    for num in a:
        print(pairs[num])