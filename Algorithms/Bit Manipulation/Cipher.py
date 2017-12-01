N, K = input().split(' ')
N, K = int(N), int(K)
S = input()
#print (S)
B = []
B.append(int(S[0]))
temp = int(B[0])
i, j = 0, 0
while len(B) < N:
    B.append(temp ^ int(S[j+1]))
    j += 1
    if j >= K-1:
        i += 1
        temp ^= B[i-1]
    temp ^= int(B[j])
print (''.join(map(str, B)))
