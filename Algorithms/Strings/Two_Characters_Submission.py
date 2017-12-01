from itertools import combinations

s_len = int(input().strip())
s = input().strip()
max_len = 0
char_present = list(combinations(set(s), 2))
#print (char_present)
if len(set(s)) <= 1:
    print (0)
elif len(set(s)) == 2:
    if s[0] != s[1]:
        print (len(s))
    else:
        print (0)
else:        
    for i, j in char_present:
        x = []
        x = [char for char in s if char == i or char == j]
        #print (x)
        if len(set(x[0::2])) == 1 and len(set(x[1::2])) == 1:
            #print (x)
            char_len = len(x)
            max_len = max(char_len, max_len)
    print (max_len)
