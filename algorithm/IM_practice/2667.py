def DFS(x, y):
    global house_cnt, N
    visited[x][y] = 1
    house_cnt += 1
    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and \
                not visited[x + dx[i]][y + dy[i]] and m[x + dx[i]][y + dy[i]] == '1':
            DFS(x + dx[i], y + dy[i])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
m = [0] * N
for i in range(N):
    m[i] = list(input())
visited = [[0] * N for _ in range(N)]
house = []
neighbor_cnt = 0

for i in range(N):
    for j in range(N):
        if m[i][j] == '1' and not visited[i][j]:
            house_cnt = 0
            DFS(i, j)
            house.append(house_cnt)
            neighbor_cnt += 1

house.sort()
print(neighbor_cnt)
for i in range(neighbor_cnt):
    print(house[i])