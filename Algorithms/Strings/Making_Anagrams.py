S1 = input()
S2 = input()

ar1 = [0] * 26
ar2 = [0] * 26
deletions = 0
for i in range(len(S1)):
    ar1[ord(S1[i])-97] += 1
for i in range(len(S2)):
    ar2[ord(S2[i])-97] += 1
    
for i in range(26):
    deletions += abs(ar1[i] - ar2[i])
print (deletions)