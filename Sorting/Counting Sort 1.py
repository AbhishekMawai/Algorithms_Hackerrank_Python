out = []
temp = []
k = 99   # Update with largest element in the range of input
temp = [0] * (k + 1)
n = int(input().strip())
out = [0] * (n)
li = list(map(int, input().strip().split()))
for b in range(0, len(li)):
    temp[li[b]] = temp[li[b]] + 1
print(*temp, sep=" ")
