n = int(input())
for i in range(n):
    s = input()
    r = s[::-1]
    for j in range(len(s) - 1):
        if abs(ord(s[j + 1]) - ord(s[j])) != abs(ord(r[j + 1]) - ord(r[j])):
            print("Not Funny")
            break
    else:
        print("Funny")
