#!/bin/python3

import sys
import string
h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = list(input().strip())
s = list(string.ascii_lowercase)
d = dict(zip(s, h))
max = 0
for _ in word:
    if d[_] > max:
        max = d[_]
print(len(word) * max)
