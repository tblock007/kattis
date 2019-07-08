t = int(input())
for _ in range(t):
    m, mi = -1, -1
    n = int(input())
    for i in range(n):
        a, b, c = [int(w) for w in input().split()]
        mt = b*b/4/a + c # some algebra or calculus tells us that this is the maximum torque that can be achieved
        if mt > m:
            m, mi = mt, (i + 1)
    print(mi)
