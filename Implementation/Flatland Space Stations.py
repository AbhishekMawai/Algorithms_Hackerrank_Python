#!/bin/python3

import sys

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
c.sort()
li = []
for i in range(m - 1):
    li.append((c[i + 1] - c[i]) // 2)
li.append(c[0])
li.append(abs(c[m - 1] - (n - 1)))
print(max(li))
