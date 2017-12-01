#!/bin/python3

s = input().strip()
count = 0
for char in s:
    if char == char.upper():
        count += 1
print (count+1)        
        
