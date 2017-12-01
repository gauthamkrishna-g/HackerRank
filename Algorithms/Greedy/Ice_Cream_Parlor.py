t = int(input())

for _ in range(t):
    m = int(input())
    n = int(input())
    c = [int(c_temp) for c_temp in input().split(' ')]
    d = {}
    for i in range(n):
        complement = m - c[i]
        if complement in d:
            print (d[complement]+1, i+1)
            break
        d[c[i]] = i            
