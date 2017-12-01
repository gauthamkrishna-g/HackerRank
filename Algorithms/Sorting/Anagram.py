T = int(input())
for _ in range(T):
    S = input()
    if len(S) % 2 == 1:
        print (-1)
    else:
        S1 = list(S[:len(S)//2])
        S2 = list(S[len(S)//2:])
        for i in S1:
            if i in S2:
                S2.remove(i)
        print (len(S2))