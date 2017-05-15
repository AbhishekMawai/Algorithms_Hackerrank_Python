n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
temp = [0] * 100
for x in a:
    temp[x] += 1
max = 0
for i in range(n - 1):
    if temp[i] + temp[i + 1] > max:
        max = temp[i] + temp[i + 1]
print(max)
