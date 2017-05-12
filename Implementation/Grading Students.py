n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())
    if (grade // 5 + 1) * 5 - grade < 3 and ((grade // 5 + 1) * 5) >= 40:
        print((grade // 5 + 1) * 5)
    else:
        print(grade)
