def calc_operations(chocs, N):
    min_chocs = min(chocs)
    ops = [0, 0, 0]
    for i in range(N):
        for j in range(3):        
            curr_ops = 0
            left = chocs[i] - (min_chocs - j)
            curr_ops += (left // 5)
            curr_ops += (left%5 // 2)
            curr_ops += (left%5%2 // 1)
            ops[j] += curr_ops
        #ops = min(curr_ops, ops)
    return min(ops)

T = int(input())
for _ in range(T):
    N = int(input())
    chocs = [int(chocs_temp) for chocs_temp in input().split(' ')]
    print (calc_operations(chocs, N))