from collections import Counter

q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = [[int(M_temp) for M_temp in input().strip().split(' ')] for i in range(n)]
    container_size = Counter(sum(row) for row in M)
    ball_count = Counter(sum(col) for col in zip(*M))
    if container_size == ball_count:
        print ("Possible")
    else:
        print ("Impossible")