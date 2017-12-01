def dfs(s):
    global visited, edges, croad, cost
    visited[s] = 1
    edge_len = len(edges[s])
    if edge_len != 0:
        for i in range(edge_len):
            if (visited[edges[s][i]]) == 0:
                dfs(edges[s][i])
                cost += croad
                
q = int(input())
for _ in range(q):
    n, m, clib, croad = input().split(' ')
    n, m, clib, croad = int(n), int(m), int(clib), int(croad)
    cost = 0
    visited = [0 for _ in range(n+1)]
    edges = {i:[] for i in range(n+1)}
    for _ in range(m):
        city_1, city_2 = map(int, input().split(' '))
        edges[city_1].append(city_2)
        edges[city_2].append(city_1)
        
    if m == 0 or croad > clib:
        print (n * clib)
    else:
        for i in range(1, n+1):
            if visited[i] == 0:
                dfs(i)
                cost += clib
        print (cost)