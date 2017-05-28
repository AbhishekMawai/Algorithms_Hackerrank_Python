#!/bin/python3

import sys
from operator import itemgetter

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
dist = n
enu = sorted(enumerate(A), key=itemgetter(1))

boo = False

for x in range(len(enu) - 1):
    if enu[x][1] == enu[x + 1][1]:
        newd = enu[x + 1][0] - enu[x][0]
        if newd < dist:
            dist = newd
            boo = True

print(dist if boo else -1)
