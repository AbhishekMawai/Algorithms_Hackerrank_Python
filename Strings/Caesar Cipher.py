n = int(input().strip())
s_copy = input().strip()
s = s_copy.lower()
k = int(input().strip()) % 26
res = []
for x in s:
    if x.isalpha():
        num = ord(x) + k
        if num > 122:
            res.append(chr(num - 26))
        else:
            res.append(chr(num))
    else:
        res.append(x)
for i in range(n):
    if s_copy[i].isupper():
        res[i] = res[i].upper()
print("".join(res))
