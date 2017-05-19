#!/bin/python3

import sys

n = int(input().strip())
previous = 1
for i in range(1, n + 1):
    current = i * previous
    previous = current
print(current)
