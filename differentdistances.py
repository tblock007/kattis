while True:
    line = input()
    if line == '0': break
    x1, y1, x2, y2, p = [float(w) for w in line.split()]
    print((abs(x2 - x1) ** p + abs(y2 - y1) ** p) ** (1.0 / p))