n, k = input().strip().split(' ')
n, k = int(n),int(k)
x = [int(x_temp) for x_temp in input().strip().split(' ')]
x.sort()
#print (x)
last = x[0]
i = count = 0
while i < n:
    while i < n and x[i] <= last + k:
        i += 1
    last = x[i-1]        
    while i < n and x[i] <= last + k:
        i += 1
    if i < n:        
        last = x[i]        
    count += 1
print (count)