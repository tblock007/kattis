t = int(input())
for cas in range(t):
    fs = input().split()
    
    sounds = []
    line = input()
    while (line != "what does the fox say?"):
        sounds.append(line.split()[2])
        line = input()
    
    ans = [s for s in fs if s not in sounds]
    print(' '.join(ans))