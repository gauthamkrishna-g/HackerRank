t = int(input())
for _ in range(t):
    R, C = input().strip().split(' ')
    R, C = int(R), int(C)
    G = []
    for _ in range(R):
        G.append(input())
    r, c = input().strip().split(' ')
    r, c = int(r), int(c)
    P = []
    for _ in range(r):
        P.append(input())
    def pattern_check(i, j):
        for k in range(1, r):
            if G[i+k][j:j+c] != P[k][:]:
                return False
        return True            
    flag = 0
    for i in range(R-r+1):
        for j in range(C-c+1):
            if G[i][j:j+c] == P[0][:] and pattern_check(i, j):
                flag = 1
                break
        if flag:
            break
    if flag:
        print ("YES")
    else:
        print ("NO")
