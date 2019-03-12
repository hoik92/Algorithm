def DFS(x, y):
    global result
    if m[x][y] == '3':
        result = 1
        return

    for i in range(4):
        if m[x + dx[i]][y + dy[i]] != '1' and not visited[x + dx[i]][y + dy[i]]:
            visited[x + dx[i]][y + dy[i]] = 1
            DFS(x + dx[i], y + dy[i])
            visited[x + dx[i]][y + dy[i]] = 0
            if result:
                return

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for t in range(10):
    tc = input()
    m = [0] * 16
    for i in range(16):
        m[i] = list(input())
    start_x, start_y = 1, 1
    visited = [[0] * 16 for _ in range(16)]

    visited[1][1] = 1
    result = 0
    DFS(start_x, start_y)
    print("#{} {}".format(tc, result))