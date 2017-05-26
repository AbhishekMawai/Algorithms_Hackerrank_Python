#!/bin/python3

import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
i = 0
count = 0
while i <= n - 2:
    if i + 2 >= n:
        count += 1
        break
    elif c[i + 2] == 0:
        i += 2
        count += 1
    else:
        i += 1
        count += 1
print(count)
