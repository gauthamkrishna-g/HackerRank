def solve(a, n):
    i = 0
    j = n-1
    tot_sum = 0
    while i != j:
        if tot_sum >= 0:
            tot_sum -= a[j]
            j -= 1
        else:
            tot_sum += a[i]
            i += 1
    return "YES" if tot_sum == 0 else "NO"

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a, n)
    print(result)