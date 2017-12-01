n = int(input())
ar = [int(input().split(' ')[0]) for _ in range(n)]
count = 0
for i in range(100):
    count += ar.count(i)
    print (count, end=' ')