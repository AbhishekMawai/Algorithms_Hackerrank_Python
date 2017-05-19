t = int(input().strip())
for x in range(t):
    n, m, s = [int(x) for x in input().strip().split()]
    ans = ((s + m) % n) - 1
    if ans <= 0:
        print(n + ans)
    else:
        print(ans)
