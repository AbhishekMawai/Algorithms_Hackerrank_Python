s = input()
d = set(s)
while any(s[i] == s[i + 1] for i in range(len(s) - 1)):
    for x in d:
        if x * 2 in s:
            s = s.replace(x * 2, "")
if s:
    print(s)
else:
    print("Empty String")
