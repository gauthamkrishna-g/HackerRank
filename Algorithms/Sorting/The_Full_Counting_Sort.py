n = int(input())
ar = [[] for _ in range(100)]
for i in range(n):
    integer, string = input().strip().split(' ')
    integer = int(integer)
    if i < n//2:
        string = '-'
    ar[integer].append(string)
#print (ar)
print (' '.join([string for equal_string in ar for string in equal_string]))