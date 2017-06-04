s = input().strip()
count = 1
for x in s:
    if x.isupper():
        count += 1
print(count)
