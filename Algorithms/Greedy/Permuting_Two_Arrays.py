q = int(input())
for _ in range(q):
    n, k = input().split(' ')
    n, k = int(n), int(k)
    a = sorted([int(a_temp) for a_temp in input().split(' ')])
    b = sorted([int(b_temp) for b_temp in input().split(' ')], reverse=True)
    flag = 0
    for i in range(n):
        if a[i] + b[i] < k:
            flag = 1
    if flag == 0:
        print ("YES")
    else:
        print ("NO")
