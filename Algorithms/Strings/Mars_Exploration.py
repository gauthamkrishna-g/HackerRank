S = input().strip()
count = i = 0
for i in range(len(S)):
    if S[i] != "SOS"[i%3]:
        count += 1
    else:
        continue
print (count)  
