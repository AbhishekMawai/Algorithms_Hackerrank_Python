n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
count = 0


def find(li, d):
    if len(li) < 2:
        if li[0] == d:
            return True
        else:
            return False
    else:
        middle = len(li) // 2
        if li[middle] == d:
            return True
        elif li[middle - 1] >= d:
            return find(li[:middle], d)
        else:
            return find(li[middle:], d)


for x in range(n - 2):
    if find(arr[x:], k + arr[x]):
        if find(arr[x + 1:], 2 * k + arr[x]):
            count += 1
print(count)
