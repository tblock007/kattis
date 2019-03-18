def solvePoint(w, h, x0, y0):
    diff = x0 - y0
    g, s, t = exEuclid(w, h)
    if diff % g != 0:
        return -1
    s1, t1 = (diff // g) * s, (diff // g) * t
    cs, ct = (h // g), (w // g)
    r = (s1 - 1) // cs
    nw, nh = s1 - cs * r, - t1 - ct * r
    return (nw * w - x0)


def exEuclid(a, b):
    r0, r1 = a, b
    s0, s1, t0, t1 = 1, 0, 0, 1
    while r1 != 0:
        q = r0 // r1
        r0 -= q * r1
        r0, r1 = r1, r0
        s0 -= q * s1
        s0, s1 = s1, s0
        t0 -= q * t1
        t0, t1 = t1, t0
    return (r0, s0, t0)

t = int(input())
for _ in range(t):
    ws, hs, wl, hl, xl, yl = [int(w) for w in input().split()]
    if (xl == 0 and yl == 0) or (xl + wl == ws and yl == 0) or (xl == 0 and yl + hl == hs) or (xl + wl == ws and yl + hl == hs):
        print(0)
        continue

    weff, heff = ws - wl, hs - hl
    time = solvePoint(weff, heff, xl, yl)    
    print('Johnny will die waiting' if time == -1 else time)
