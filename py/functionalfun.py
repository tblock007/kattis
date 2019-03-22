while True:
    try:
        line = input()
    except:
        break
    inputs = line.split()[1:]
    outputs = input().split()[1:]
    n = int(input())
    f, invf, outputs_covered = dict(), dict(), set()
    function, injective, surjective = True, True, False
    
    for i in range(n):
        a, arrow, b = input().split()
        outputs_covered.add(b)
        if a in f.keys():
            function = False
        if b in invf.keys():
            injective = False
        f[a] = b
        invf[b] = a
    if len(outputs_covered) == len(outputs):
        surjective = True
    
    if not function:
        print('not a function')
    elif injective and surjective:
        print('bijective')
    elif injective:
        print('injective')
    elif surjective:
        print('surjective')
    else:
        print('neither injective nor surjective')
    
