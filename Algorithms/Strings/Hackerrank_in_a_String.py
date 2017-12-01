q = int(input().strip())
for _ in range(q):
    a = list('hackerrank')
    s = list(input().strip())
    j = 0
    for char in s:
        if char == a[j]:
            j += 1
        if j == 10:
            print ("YES")
            break
    if j != 10:
        print ("NO")