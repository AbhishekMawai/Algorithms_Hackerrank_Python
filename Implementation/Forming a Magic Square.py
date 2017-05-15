li = []
for i in range(3):
    lj = [int(x) for x in input().split()]
    li.append(lj)
    lj = list()
possib = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]], [[6, 1, 8], [7, 5, 3], [2, 9, 4]], [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], [[8, 3, 4], [1, 5, 9], [6, 7, 2]], [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

total = []
total_list = []
for each_matr in possib:
    for x in range(3):
        for y in range(3):
            total.append(abs(each_matr[x][y] - li[x][y]))
    total_list.append(sum(total))
    total = []
print(min(total_list))
