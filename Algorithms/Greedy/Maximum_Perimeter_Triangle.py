n = int(input())
l = [int(l_temp) for l_temp in input().strip().split(' ')]
l.sort(reverse=True)
for i in range(n-2):
    if l[i] < l[i+1] + l[i+2]:
        print (l[i+2], l[i+1], l[i])
        break
else:
    print (-1)