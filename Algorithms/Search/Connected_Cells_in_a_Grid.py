n = int(input())
m = int(input())
mat = [[int(j) for j in input().split()] for i in range(n)]

def flood_fill(i, j):
    if i >= n or j >= m or i < 0 or j < 0 or mat[i][j] == 0 or mat[i][j] == -1:
        return 0
    else:
        mat[i][j] = -1
        return 1 + flood_fill(i-1, j-1) + flood_fill(i-1, j) + flood_fill(i-1, j+1) + flood_fill(i, j-1) + flood_fill(i, j+1) + flood_fill(i+1, j-1) + flood_fill(i+1, j) + flood_fill(i+1, j+1)
        
print (max(flood_fill(i, j) for i in range(n) for j in range(m)))