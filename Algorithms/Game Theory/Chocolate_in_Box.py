from functools import reduce

N = int(input())
A = [int(A_temp) for A_temp in input().split(' ')]
X = reduce(lambda a, b: a^b, A)
print (sum([int(X^i < i) for i in A]))