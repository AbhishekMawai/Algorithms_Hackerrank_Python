n = int(input())
li = [int(x) for x in input().strip().split()]


def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def Quicksort(A, p, r):
    if p == n // 2 and r == n // 2:
        return A[p]
    if p < r:
        q = Partition(A, p, r)
        if q == n // 2:
            return A[q]
        elif q > n // 2:
            return Quicksort(A, p, q - 1)
        else:
            return Quicksort(A, q + 1, r)

print(Quicksort(li, 0, len(li) - 1))
