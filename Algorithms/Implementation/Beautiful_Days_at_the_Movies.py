i, j , k = input().strip().split(' ')
i, j, k = int(i), int(j), int(k)
count = 0
for num in range(i, j+1):
    rev_num = int(''.join(list(str(num))[::-1]))
    x = abs(num-rev_num)
    #print (x)
    if x % k == 0:
        count += 1
print (count)