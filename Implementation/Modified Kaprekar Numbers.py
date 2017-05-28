p = int(input())
q = int(input())
li = []
for num in range(p, q + 1):
    d = len(str(num))
    sq = num * num
    r = str(sq)[len(str(sq)) - d:]
    l = str(sq)[:len(str(sq)) - d]
    if l == "":
        l = "0"
    if int(l) + int(r) == num:
        li.append(num)
if li:
    print(*li)
else:
    print("INVALID RANGE")
