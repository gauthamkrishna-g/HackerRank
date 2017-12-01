n = int(input())
ratings = [int(input()) for _ in range(n)]

candies = [1] * n
for i in range(1, n):
    if ratings[i] > ratings[i-1]:
        candies[i] = candies[i-1] + 1
#print (candies)
for i in reversed(range(1, n)):
    if ratings[i] < ratings[i-1]:
        candies[i-1] = max(candies[i-1], candies[i]+1)
print (sum(candies))
