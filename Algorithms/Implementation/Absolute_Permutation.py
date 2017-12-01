t = int(input())
for _ in range(t):
    n, k = input().strip().split(' ')
    n, k = int(n), int(k)
    if k == 0:
        print (*list(range(1, n+1)))
    elif (n / k) % 2 != 0:
        print (-1)
    else:        
        perm = []
        sign = True 
        for i in range(1, n+1):
            if sign:
                perm.append(i + k)
            else:
                perm.append(i - k)
            if i % k == 0:
                if sign:
                    sign = False
                else:
                    sign = True
        print (*perm)
