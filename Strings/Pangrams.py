import string
s = input()
s = s.lower()
check = string.ascii_lowercase
lena = len(check)
for each in check:
    if each in s:
        lena -= 1
if lena:
    print("not pangram")
else:
    print("pangram")
