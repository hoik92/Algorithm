from collections import deque


def find(x, y, time):
    global N, M, L, cnt
    if time == L:
        return
    for i in range(4):
        tmpx, tmpy = x + tunnelx[m[x][y]][i], y + tunnely[m[x][y]][i]
        if 0 <= tmpx < N and 0 <= tmpy < M and not visited[tmpx][tmpy] and m[tmpx][tmpy] in possible[i]:
            visited[tmpx][tmpy] = 1
            cnt += 1
            find(tmpx, tmpy, time + 1)


def find_bfs():
    global N, M, L, cnt

    while q:
        x, y, time = q.popleft()
        if time == L:
            break
        for i in range(4):
            tmpx, tmpy = x + tunnelx[m[x][y]][i], y + tunnely[m[x][y]][i]
            if 0 <= tmpx < N and 0 <= tmpy < M and not visited[tmpx][tmpy] and m[tmpx][tmpy] in possible[i]:
                visited[tmpx][tmpy] = 1
                cnt += 1
                q.append((tmpx, tmpy, time + 1))


tunnelx = [0, [0, 1, 0, -1], [0, 1, 0, -1], [0, 0, 0, 0], [0, 0, 0, -1], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, -1]]
tunnely = [0, [1, 0, -1, 0], [0, 0, 0, 0], [1, 0, -1, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, -1, 0], [0, 0, -1, 0]]
possible = [[1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5], [1, 2, 5, 6]]
for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    visited = [[0] * M for _ in range(N)]
    cnt = 0

    q = deque()
    if m[R][C]:
        visited[R][C] = 1
        cnt += 1
        q.append((R, C, 1))
        # find(R, C, 1)
        find_bfs()
    print(f"#{tc} {cnt}")
