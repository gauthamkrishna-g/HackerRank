#!/bin/python3
h = 0
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n%2 == 1:
        h = 2 ** (int(n/2) + 2) - 2
    elif n%2 == 0:
        h = 2 ** (int(n/2) + 1) - 1
    print(h)        	