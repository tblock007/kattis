n = int(input())
c = sorted(int(w) for w in input().split())
ans = 2.0
for index, fill in enumerate(c):
    cap = index + 1
    if fill > cap:
        ans = -1.0
        break
    ans = min(ans, fill / cap)
print(ans if ans >= 0.0 else 'impossible')