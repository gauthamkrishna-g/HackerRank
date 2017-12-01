T = int(input())
for _ in range(T):
    S = input()
    flag = 0
    l = 0
    r = len(S)-1
    while l < r:
        if S[l] != S[r]:
            if S[l+1] == S[r] and S[l+2] == S[r-1]:
                print (l)
            else:
                print (r)
            flag = 1
            break
        else:
            l += 1
            r -= 1
    if flag == 0:
        print (-1)