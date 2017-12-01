def getWays(n, squares, d, m):
    count = 0
    for i in range(n):
        if i+m <= n and sum(squares[i:i+m]) == d:
            count += 1
    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = getWays(n, s, d, m)
print(result)
