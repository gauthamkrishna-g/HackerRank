#!/bin/python3

s = input().strip()
t = input().strip()
k = int(input().strip())
s, t = list(s), list(t)
s_len, t_len = len(s), len(t)
i = 0
while i<s_len and i<t_len:
    if s[i] == t[i]:
        i += 1
    else:
        break
non_match = s_len - i + t_len - i
if k >= s_len+t_len or k >= non_match and (k-non_match)%2 == 0:
    print ("Yes")
else:
    print ("No")