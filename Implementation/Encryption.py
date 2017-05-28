#!/bin/python3

import sys
import math
import itertools

s = input().strip()
n = len(s)
row = math.floor(math.sqrt(n))
col = math.ceil(math.sqrt(n))
while row * col < n:
    row = row + 1
li = []
y = 0
for x in range(row):
    li.append(list(s[y:y + col]))
    y = y + col
ans = list(itertools.zip_longest(*li))
for x in ans:
    print("".join(filter(None, x)), end=" ")
