n = int(input().strip())
li = list(map(int, input().strip().split()))
lj = list(li)
countq = 0


def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
            global countq
            countq += 1
    A[i + 1], A[r] = A[r], A[i + 1]
    countq += 1
    return i + 1


def Quicksort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        Quicksort(A, p, q - 1)
        Quicksort(A, q + 1, r)


Quicksort(li, 0, len(li) - 1)
shifts = 0
for j in range(1, n):
    key = lj[j]
    i = j - 1
    while i >= 0 and lj[i] > key:
        lj[i + 1] = lj[i]
        i = i - 1
    lj[i + 1] = key
    shifts = shifts + j - (i + 1)
print(shifts - countq)
