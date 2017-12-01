#!/bin/python3

h = list(map(int, input().strip().split(' ')))
word = input().strip()
max_height = 0
for w in word:
    i = ord(w)-97
    max_height = max(max_height, h[i])
print (len(word)*max_height)    
