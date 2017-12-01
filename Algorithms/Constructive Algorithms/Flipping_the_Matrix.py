q = int(input())
for _ in range(q):
    n = int(input())
    matrix = [[int(matrix_temp) for matrix_temp in input().split(' ')] for _ in range(2*n)]
    max_sum = 0
    for i in range(n):
        for j in range(n):
            max_sum += max(matrix[i][j], matrix[i][2*n-j-1], matrix[2*n-i-1][j], matrix[2*n-i-1][2*n-j-1])
    print (max_sum)
