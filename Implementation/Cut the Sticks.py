#!/bin/python3

import sys

n = int(input().strip())
li = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while li:
    cut = min(li)
    print(len(li))
    for x in range(len(li)):
        li[x] = li[x] - cut
    li = [x for x in li if x > 0]
