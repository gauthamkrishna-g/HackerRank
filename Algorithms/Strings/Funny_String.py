t = int(input().strip())
for a0 in range(t):
    funny = []
    s = input().strip()
    r = s[::-1]
    for j in range(1, len(s)):
        if abs(ord(s[j]) - ord(s[j-1])) == abs(ord(r[j]) - ord(r[j-1])):
            funny.append(1)
        else:
            funny.append(0)
    #print(funny)
    if all(x == 1 for x in funny):
        print("Funny")
    else:
        print("Not Funny")
