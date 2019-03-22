def count(t, sa, ea, sb, eb, sc, ec):
    result = 0
    if t > sa and t <= ea: result = result + 1
    if t > sb and t <= eb: result = result + 1
    if t > sc and t <= ec: result = result + 1
    return result

cost = [int(w) for w in input().split()]
sa, ea = [int(w) for w in input().split()]
sb, eb = [int(w) for w in input().split()]
sc, ec = [int(w) for w in input().split()]

total = 0
for t in range(1, 101):
    c = count(t, sa, ea, sb, eb, sc, ec)
    if (c > 0):
        total = total + c * (cost[c - 1])
print(total)