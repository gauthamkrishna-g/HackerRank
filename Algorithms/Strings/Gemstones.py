from functools import reduce

n = int(input())
rocks = [input().strip().split(' ') for _ in range(n)]
rocks = [list(rocks[i][0]) for i in range(n)]
common = set(rocks[0]).intersection(*rocks)
#rocks = [set(rocks[i][0]) for i in range(n)]
#common = reduce(set.intersection, rocks)
print (len(common))
