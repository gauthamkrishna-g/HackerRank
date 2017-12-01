tot = count = 0
#a = []
n,x = input().split()
n = int(n)
x = int(x)
a=[int(toy) for toy in input().split(" ")]
a.sort()
for i in range(len(a)):
    tot += a[i]
    if tot <= x:
        count += 1
print(count)        

        