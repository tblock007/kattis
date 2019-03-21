class pokenom:
    def __init__(self, a, d, h):
        self.a, self.d, self.h = a, d, h

    # def __str__(self):
    #     return 'Attack: {0}, Defense: {1}, Health: {2}'.format(self.a, self.d, self.h)

    

n, k = [int(w) for w in input().split()]
box = []
for _ in range(n):
    a, d, h = [int(w) for w in input().split()]
    box.append(pokenom(a, d, h))

bestA = set(sorted(box, key = lambda p: p.a, reverse = True)[:k])
bestD = set(sorted(box, key = lambda p: p.d, reverse = True)[:k])
bestH = set(sorted(box, key = lambda p: p.h, reverse = True)[:k])

team = bestA | bestD | bestH
print(len(team))

# for p in bestA:
#     print(p)
# print()
# for p in bestD:
#     print(p)
# print()
# for p in bestH:
#     print(p)
# print()
