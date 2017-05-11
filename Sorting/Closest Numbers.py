import math
n = int(input())
li = [int(x) for x in input().strip().split()]
li.sort()
mini = math.inf
d = {}
for x in range(n - 1):
    y = x + 1
    lj = []
    mini = li[y] - li[x]
    lj.append((li[x], li[y]))
    if mini in d:
            d.get(mini).append(*lj)
    else:
            d[mini] = lj
for e in d.get(min(d)):
    print(*e, end=" ")
