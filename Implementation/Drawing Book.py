n = int(input().strip())
p = int(input().strip())
count = 0
for i in range(1, p, 2):
    count += 1
count1 = 0
for j in range(n, p - 1, -2):
        count1 += 1
if count1 != 0:
    count1 = count1 - 1
print(min(count, count1))
