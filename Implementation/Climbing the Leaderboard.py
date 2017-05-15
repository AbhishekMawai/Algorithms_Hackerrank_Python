#!/bin/python3

import sys

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
ranks = []
ranks.append(scores[0])
for x in range(1, n):
    if scores[x] != scores[x - 1]:
        ranks.append(scores[x])
ind = len(ranks) - 1
for each in alice:
    while each > ranks[ind] and ind >= 0:
        ind -= 1
    if each == ranks[ind]:
        print(ind + 1)
    else:
        print(ind + 2)
