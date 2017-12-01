from collections import deque

n = int(input())
for a in range(1, n):
    row_vals = []
    for b in range(1, n):
        moves = 0
        board = [[False] * n for _ in range(n)]
        pos_queue = deque([(0, 0, 0)])
        while pos_queue:
            x, y, depth = pos_queue.pop()
            if not (0<=x<n and 0<=y<n) or board[y][x]:
                continue
            if (x, y) == (n-1, n-1):
                row_vals.append(depth)
                break
            board[y][x] = True
            d = depth+1
            pos_queue.extendleft([(x+a,y+b,d), (x-a,y+b,d), (x+a,y-b,d), (x-a,y-b,d), (x+b,y+a,d), (x-b,y+a,d), (x+b,y-a,d), (x-b,y-a,d)])
        if not pos_queue:
            row_vals.append(-1)
    print (*row_vals)
