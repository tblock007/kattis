from sys import stdin

pairs = [['A#', 'Bb'], ['C#', 'Db'], ['D#', 'Eb'], ['F#', 'Gb'], ['G#', 'Ab']]
alt = {}
for pair in pairs:
    alt[pair[0]] = pair[1]
    alt[pair[1]] = pair[0]
lines = stdin.readlines()
cas = 1
for line in lines:
    note, key = line.split()
    if note in alt.keys():
        ans = '{0} {1}'.format(alt[note], key)
    else:
        ans = 'UNIQUE'
    print('Case {0}: {1}'.format(cas, ans))
    cas += 1
