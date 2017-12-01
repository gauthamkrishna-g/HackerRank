n, k = input().split(' ')
n, k = int(n), int(k)
arr = [int(arr_temp) for arr_temp in input().split(' ')]

d = {val:i for i, val in enumerate(arr)}    
#print (d)
for i, val in enumerate(reversed(range(1, n+1))):
    if val > arr[i]:
        prev_val = arr[i]
        curr_index = d[val]
        arr[i], arr[curr_index] = arr[curr_index], arr[i]
        d[val] = i
        d[prev_val] = curr_index
        k -= 1       
    if k == 0:
        break 
print (*arr)
