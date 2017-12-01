n = int(input())
m = 5
likes = 0
for _ in range(n):
    m = m // 2
    likes += m
    m *= 3
print (likes)