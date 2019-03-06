def DFS_r(v):
    print(v)
    visited[v] = 1

    for i in range(1, V+1):
        if m[v][i] and not visited[i]:
            DFS_r(i)

V = 7
m = [[0] * (V+1) for i in range(V+1)]

visited = [0] * (V+1)

E_list = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
E = len(E_list) // 2
for i in range(E):
    x, y = E_list[2 * i], E_list[2 * i + 1]
    m[x][y], m[y][x] = 1, 1

DFS_r(1)