n = int(input())
ar = [int(ar_temp) for ar_temp in input().split(' ')]
d = {i:0 for i in range(100)}
for i in ar:
    d[i] += 1
print (' '.join(map(str, d.values())))