n = int(input())
ar = [int(ar_temp) for ar_temp in input().split(' ')]

def partition(ar, l, r):
    j = l
    pivot = ar[r]
    for i in range(l, r):
        if ar[i] <= pivot:
            ar[i], ar[j] = ar[j], ar[i]
            j += 1
    ar[r], ar[j] = ar[j], ar[r]
    return j

def quick_sort(ar, l, r):
    if l >= r:
        return
    m = partition(ar, l, r)
    print (' '.join(map(str, ar)))
    quick_sort(ar, l, m-1)
    quick_sort(ar, m+1, r)

quick_sort(ar, 0, n-1)    