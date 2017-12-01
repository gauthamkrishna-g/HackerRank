n = int(input())
k = int(input())
x = sorted([int(input()) for _ in range(n)])
#print (x)
min_unfairness = x[n-1] - x[0]
for i in range(n-k+1):
    if x[i+k-1] - x[i] < min_unfairness:
        min_unfairness = x[i+k-1] - x[i]
    #print (x[i+k-1], x[i])
print (min_unfairness)
