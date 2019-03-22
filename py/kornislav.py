# let walks be l0, l1, l2, l3
# rectangle is enclosed only if l1 <= l3
#                   and only if l2 <= l0
import itertools
l = [int(w) for w in input().split()]
maxarea = -1
for walk in itertools.permutations(l):
    if walk[1] > walk[3] or walk[2] > walk[0]:
        continue
    else:
        maxarea = max(maxarea, walk[1] * walk[2])
print(maxarea)