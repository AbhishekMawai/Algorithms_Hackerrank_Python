size = int(input())
A = list(map(int, input().strip().split()))
shifts = 0
for j in range(1, size):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i = i - 1
        A[i + 1] = key
    shifts = shifts + j - (i + 1)
print(shifts)
