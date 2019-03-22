from sys import stdin

def jolly(seq):
    jumps = set()
    l = len(seq)
    for i in range(l - 1):
        j = abs(seq[i + 1] - seq[i])
        if (j < 1 or j >= l):
            return False
        jumps.add(j)
    if len(jumps) == l - 1:
        return True
    return False

for line in stdin.readlines():
    seq = [int(w) for w in line.split()[1:]]
    print('Jolly' if jolly(seq) else 'Not Jolly')