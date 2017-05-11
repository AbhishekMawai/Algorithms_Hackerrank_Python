n = int(input().strip())
li = []
lj = []
for x in range(n // 2):
    li.append((int(input().strip().split()[0]), "-"))
for x in range(n // 2, n, 1):
        y = input().strip().split()
        li.append((int(y[0]), str(y[1])))
k = 99
out = [0] * n
temp = [0] * (k + 1)
for b in range(0, n):
    temp[li[b][0]] = temp[li[b][0]] + 1
for c in range(1, k + 1):
    temp[c] = temp[c] + temp[c - 1]
for q in range(n - 1, -1, -1):
    out[temp[li[q][0]] - 1] = li[q][1]
    temp[li[q][0]] -= 1
print(" ".join(out))
