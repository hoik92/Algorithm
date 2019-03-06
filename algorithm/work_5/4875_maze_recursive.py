import sys
sys.stdin = open('input4875.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS_r(x, y):
    global N
    global result
    if m[x][y] == 3:
        result = 1
        return
    visited[x][y] = 1

    for i in range(4):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and m[x+dx[i]][y+dy[i]] != 1 and not visited[x+dx[i]][y+dy[i]]:
            DFS_r(x + dx[i], y + dy[i])
            if result:
                return

for tc in range(1, int(input())+1):
    N = int(input())
    result = 0
    m = [[0] * N for _ in range(N)]
    for i in range(N):
        s = input()
        for j in range(N):
            m[i][j] = int(s[j])

    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if m[i][j] == 2:
                x, y = i, j
                break

    DFS_r(x, y)

    print(f"#{tc} {result}")