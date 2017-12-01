q = int(input().strip())

for _ in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if abs(z-x) > abs(z-y):
        print ("Cat B")
    elif abs(z-x) < abs(z-y):
        print ("Cat A")
    else:
        print ("Mouse C")
