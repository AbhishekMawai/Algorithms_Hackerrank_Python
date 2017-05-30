import math
n, k = [int(x) for x in input().strip().split()]
arr = [int(y) for y in input().strip().split()]
count = 0
currentpage = 0
for chapterprob in arr:
    numpages = math.ceil(chapterprob / k)
    for a in range(1, numpages + 1):
        if a < numpages or chapterprob % k == 0:
            currentpage += 1
            lower = ((a - 1) * k) + 1
            higher = a * k
            if lower <= currentpage <= higher:
                count += 1
        else:
            currentpage += 1
            lower = ((a - 1) * k) + 1
            higher = (a - 1) * k + (chapterprob % k)
            if lower <= currentpage <= higher:
                count += 1
print(count)
