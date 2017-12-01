n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

count = 0
b = [0] * n
for i in range(n):
    b[i] = a.count(i)   
for i in range(n-1):
    if b[i] + b[i+1] > count:
        count = b[i] + b[i+1]
print (count)        