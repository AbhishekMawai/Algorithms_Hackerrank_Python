n = int(input())
for i in range(n):
    count = 0
    s = input()
    for x in range(1, len(s)):
        if s[x] == s[x - 1]:
            count += 1
    print(count)
