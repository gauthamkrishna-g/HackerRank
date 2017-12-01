n = int(input())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
d = {x:a.count(x) for x in set(a)}
print (len(a) - max(d.values()))