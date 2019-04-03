from collections import deque


def bfs(n):
    global N, cnt
    visited[n] = 1
    for i in range(1, N + 1):
        if m[n][i] and not visited[i]:
            cnt += 1
            visited[i] = 1
            queue.append((i, 1))

    while queue:
        friend, bridge = queue.popleft()
        if bridge >= 2:
            break
        for i in range(1, N + 1):
            if m[friend][i] and not visited[i]:
                cnt += 1
                visited[i] = 1
                queue.append((i, bridge + 1))


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    m = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        m[a][b] = 1
        m[b][a] = 1

    visited = [0] * (N + 1)
    queue = deque()
    cnt = 0
    bfs(1)
    print(f"#{tc} {cnt}")
