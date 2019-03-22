from heapq import heappush, heappop, nsmallest

# Read first line
n, k = [int(w) for w in input().split()]

# Create three lists that will be used as "heaps"
# https://en.wikipedia.org/wiki/Binary_heap
bestA, bestD, bestH = [], [], []

# Read in each pokenom and store (stat, index) pairs 
# in the corresponding heap.
# Note that we store the NEGATIVE of the stat here.
# This is a small trick used because the default heap 
# is a "min-heap", so the smallest element is always on 
# top.  If we store the negatives of the stat, then this 
# actually gives the largest stat, as desired.
for index in range(n):
    a, d, h = [int(w) for w in input().split()]
    heappush(bestA, (-1 * a, index))
    heappush(bestD, (-1 * d, index))
    heappush(bestH, (-1 * h, index))

# After all (stat, index) pairs are stored in the heaps, 
# we simply need to extract the top k from each heap.
# Here, we will naively throw them into the list, without 
# worrying about duplicates.
# Remember that the heaps store (stat, index) pairs.  We 
# only care about the index, so after popping off the pair, 
# we only throw the index, located at [1], into the team list.
team = []
for _ in range(k):
    team.append(heappop(bestA)[1])
    team.append(heappop(bestD)[1])
    team.append(heappop(bestH)[1])

# Converting team to a set here handles duplicates.
print(len(set(team)))
