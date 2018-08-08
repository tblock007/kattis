cas = 1
while True:
    n = int(input())
    if n == 0: break
    print('List {0}:'.format(cas))
    cas = cas + 1

    animals = dict()
    for i in range(n):
        tokens = input().split()
        animal = tokens[-1].lower()
        if animal in animals.keys():
            animals[animal] += 1
        else:
            animals[animal] = 1
    for k in sorted(animals.keys()):
        print('{0} | {1}'.format(k, animals[k]))
