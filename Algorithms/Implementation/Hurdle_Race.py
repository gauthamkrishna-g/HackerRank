#!/bin/python3

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
max_height = max(height)
if max_height - k >= 1:
    print (max_height-k)
else:
    print (0)
    
