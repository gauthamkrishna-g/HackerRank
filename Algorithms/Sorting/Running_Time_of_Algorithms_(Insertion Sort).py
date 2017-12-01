n = int(input())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
#print (a)
count = 0
for i in range(n):
    temp = a[i]
    j = i
    while j > 0 and a[j-1] > temp:
        a[j] = a[j-1]
        j -= 1
        count += 1
    a[j] = temp
print (count)