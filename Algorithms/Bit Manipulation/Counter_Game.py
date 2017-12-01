T = int(input())

for _ in range(T):
    N = int(input())
    setbits = sum([i == '1' for i in bin(N-1)[2:]])
    #print (setbits)
    if setbits & 1:
        print ("Louise")
    else:
        print ("Richard")
