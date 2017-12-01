L = int(input())
R = int(input())
xor = L ^ R
max_xor = 1
while xor:
    xor >>= 1
    max_xor <<= 1
print (max_xor-1)
