T = int(input())
for _ in range(T):
    n = int(input())
    s = [int(s_arr) for s_arr in input().split(' ')]
    misere, count = 0, 0
    for i in range(n):
        misere ^= s[i]
        if s[i] <= 1:
            count += 1
    print ("Second" if (count == n and misere == 1) or (count < n and misere == 0) else "First")