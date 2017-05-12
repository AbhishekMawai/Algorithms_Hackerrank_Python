n = int(input().strip())
score = list(map(int, input().strip().split(' ')))
best = score[0]
bestcount = 0
worst = score[0]
worstcount = 0
for x in score:
    if x > best:
        best = x
        bestcount += 1
    elif x < worst:
        worst = x
        worstcount += 1
print(bestcount, worstcount)
