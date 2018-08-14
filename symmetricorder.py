cas = 1
while True:
    n = int(input())
    if n == 0: break
    print('SET {0}'.format(cas))
    names = [input() for i in range(n)]
    for e in range(0, len(names), 2):
        print(names[e])
    for o in reversed(range(1, len(names), 2)):
        print(names[o])
    cas += 1