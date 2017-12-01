#!/bin/python3

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]
#a_temp = [x%4 for x in [4, 6, 8]]
#print (any(a_temp) == 1)
count = 0
for x in range(a[-1], b[0]+1):
    a_temp = [x%i for i in a]
    if any(a_temp) is not True: # any() returns True if any element is non_zero
        b_temp = [i%x for i in b]
        if any(b_temp) is not True:
            #print(x)
            count += 1
print (count)            