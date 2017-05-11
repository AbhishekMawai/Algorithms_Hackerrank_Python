n = int(input().strip())
li = list(map(int, input().strip().split()))
out = []
temp = []
k = 99  # Update with largest element in the range of input
temp = [0] * (k + 1)
out = [0] * (n)
for b in range(0, len(li)):
    temp[li[b]] = temp[li[b]] + 1
for c in range(1, k + 1):
    temp[c] = temp[c] + temp[c - 1]
for d in range(len(li) - 1, -1, -1):
    out[temp[li[d]] - 1] = li[d]  # Reduce index by 1 in out list.
    temp[li[d]] -= 1
print(*out, sep=" ")
