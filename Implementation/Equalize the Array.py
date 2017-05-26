n = int(input())
li = [int(x) for x in input().split()]
lj = []
if len(set(li)) == 1:
    print("0")
else:
    for x in li:
        lj.append(li.count(x))
    print(n - max(lj))
