from copy import deepcopy

r, c, n = input().strip().split(' ')
r, c, n = int(r), int(c), int(n)
grid = [[x for x in input()] for _ in range(r)]
#print (grid)

def new_grid(ar_in):
    bomb_grid_temp = deepcopy(bomb_grid)
    for i in range(r):
        for j in range(c):
            if ar_in[i][j] == "O":
                for pos in range(max(0, i-1), min(r, i+2)):
                    bomb_grid_temp[pos][j] = "."
                for pos in range(max(0, j-1), min(j+2, c)):
                    bomb_grid_temp[i][pos] = "."
    return bomb_grid_temp                    

bomb_grid = [['O' for _ in range(c)] for _ in range(r)]
seconds = [[] for _ in range(6)]
seconds[0] = seconds[1] = grid
seconds[2] = seconds[4] = bomb_grid
seconds[3] = deepcopy(new_grid(seconds[1]))
seconds[5] = deepcopy(new_grid(seconds[3]))

if n > 5:
    if n % 2 == 0:
        n = 2
    elif n % 4 == 3:
        n = 3
    elif n % 4 == 1:
        n = 5

for t in seconds[n]:
    print ("".join(t))
