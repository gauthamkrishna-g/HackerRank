from math import sqrt

L, s1, s2 = input().strip(' ').split()
L, s1, s2 = int(L), int(s1), int(s2)
Q = int(input())
q = []
for _ in range(Q):
    q.append(int(input()))

for i in range(len(q)):
    x = L * (2 ** 0.5)
    y = (q[i] ** 0.5) * (2 ** 0.5)
    t = (x - y) / abs(s1-s2)
    print(t)