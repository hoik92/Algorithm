from collections import deque


def find(x, y, K, depth):
    global N, M, cost, max_cnt, cnt
    q = deque()
    q.append((x, y, depth))
    while q:
        x, y, depth = q.popleft()
        if depth == K:
            break
        for i in range(4):
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and not visited[x + dx[i]][y + dy[i]]:
                visited[x + dx[i]][y + dy[i]] = 1
                if m[x + dx[i]][y + dy[i]]:
                    cnt += 1
                q.append((x + dx[i], y + dy[i], depth + 1))
    if cnt * M - cost >= 0 and cnt > max_cnt:
        max_cnt = cnt


# def akfmaah(x, y, k):
#     global N, M, cost, max_cnt, cnt
#     for i in range(k):
#         for j in range(k - i):


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    max_cnt = 1
    for k in range(2, N + 2):
        cost = k * k + (k - 1) * (k - 1)
        for i in range(N):
            for j in range(N):
                visited = [[0] * N for _ in range(N)]
                visited[i][j] = 1
                cnt = 0
                if m[i][j]:
                    cnt += 1
                find(i, j, k, 1)
    print(f"#{tc} {max_cnt}")
