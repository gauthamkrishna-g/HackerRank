n = int(input())
for _ in range(n):
    s = input().strip()
    count = 0
    #if len(set(s)) == 1:
    #    print (len(s)-1)
    #else:
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    print (count)
