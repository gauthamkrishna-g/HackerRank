from functools import reduce
import operator

n = int(input())
a = [int(a_temp) for a_temp in input().split(' ')]
print (reduce(operator.xor, a))
