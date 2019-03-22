def pm(g):
    result = ''.join([(''.join(r)) for r in g])
    print('invalid grille' if ('#' in result) else result)

def rotate(gr):
    return [[gr[len(gr) - j - 1][i] for j in range(len(gr))] for i in range(len(gr))]

def fill(m, gr, ch):
    for i in range(len(gr)):
        for j in range(len(gr)):
            if (gr[i][j] == '.'):
                m[i][j] = ch[0]
                ch[:] = ch[1:] if len(ch) > 1 else ['#']

n = int(input())
message = [['#' for i in range(n)] for j in range(n)]
grill = [list(input()) for i in range(n)]
characters = list(input())

for i in range(4):
    fill(message, grill, characters)
    grill = rotate(grill)

pm(message)