n, k = input().strip().split(' ')
n, k = int(n), int(k)
nums = [int(nums_temp) for nums_temp in input().split(' ')]
d = {num:0 for num in nums}
#print (d)
count = 0
for i in nums:
    if i + k in d:    
        count += 1
print (count)