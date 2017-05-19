#!/bin/python3

import sys

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
energy = 100
for i in range(0, n, k):
    if c[i] == 0:
        energy -= 1
    else:
        energy -= 3
print(energy)
