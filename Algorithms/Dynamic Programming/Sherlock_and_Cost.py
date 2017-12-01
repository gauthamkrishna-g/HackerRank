T = int(input())

for _ in range(T):
    N = int(input())
    B = [int(B_temp) for B_temp in input().split(' ')]    
    low, high = 0, 0
    for i in range(1, N):
        low_next = max(low, high+abs(B[i-1]-1))
        high_next = max(high, low+abs(B[i]-1))
        low, high = low_next, high_next    
    print(max(low, high))
