t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    cost = b*x + w*y
    x_cost = b*(y+z) + w*y
    y_cost = b*x + w*(x+z)        
    new_cost = min(cost, x_cost, y_cost)
    print (new_cost)
