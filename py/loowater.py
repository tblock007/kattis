while True:
    n, m = [int(w) for w in input().split()]
    if n == 0 and m == 0:
        break
    
    h = sorted(int(input()) for i in range(n))
    k = sorted(int(input()) for i in range(m))     

    possible = True
    cost = 0
    ki = 0
    for head in h:
        # get the smallest available knight that can chop
        while (ki < len(k) and k[ki] < head):
            ki = ki + 1
        if (ki == len(k)):
            possible = False
            break
        cost = cost + k[ki]
        ki = ki + 1

    if possible:
        print(cost)
    else:
        print('Loowater is doomed!')
