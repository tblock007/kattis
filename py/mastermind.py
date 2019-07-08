from collections import Counter

nn, a, b = input().split()
n = int(nn)
r = 0
ca, cb = Counter(), Counter()

# make a pass through both strings, keeping track of the perfect 
# matches, and counting characters for non-matches
for i in range(n):
    if a[i] == b[i]:
        r += 1
    else:
        ca[a[i]] += 1
        cb[b[i]] += 1

# r is already computed, so we just need to compute s from the counts
# for every unmatched letter in the first string, if there are any 
# in the second string, add the minimum of the counts
s = sum(min(ca[c], cb[c]) for c in ca)

print('{0} {1}'.format(r, s))

