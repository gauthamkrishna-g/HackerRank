#!/bin/python3

import sys
import math
s = input().strip()
#s = s.replace(" ", "")
a = len(s)
index,count = 0,0
#i = 0
r = math.floor(math.sqrt(a))
c = math.ceil(math.sqrt(a))
#def cols():
#    global index
#for i in s[0:c]:
def cols():
    global index
    global count
    for i in range(index, a, c):
        if(count >= a):
            return
        print(s[i], end='')
        count += 1
    print(" ", end='')
    index += 1
    cols()

cols()
"""for j in s:
        if index % c == count:
            print(j, end='')
        index += 1
    #j = s[0]
    count += 1
    #index = count
    print(" ", end='') """
#    if count > c:
#       break
#i += 1
#cols()

#print(s)
