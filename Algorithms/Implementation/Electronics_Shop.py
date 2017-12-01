s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = [int(keyboards_temp) for keyboards_temp in input().strip().split(' ')]
pendrives = [int(pendrives_temp) for pendrives_temp in input().strip().split(' ')]

max_cost = -1
for i in range(n):
    for j in range(m):
        cost = keyboards[i] + pendrives[j]
        if  cost <= s and cost > max_cost:
            max_cost = cost
print (max_cost)     