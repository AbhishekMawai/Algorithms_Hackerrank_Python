n = int(input().strip())
count = 0
m = 5
for x in range(n):
    count += m // 2
    m = (m // 2) * 3
print(count)
