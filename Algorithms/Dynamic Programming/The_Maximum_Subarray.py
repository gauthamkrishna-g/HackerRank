T = int(input())
for _ in range(T):
    N = int(input())
    a = [int(a_temp) for a_temp in input().split(' ')]
    
    max_ending_here, max_so_far = a[0], a[0]
    for x in a[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_ending_here, max_so_far)
    
    non_contiguous_sum = a[0]
    for x in a[1:]:
        non_contiguous_sum = max(x, non_contiguous_sum + max(x, 0))
    print (max_so_far, non_contiguous_sum)