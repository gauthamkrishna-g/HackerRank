def dfs(grid, start, end):
    if start in visited:
        return False
    visited.add(start)
    if start == end:
        return True
    found = False
    for node in grid[start]:
        found = dfs(grid, node, end)
        if found:
            path.append(node)
            return True
    return False

def grid_forest():
    grid = {}
    start, end = 0, 0
    for i in range(n):
        for j in range(m):
            cell = (i * m) + j
            grid[cell] = set()
            if forest[i][j] in (".", "M"):
                if forest[i][j] == "M":
                    start = cell                    
                for k in (-1, 1):
                    if 0 <= i+k < n and forest[i+k][j] in (".", "M", "*"):
                        grid[cell].add(((i+k) * m) + j)
                    if 0 <= j+k < m and forest[i][j+k] in (".", "M", "*"):
                        grid[cell].add((i * m) + j+k)
            elif forest[i][j] == "*":
                end = cell
    return grid, start, end                
    
t = int(input())
global path, visited
path, visited = [], set()

for _ in range(t):
    n, m = input().split(' ')
    n, m = int(n), int(m)
    forest = []
    for _ in range(n):
        forest.append([cell for cell in input()])
    grid, start, end = grid_forest()
    #print (grid)
    path = [start]
    visited.clear()
    dfs(grid, start, end)
    
    waves = 0
    for cell in reversed(path):
        if len(grid[cell]) > 2:
            waves += 1
        elif cell == start and len(grid[cell]) == 2:
            waves += 1
    K = int(input())            
    if waves == K:
        print ("Impressed")
    else:
        print ("Oops!")
