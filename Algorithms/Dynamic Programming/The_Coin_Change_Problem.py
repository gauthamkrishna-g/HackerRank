n, m = input().split(' ')
n, m = int(n), int(m)
c = [int(c_temp) for c_temp in input().split(' ')]
ways = [0] * (n+1)
ways[0] = 1
for i in range(m):
    for j in range(n):
        x = j + c[i]
        if x > n:
            break
        ways[x] += ways[j]
print (ways[n])