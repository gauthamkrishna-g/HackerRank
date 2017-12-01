n = int(input())
ar = [int(ar_temp) for ar_temp in input().strip().split(' ')]
for i in range(n):
    temp = ar[i]
    j = i
    while j > 0 and ar[j-1] > temp:
        ar[j] = ar[j-1]
        j -= 1
    ar[j] = temp
    if i > 0:
        for k in ar:
            print (k, end=' ')
        print ()            
