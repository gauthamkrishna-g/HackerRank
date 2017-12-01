from functools import reduce

T = int(input())
for _ in range(T):
    n, k = map(int, input().split(' '))
    c = [int(c_temp) for c_temp in input().split(' ')]
    poker = reduce(lambda a, b: a^b, c)
    print ("Second" if poker == 0 else "First")