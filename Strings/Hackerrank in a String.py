q = int(input().strip())
for a0 in range(q):
    s = iter(input().strip().lower())
    for x in "hackerrank":
        if x not in s:
            print("NO")
            break
    else:
        print("YES")
