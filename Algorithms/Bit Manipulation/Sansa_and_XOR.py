T = int(input())

for _ in range(T):
    N = int(input())
    arr = [int(arr_temp) for arr_temp in input().split(' ')]
    xor = 0
    if N % 2 == 1:
        for i in range(0, N, 2):
            xor ^= arr[i]
    print (xor)
