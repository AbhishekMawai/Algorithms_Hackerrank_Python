#!/bin/python3

import sys
import copy

n = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = [int(x) for x in list(input().strip())]
    grid.append(grid_t)
final = copy.deepcopy(grid)
for row in range(1, n - 1):
    for column in range(1, n - 1):
        a = grid[column][row]
        if a > grid[column - 1][row] and a > grid[column + 1][row]:
            if a > grid[column][row - 1] and a > grid[column][row + 1]:
                final[column][row] = "X"
for i in final:
    print(*i, sep="")
