def DFS_r(v):
    visited[v] = 1

    for i in range(1, V+1):
        if m[v][i] and not visited[i]:
            DFS_r(i)
            print(i, end=' ')

for tc in range(1, 11):
    V, E = map(int, input().split())
    E_list = list(map(int, input().split()))

    m = [[0] * (V+1) for _ in range(V+1)]
    input_degree = [0] * (V+1)
    visited = [0] * (V+1)

    for i in range(E):
        x, y = E_list[2 * i], E_list[2 * i + 1]
        m[y][x] = 1

    for i in range(1, V+1):
        for j in range(1, V+1):
            if m[i][j]:
                input_degree[j] += 1

    print(f"#{tc}", end=' ')
    for i in range(1, V+1):
        if not input_degree[i]:
            DFS_r(i)
            print(i, end=' ')
    print()