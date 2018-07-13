g = sum(int(w) for w in input().split())
e = sum(int(w) for w in input().split())
if (g > e):
    print('Gunnar')
elif (e > g):
    print('Emma')
else:
    print('Tie')