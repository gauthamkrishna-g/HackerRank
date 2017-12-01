t = int(input())
for a0 in range(t):
    n, c, m = input().strip().split(' ')
    n, c, m = int(n), int(c), int(m)
    chocs = n // c
    wraps = chocs
    while wraps >= m:
        add_chocs = wraps // m
        wraps = add_chocs + wraps % m
        chocs += add_chocs
    print (chocs)
