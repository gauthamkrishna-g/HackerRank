n = int(input().strip())
for _ in range(n):
    s = input().strip()
    p = {}
    cost = 0
    for i in s:
        if i in p:
            continue
        else:
            p[i] = 1
            cost += 1
    print (cost)
