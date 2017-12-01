#!/bin/python3

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
d = dict((x, c.count(x)) for x in set(c))
count = sum([(val // 2) for val in d.values()])
print (count)        