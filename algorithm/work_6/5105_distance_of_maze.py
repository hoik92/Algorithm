dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global result, cnt, N

    if m[x][y] == '3':
        cnt -= 1
        result = 1
        return
    visited[x][y] = 1
    for i in range(4):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and m[x+dx[i]][y+dy[i]] != '1' and not visited[x+dx[i]][y+dy[i]]:
            DFS(x + dx[i], y + dy[i])
            cnt += 1
            if result:
                return
            cnt -= 1
    visited[x][y] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        m[i] = list(input())

    for i in range(N):
        for j in range(N):
            if m[i][j] == '2':
                x, y = i, j
                break

    result, cnt = 0, 0
    DFS(x, y)

    print(f"#{tc} {cnt}")