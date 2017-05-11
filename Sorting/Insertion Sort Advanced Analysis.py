t = int(input())
for x in range(t):
    n = int(input())
    li = list(map(int, input().strip().split()))
    countinv = 0

    def merge(left, right):
        result = []
        i, j = 0, 0
        lleft = len(left)
        lright = len(right)
        while i < lleft and j < lright:
            # This loop runs as long as both left and right arrays(lists) have elements
            if left[i] <= right[j]:
                result.append(left[i])
                i = i + 1
            else:
                result.append(right[j])
                j = j + 1
                global countinv    # counter for inversions
                countinv = countinv + len(left) - i
        result += left[i:]
        result += right[j:]
        return result

    def mergesort(A):
        if len(A) < 2:
            return A[:]
        else:
            middle = len(A) // 2
            left = mergesort(A[:middle])  # Calling recursively to store result returned from merge().
            right = mergesort(A[middle:])  # Calling recursively to store result returned from merge().
            return merge(left, right)
    mergesort(li)
    print(countinv)
