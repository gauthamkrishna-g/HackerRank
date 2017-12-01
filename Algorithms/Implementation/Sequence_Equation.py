n = int(input())
p = [int(p_temp)-1 for p_temp in input().strip().split(' ')]
for i in range(n):
    print(p.index(p.index(i)) + 1)