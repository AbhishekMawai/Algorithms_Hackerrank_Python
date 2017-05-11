n = int(input())
li = [int(x) for x in input().split()]
li_sorted = sorted(li)


def find_elem(lis):
    count = 0
    li_dict = {}
    for i in range(n):
        li_dict[lis[i]] = i
    for j in range(n):
        if lis[j] != li_sorted[j]:
            count += 1
            ind = li_dict[li_sorted[j]]
            li_dict[lis[j]] = ind
            lis[j], lis[ind] = lis[ind], lis[j]
    return count


print(min(find_elem(list(reversed(li))), find_elem(list(li))))
