n = int(input())
s = input()
total = 0
count = 0
for x in s:
    if x == "U":
        total += 1
        if total == 0:
            count += 1
    else:
        total -= 1
print(count)
