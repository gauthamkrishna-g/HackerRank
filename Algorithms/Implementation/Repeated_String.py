#!/bin/python3

s = list(input().strip())
n = int(input().strip())
s_len = len(s)
a_count_s = s.count('a')
a_count = n // s_len 
extra = n % s_len
a_count_extra = 0
if extra > 0:
    a_count_extra = s[:extra].count('a')    
a_count_n = a_count * a_count_s + a_count_extra
print (a_count_n)