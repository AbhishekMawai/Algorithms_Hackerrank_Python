n = int(input())
px = [int(x) for x in input().split()]
for i in range(n):
    print(px.index(px.index(i + 1) + 1) + 1)
