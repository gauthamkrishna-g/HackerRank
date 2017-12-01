#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    corr_stud = len([int(x) for x in a if x<=0])
    if corr_stud < k:
        print("YES")
    else:
        print("NO")
    
