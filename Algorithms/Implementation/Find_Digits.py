t = int(input())
for _ in range(t):
    n = input()
    a = [int(i) for i in n]
    a = [int(n) % int(i) for i in a if i > 0]
    print(a.count(0))
