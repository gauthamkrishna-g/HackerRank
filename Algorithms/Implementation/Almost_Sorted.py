n = int(input())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

sorted_arr = sorted(arr)
indices = []
for i in range(n):
    if arr[i] != sorted_arr[i]:
        indices.append(i)

if len(indices) == 2:
    print ("yes")
    print ("swap", indices[0]+1, indices[1]+1)
else:
    segment = arr[indices[0]:indices[-1]+1]
    rev_segment = sorted(segment, reverse=True)
    if segment == rev_segment:
        print ("yes")
        print ("reverse", indices[0]+1, indices[-1]+1)
    else:
        print ("no")
