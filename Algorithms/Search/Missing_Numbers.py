n_len = int(input())
n = [int(n_temp) for n_temp in input().strip().split(' ')]
m_len = int(input())
m = [int(m_temp) for m_temp in input().strip().split(' ')]
counts = [0] * 201
pivot = n[0]
for i in range(n_len):
    counts[100+n[i]-pivot] += 1
for i in range(m_len):
    counts[100+m[i]-pivot] -= 1
#print (counts)    
for i in range(len(counts)):
    if counts[i] != 0:
        print (i-100+pivot, end=' ')