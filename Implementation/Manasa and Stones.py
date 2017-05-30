t = int(input())
for x in range(t):
    n = int(input())
    a = int(input())
    b = int(input())
    diff = abs(a - b)
    ans = min(a, b) * (n - 1)
    li = []
    while ans <= max(a, b) * (n - 1):
        li.append(ans)
        if diff != 0:
            ans += diff
        else:
            break
    print(*li)
