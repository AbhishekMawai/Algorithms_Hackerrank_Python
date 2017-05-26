#!/bin/python3

import sys

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
topic = []
topic_i = 0
large = 0
li = []
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(topic_t)

for x in range(n - 1):
    y = x + 1
    while y <= n - 1:
        count = 0
        d = zip(topic[x], topic[y])
        for _ in d:
            if "1" in _:
                count += 1
        y += 1
        li.append(count)
        if large < count:
            large = count

print(large)
print(li.count(large))
