n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
a.sort()
b = [abs(a[i+1]-a[i]) for i in range(len(a)-1)]
print (min(b))