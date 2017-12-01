n, k = input().split(' ')
n, k = int(n), int(k)
c = sorted(list(map(int, input().split(' '))))
count = [0] * k
count_i, min_sum = 0, 0
for i in reversed(range(n)):
    min_sum += (count[count_i]+1) * c[i]
    count[count_i] += 1
    count_i += 1
    if count_i >= k:
        count_i = 0
    #print (count)        
print (min_sum)
