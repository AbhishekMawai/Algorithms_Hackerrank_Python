import math
t = int(input())
for x in range(t):
    a, b = [int(y) for y in input().strip().split()]
    count = 0
    start = int(math.sqrt(a))
    if start * start == a:
        count += 1
        start += 1
    else:
        start += 1
    while start * start <= b:
        count += 1
        start = start + 1
    print(count)
