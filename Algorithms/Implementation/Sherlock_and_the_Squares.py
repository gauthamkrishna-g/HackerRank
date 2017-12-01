from math import sqrt, floor, ceil
t = int(input())
for _ in range(t):
    a, b = input().split()
    a, b = int(a), int(b)
    print(floor(sqrt(b)) - ceil(sqrt(a)) + 1)