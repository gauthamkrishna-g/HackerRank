n = int(input())
arr = [int(arr_temp) for arr_temp in input().split(' ')]

#print (*reversed(arr))
for i in range(n//2):
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
print (*arr)
