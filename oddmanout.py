n = int(input())
for i in range(n):
    g = int(input())
    guests = set()
    for w in input().split():
        if int(w) in guests:
            guests.remove(int(w))
        else:
            guests.add(int(w))
    print('Case #{0}: {1}'.format(i + 1, list(guests)[0]))