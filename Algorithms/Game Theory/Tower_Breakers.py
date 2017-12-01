T = int(input())
for _ in range(T):
    N, M = input().split(' ')
    N, M = int(N), int(M)
    print (2 if (M == 1 or N % 2 == 0) else 1)
