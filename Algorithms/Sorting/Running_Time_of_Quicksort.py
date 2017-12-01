n = int(input())
ar = [int(ar_temp) for ar_temp in input().split(' ')]
ar_ins = [int(ar_temp) for ar_temp in ar]

ins_count = 0
for i in range(n):
    temp = ar_ins[i]
    j = i
    while j > 0 and ar_ins[j-1] > temp:
        ar_ins[j] = ar_ins[j-1]
        j -= 1
        ins_count += 1
    ar_ins[j] = temp

def partition(ar, l, r, quick_count):
    j = l
    pivot = ar[r]
    for i in range(l, r):
        if ar[i] <= pivot:
            ar[i], ar[j] = ar[j], ar[i]
            j += 1
            quick_count.append(None)
    ar[r], ar[j] = ar[j], ar[r]
    quick_count.append(None)
    return j

def quick_sort(ar, l, r, quick_count):
    if l >= r:
        return
    m = partition(ar, l, r, quick_count)
    quick_sort(ar, l, m-1, quick_count)
    quick_sort(ar, m+1, r, quick_count)

quick_count = []
quick_sort(ar, 0, n-1, quick_count) 
print (ins_count - len(quick_count))