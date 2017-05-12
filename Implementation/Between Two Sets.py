n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]
maxa = max(a)
minb = min(b)
count = 0
for x in range(maxa, minb + 1):
    boo = True
    for y in a:
        if x % y != 0:
            boo = False
            break
    if boo:
        for z in b:
            if z % x != 0:
                boo = False
                break
        if boo:
            count += 1
print(count)
