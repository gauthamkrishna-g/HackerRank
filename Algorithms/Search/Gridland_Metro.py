n, m, k = input().split()
n, m ,k = int(n), int(m), int(k)

d = {}
for _ in range(k):
    r, c1, c2 = input().split()
    r, c1, c2 = int(r), int(c1), int(c2)
    if r not in d:
        d[r] = [(c1, c2)]
    else:
        for row in d[r]:
            if c1 >= row[0] and c1 <= row[1]:
                d[r].append((row[0], max(c2, row[1])))
                d[r].remove(row)
            elif c2 >= row[0] and c2 <= row[1]:
                d[r].append((min(c1, row[0]), row[1]))
                d[r].remove(row)
            else:
                d[r].append((c1, c2))
                
lampposts = n * m                
for r in d:
    for row in d[r]:
        lampposts -= (row[1] - row[0] + 1)
print (lampposts)
