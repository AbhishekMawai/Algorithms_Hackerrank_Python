#!/bin/python3

import sys
from collections import deque

n, k, q = input().strip().split(' ')
n, k, q = [int(n), int(k), int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
m = []
for x in range(q):
    m.append(int(input().strip()))
d = deque(a)
d.rotate(k)
for y in m:
    print(d[y])
