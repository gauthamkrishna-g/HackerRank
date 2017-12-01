t = int(input())
for _ in range(t):
    s = [s_temp for s_temp in input().strip()]
    #s_len = len(s)
    #s_first_half = s[:s_len//2]
    #s_second_half = s[s_len//2+s_len%2:][::-1] 
    op = 0
    for i in range(len(s)//2):
        #op += ord(max(s_first_half[i], s_second_half[i])) - ord(min(s_first_half[i], s_second_half[i]))
        op += abs(ord(s[i]) - ord(s[len(s)-i-1]))
    print (op)