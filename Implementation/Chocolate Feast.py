#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n, c, m = input().strip().split(' ')
    n, c, m = [int(n), int(c), int(m)]
    total = 0
    wrappers = n // c
    total += wrappers
    remaining = 0
    while wrappers >= m:
        total = total + wrappers // m
        remaining = wrappers % m
        wrappers = wrappers // m + remaining
    print(total)
