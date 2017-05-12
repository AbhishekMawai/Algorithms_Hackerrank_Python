n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
count = [0] * 6
for x in types:
    count[x] += 1
ma = max(count)
for x in range(6):
    if count[x] == ma:
        print(x)
