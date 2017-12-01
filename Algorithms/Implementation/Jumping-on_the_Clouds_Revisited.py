#!/bin/python3

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
E = 100
i = 0
while i < n:
    E -= 1
    if c[i] == 1:
        E -= 2 
    if (i+k) % n == 0:
        print (E)
        break
    else:
        i = (i+k) % n   
                
