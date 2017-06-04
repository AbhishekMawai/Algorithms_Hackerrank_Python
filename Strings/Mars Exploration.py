cnt = 0
S = input().strip()
for x in range(0, len(S), 3):
    if S[x] != "S":
        cnt += 1
    if S[x + 2] != "S":
        cnt += 1
    if S[x + 1] != "O":
        cnt += 1
print(cnt)
