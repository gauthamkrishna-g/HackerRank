N = int(input())
w = [int(w_temp) for w_temp in input().split(' ')]

w.sort()
units = 1
low = w[0]
for i in range(1, N):
    if w[i] > low + 4:
        units += 1
        low = w[i]
print (units)
