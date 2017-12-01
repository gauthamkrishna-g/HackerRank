def count_ways(x, n, k):
    if x < 0 or k**n > x:
        return 0
    if x == 0 or k**n == x:
        return 1
    return count_ways(x, n, k+1) + count_ways(x-(k**n), n, k+1)
x = int(input())
n = int(input())
ways = count_ways(x, n, 1)
print (ways)