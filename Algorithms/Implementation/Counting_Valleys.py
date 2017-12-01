n = int(input())
hike = input()

level = valley = 0
for i in range(n):
    if hike[i] == 'U':
        level += 1
    else:
        if level == 0:
            valley += 1
        level -= 1              
print (valley)