#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    b, w = input().strip().split(' ')
    b, w = [int(b), int(w)]
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]
    if x > y + z:
        print(b * (y + z) + w * y)
    elif y > x + z:
        print(b * x + w * (x + z))
    else:
        print(b * x + w * y)
