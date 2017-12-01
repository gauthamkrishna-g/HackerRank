n = int(input().strip())
count = 2 ** (bin(int(n)).lstrip('0b').count('0'))
print (count)
