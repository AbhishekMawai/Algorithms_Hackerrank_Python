def getWays(squares, d, m):
    count = 0
    for i in range(n - m + 1):
        if sum(squares[i:i + m]) == d:
            count += 1
    return count


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = getWays(s, d, m)
print(result)
