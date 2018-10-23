import sys
lines = sys.stdin.readlines()
r, n = [int(w) for w in lines[0].split()]
rooms = [int(w) for w in lines[1:]]
if n >= r:
    print('too late')
else:
    for i in range(1, 101):
        if i not in rooms:
            print(i)
            break