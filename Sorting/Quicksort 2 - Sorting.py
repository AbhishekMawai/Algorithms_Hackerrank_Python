N = int(input())
li = list(map(int, input().split()))
ans = []


def Partition(A):
    x = A[0]
    left = []
    right = []
    for j in range(1, len(A)):
        if A[j] < x:
            left.append(A[j])
        else:
            right.append(A[j])
    if len(left) > 1:
        left = Partition(left)
        print(*left)
    if len(right) > 1:
        right = Partition(right)
        print(*right)
    return left + [x] + right


print(*Partition(li))
