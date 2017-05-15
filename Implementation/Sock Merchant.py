n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
s = set(c)
count = 0
for x in s:
    d = c.count(x)
    count += d // 2
print(count)
