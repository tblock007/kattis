from sys import stdin

for line in stdin.readlines():
    tokens = line.split()
    name = []
    bpm = []
    for token in tokens:
        try:
            bpm.append(float(token))
        except:
            name.append(token)
    print('{0} {1}'.format(sum(bpm) / len(bpm), ' '.join(name)))