s = list(input())
arr = []
for char in s:
    if arr and arr[-1] == char:
        arr.pop()
    else:
        arr.append(char)
if arr:
    print (''.join(arr))
else:
    print ("Empty String")
