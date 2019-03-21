from heapq import heappush, heappop, nsmallest

n, k = [int(w) for w in input().split()]
bestA, bestD, bestH = [], [], []
for index in range(n):
    a, d, h = [int(w) for w in input().split()]
    heappush(bestA, (-1 * a, index))
    heappush(bestD, (-1 * d, index))
    heappush(bestH, (-1 * h, index))

team = []
for _ in range(k):
    team.append(heappop(bestA)[1])
    team.append(heappop(bestD)[1])
    team.append(heappop(bestH)[1])

print(len(set(team)))
