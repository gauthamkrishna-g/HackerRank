t = int(input())

for _ in range(t):
    y = int(input().strip())
    z = y
    while(z%3 != 0):
        z -= 5
    if z < 0: 
        print('-1')
    else: 
        print(z * '5' + (y-z) * '3')
