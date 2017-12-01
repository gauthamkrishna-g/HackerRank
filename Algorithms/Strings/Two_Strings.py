p = int(input())
for _ in range(p):
    a = input()
    b = input()
    flag = 0
    for i in a:
        if i in b:
            flag = 1
            break
    if flag:
        print ("YES")
    else:
        print ("NO")