xor = lambda n: [n, 2, n+2, 0][n%8//2]

Q = int(input())
for _ in range(Q):
    L, R = input().split(' ')
    L, R = int(L), int(R)
    print (xor(L-1) ^ xor(R))
