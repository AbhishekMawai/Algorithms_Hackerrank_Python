#!/bin/python3

import sys

s = input().strip()
n = int(input().strip())
if n % len(s) == 0:
    count = n // len(s) * s.count("a")
else:
    count = n // len(s) * s.count("a") + s[:n % len(s)].count("a")
print(count)
