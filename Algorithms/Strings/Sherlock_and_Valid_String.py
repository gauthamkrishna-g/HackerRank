S = input()
d = {x: S.count(x) for x in set(S)}
#print (d)
counts = list(d.values())
min_count = min(counts)
max_count = max(counts)
changes, min_counts, max_counts = 0, 0, 0
for i in range(len(counts)):        
    if counts[i] > min_count and counts[i] < max_count:
        changes += 1
    elif counts[i] == min_count:
        min_counts += 1
    elif counts[i] == max_count:
        max_counts += 1
    #print (changes, min_counts, max_counts)       
if min_count == max_count or (changes == 0 and (min_counts == 1 or max_counts == 1)):
    print ("YES")
else:
    print ("NO")