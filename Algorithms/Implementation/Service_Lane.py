n, t = input().strip().split(' ')
n, t = int(n), int(t)
width = [int(width_temp) for width_temp in input().strip().split(' ')]
for _ in range(t):
    i, j = input().strip().split(' ')
    i, j = int(i), int(j)
    print (min(width[i:j+1]))
