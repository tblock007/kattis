x = [int(w) for w in input().split()]
while x != [1, 2, 3, 4, 5]:
    for i in range(4):
        if x[i] > x[i + 1]:
            x[i], x[i + 1] = x[i + 1], x[i]
            print(' '.join(str(i) for i in x))