#!/bin/python3

import sys

q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = []
    sum_rows = []
    sum_cols = []
    for M_i in range(n):
        M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
        M.append(M_t)
    for col in range(n):
        ball_type = 0
        for row in range(n):
            ball_type += M[row][col]
        sum_cols.append(ball_type)
        sum_rows.append(sum(M[col]))
    if sorted(sum_rows) == sorted(sum_cols):
        print("Possible")
    else:
        print("Impossible")
