x1, v1, x2, v2 = [int(x) for x in input().strip().split(' ')]
if v2 >= v1:
    print("NO")
else:
    while x1 < x2:
        x1 += v1
        x2 += v2
        if x1 == x2:
            print("YES")
            break
        elif x1 > x2:
            print("NO")
            break
