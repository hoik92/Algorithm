# def DFS(x, y):
#     global max_height
#     visited[x][y] = 1
#     if m[x][y] > max_height:
#         max_height = m[x][y]
#     for i in range(4):
#         if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and \
#                 m[x + dx[i]][y + dy[i]] and not visited[x + dx[i]][y + dy[i]]:
#             DFS(x + dx[i], y + dy[i])

def BFS():
    global max_height
    while len(queue):
        x, y = queue.pop(0)
        if m[x][y] > max_height:
            max_height = m[x][y]
        for i in range(4):
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and \
                    m[x + dx[i]][y + dy[i]] and not visited[x + dx[i]][y + dy[i]]:
                queue.append((x + dx[i], y + dy[i]))
                visited[x + dx[i]][y + dy[i]] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))
    visited = [[0] * N for _ in range(N)]

    cnt, max_height = 0, 0
    queue = []
    for i in range(N):
        for j in range(N):
            if m[i][j] and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = 1
                BFS()
                # DFS(i, j)
                cnt += 1
    print("#{} {} {}".format(tc, cnt, max_height))