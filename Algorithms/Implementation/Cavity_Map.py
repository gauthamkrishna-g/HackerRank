n = int(input())
grid = []
grid_i = 0
for _ in range(n):
    grid.append(list(input()))
#print (grid)
i, j = 0, 0
for i in range(n):
    for j in range(n):
        if i >= 1 and i < n-1 and j >= 1 and j < n-1: 
            if grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1]:
                grid[i][j] = 'X'
for i in range(n):
    for j in range(n):
        print (grid[i][j], end='')
    print ()
