n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = sorted([int(c_temp) for c_temp in input().strip().split(' ')])
#c = sorted(c)
#print (c)
if n == m:
    print (0)
else:
    max_dist = 0
    for i in range(m-1):
        c_dist = (c[i+1] - c[i]) // 2
        max_dist = max(max_dist, c_dist)
    max_dist = max(c[0]-0, max_dist, n-1-c[m-1])
    print (max_dist)
