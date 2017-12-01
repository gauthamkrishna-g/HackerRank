t = int(input())
for _ in range(t):
    n = int(input())
    c = [int(temp_c) for temp_c in input().strip().split(' ')]
    r = 0
    for i in range(n):
        if c[i] % 2 == 1:
            r ^= i
    if r == 0:
        print ("Second")
    else:
        print ("First")