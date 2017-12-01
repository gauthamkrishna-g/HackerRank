from collections import Counter

t = int(input())
for _ in range(t):
    s = input()
    sub_strings = {}
    for i in range(len(s)):
        for j in range(1, len(s)-i+1):
            sub_string = frozenset(Counter(s[i:i+j]).items())
            sub_strings[sub_string] = sub_strings.get(sub_string, 0) + 1
    # print (sub_strings)
    
    anagrams = 0
    for sub_string in sub_strings:
        anagrams += sub_strings[sub_string] * (sub_strings[sub_string]-1) // 2
    print (anagrams)          

