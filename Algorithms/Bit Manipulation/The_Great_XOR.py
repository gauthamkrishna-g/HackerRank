q = int(input())

for _ in range(q):
    x = int(input())
    a = 1
    while a <= x:
        a <<= 1
    print (a-x-1)
