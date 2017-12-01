t = int(input())
for _ in range(t):
    w = list(input().strip())
    i = len(w) - 1
    while i>0 and w[i-1] >= w[i]:
        i -= 1
    if i<=0:
        print("no answer")
        continue
    j = len(w) - 1        
    while w[j] <= w[i-1]:
        j -= 1
    w[i-1], w[j] = w[j], w[i-1]
    w = w[:i] + sorted(w[i:])
    str = ''.join(w)
    print(str)
        
            
            
            
    