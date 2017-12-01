p = []
for s_i in range(3):
    s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
    p.append(s_t)
#print (p)   
s = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [8, 3, 4, 1, 5, 9, 6, 7, 2], [2, 7, 6, 9, 5, 1, 4, 3, 8],
     [2, 9, 4, 7, 5, 3, 6, 1, 8], [6, 1, 8, 7, 5, 3, 2, 9, 4], [6, 7, 2, 1, 5, 9, 8, 3, 4],
     [4, 3, 8, 9, 5, 1, 2, 7, 6], [4, 9, 2, 3, 5, 7, 8, 1, 6]]

min_cost = [] 
for i in range(8):
    min_cost.append(0) 
    for j in range(9): 
        min_cost[i] += abs(s[i][j] - p[int(j//3)][j%3]) 
print (min(min_cost))
