t1, t2, n = input().strip().split(' ')
t1, t2, n = int(t1), int(t2), int(n)
for i in range(n-2):
    t3 = t1 + (t2 ** 2)
    t1 = t2
    t2 = t3
print (t3)    