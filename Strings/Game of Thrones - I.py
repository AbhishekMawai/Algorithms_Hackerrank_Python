from collections import Counter
s = input()
c = Counter(s)
count = 0
if len(s) % 2 == 0:
    for x, y in c.items():
        if y % 2 == 1:
            print("NO")
            break
    else:
        print("YES")
else:
    for x, y in c.items():
        if y % 2 == 1:
            count += 1
            if count > 1:
                print("NO")
                break
    else:
        print("YES")
