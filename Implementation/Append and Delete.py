#!/bin/python3

import sys

s = input().strip()
t = input().strip()
k = int(input().strip())
if k >= len(s) + len(t):
    print("Yes")
else:
    if len(s) > len(t):
        s, t = t, s
    rems = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            rems = len(s[i:])
            remt = len(t[i:])
            break
    else:
        rems = 0
        remt = len(t[i + 1:])
    if k < rems + remt:
        print("No")
    elif k == rems + remt:
        print("Yes")
    else:
        if rems == len(s):
            if k > rems + remt:
                print("Yes")
            else:
                print("No")
        elif (k - (rems + remt)) % 2 == 0:
            print("Yes")
        else:
            print("No")
