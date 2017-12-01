from functools import reduce

g = int(input())
for _ in range(g):
    n = int(input())
    s = [int(s_arr) for s_arr in input().split(' ')]
    nim = reduce(lambda a, b: a^b, s)
    print ("Second" if nim == 0 else "First")