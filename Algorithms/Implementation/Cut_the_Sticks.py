n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while len(arr) > 0:
    print (len(arr))
    min_arr = min(arr)
    arr = [x-min_arr for x in arr]
    arr = [x for x in arr if 0 is not x]
    
