n = int(input().strip())
B = list(input().strip())
count = 0
#if n < 3:
#    print (0)
#else:
for i in range(n): #range(n-2)
    if B[i:i+3] == ['0', '1', '0']:
    #if B[i] == '0' and B[i+1] == '1' and B[i+2] == '0':
        B[i+2] = 1
        count += 1
print (count)
