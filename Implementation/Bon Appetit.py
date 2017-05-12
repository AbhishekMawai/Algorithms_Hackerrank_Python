n, k = [int(x) for x in input().split()]
cost = list(map(int, input().split()))
charged = int(input())


def mean(m):
    return sum(m) / 2


if charged == mean(cost) - cost[k] / 2:
    print("Bon Appetit")
else:
    print(cost[k] // 2)
