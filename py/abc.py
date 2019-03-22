x = {}
x['A'], x['B'], x['C'] = sorted(int(w) for w in input().split())
o = input()
print(x[o[0]], x[o[1]], x[o[2]])