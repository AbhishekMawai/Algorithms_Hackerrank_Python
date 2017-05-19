#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ini = 1
    for x in range(n + 1):
        if x == 0:
            pass
        elif x % 2 == 1:
            ini = 2 * ini
        else:
            ini += 1
    print(ini)
