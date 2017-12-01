n = int(input().strip())
s = input().strip()
k = int(input().strip())
cipher = []
for char in s:
    if 'a' <= char <= 'z':
        cipher.append(chr(((ord(char)-ord('a')+k)%26)+ord('a')))
    elif 'A' <= char <= 'Z':
        cipher.append(chr(((ord(char)-ord('A')+k)%26)+ord('A')))
    else:
        cipher.append(char)
print (''.join(cipher))
