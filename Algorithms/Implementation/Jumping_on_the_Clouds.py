#!/bin/python3

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
jump = -1
cloud = 0
while cloud < n:
    if cloud < n-2 and c[cloud+2] == 0:
        cloud += 1
    cloud += 1        
    jump += 1
print(jump)        
        
