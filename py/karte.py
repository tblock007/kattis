def parse(line):
    p, k, h, t = set(), set(), set(), set()
    for i in range(0, len(line), 3):
        if line[i] == 'P':
            if int(line[i + 1:i + 3]) in p:
                return 'GRESKA'
            p.add(int(line[i + 1:i + 3]))
        elif line[i] == 'K':            
            if int(line[i + 1:i + 3]) in k:
                return 'GRESKA'
            k.add(int(line[i + 1:i + 3]))
        elif line[i] == 'H':            
            if int(line[i + 1:i + 3]) in h:
                return 'GRESKA'
            h.add(int(line[i + 1:i + 3]))
        elif line[i] == 'T':
            if int(line[i + 1:i + 3]) in t:
                return 'GRESKA'
            t.add(int(line[i + 1:i + 3]))
    return '{0} {1} {2} {3}'.format(13 - len(p), 13 - len(k), 13 - len(h), 13 - len(t))



line = input()
print(parse(line))
