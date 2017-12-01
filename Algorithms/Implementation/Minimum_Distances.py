n = int(input())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
min_dij = n+1
count = 0
#if all(a.count(ele) == 1 for ele in set(a)):
#    print (-1)
for ele in set(a):
    if a.count(ele) > 1:
        indices = [index for index, element in enumerate(a) if element == ele]
        min_index_ij = min([indices[i] - indices[i-1] for i in range(1, len(indices))])
        min_dij = min(min_index_ij, min_dij)
        count += 1
if count > 0:
    print (min_dij)
else:
    print (-1)
