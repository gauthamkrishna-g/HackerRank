n = int(input())
ar = [int(ar_temp) for ar_temp in input().strip().split(' ')]
p = ar[0]
left = [x for x in ar if x < p]
equal = [x for x in ar if x == p]
right = [x for x in ar if x > p]
print (' '.join(map(str, left + equal + right)))