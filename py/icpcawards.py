n = int(input())
unis = set()
for i in range(n):
    uni, team = [w for w in input().split()]
    if uni not in unis:
        unis.add(uni)
        print('{0} {1}'.format(uni, team))
    if (len(unis) == 12):
        break
