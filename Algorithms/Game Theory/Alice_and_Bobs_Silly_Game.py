prime_nums = [2]
first = 2
g = int(input().strip())
for _ in range(g):
    n = int(input().strip())
    if first < n:
        for i in range(first+1, n+1):
            for p in prime_nums:
                if i % p == 0:
                    break
            else:
                prime_nums.append(i)
        first = n        
    count = 0
    for i in prime_nums:
        if i > n:
            break
        count += 1
    #print (prime_nums)        
    print('Alice' if count %2 == 1 else 'Bob')