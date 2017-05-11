n = int(input().strip())
li = [int(input().strip().split()[0]) for x in range(n)]
k = 99  # Update with largest element in the range of input
out = [0] * n
temp = [0] * (k + 1)
for b in range(0, len(li)):
    temp[li[b]] = temp[li[b]] + 1
for c in range(1, k + 1):
    temp[c] = temp[c] + temp[c - 1]
print(*temp)
