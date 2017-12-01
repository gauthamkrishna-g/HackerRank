s = input().strip()
n = int(input().strip())
d = {}
i = count = 0
while i < len(s):
    if s[i] == s[i-1]:
        count += ord(s[i]) - 96
    else: 
        count = ord(s[i]) - 96
    d[count] = 1
    i += 1
#print (d)    
for x in [int(input()) for _ in range(n)]:
    print('Yes' if x in d else 'No')
