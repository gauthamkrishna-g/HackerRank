def chess(x, y):
    if 1 <= x <= 15 and 1 <=y <= 15:
        return not chess(x-2, y+1) or not chess(x-2, y-1) or not chess(x+1, y-2) or not chess(x-1, y-2)
    else:
        return True
    
T = int(input())
for _ in range(T):
    x, y = map(int, input().split(' '))
    print ("First" if chess(x, y) else "Second")
