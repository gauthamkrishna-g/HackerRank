n = int(input())
ar = [int(ar_temp) for ar_temp in input().strip().split(' ')]

def quicksort(ar):
    if len(ar) <= 1:
        return ar
    p = ar[0]
    left = [x for x in ar if x < p]
    equal = [x for x in ar if x == p]
    right = [x for x in ar if x > p]
    final = quicksort(left) + equal + quicksort(right)
    print (' '.join(map(str, final)))
    return final

quicksort(ar)