N = int(input())

A, B = [0] * 1000, [0] * 1000
for A_temp in input().split(' '):
    A[int(A_temp)-1] += 1
for B_temp in input().split(' '):
    B[int(B_temp)-1] += 1
#print (A, B)
count = 0
for i in range(1000):
    count += min(A[i], B[i]) 

if count < N:
    count += 1
else:
    count -= 1
print (count)    