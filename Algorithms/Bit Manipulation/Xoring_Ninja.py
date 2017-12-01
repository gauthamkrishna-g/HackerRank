T = int(input())
for _ in range(T):
    n = int(input())
    x, y = 0, 1
    mod = (10**9) + 7
    a = [int(a_temp) for a_temp in input().split(' ')]
    #print (a)
    for i in range(n):
        x |= a[i] 
        x %= mod
        if i:
            y <<= 1
        y %= mod
    print ((x*y) % mod)
