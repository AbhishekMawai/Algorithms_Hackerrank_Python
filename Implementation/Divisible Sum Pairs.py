n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
count = 0
for x in range(n - 1):
    for y in range(x + 1, n):
        if (a[x] + a[y]) % k == 0:
            count += 1
print(count)
