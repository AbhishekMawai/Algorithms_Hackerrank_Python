#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    count = 0
    n = input().strip()
    for x in n:
        if int(x) != 0:
            if int(n) % int(x) == 0:
                count += 1
    print(count)
