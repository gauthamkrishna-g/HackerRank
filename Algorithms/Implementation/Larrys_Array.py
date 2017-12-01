T = int(input())

for _ in range(T):
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    swaps = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                swaps += 1
    #print (swaps)                
    if swaps % 2 == 0:
        print ("YES")
    else:
        print ("NO")
