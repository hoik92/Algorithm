dx = [-3, -3, -2, 2, 3, 3, 2, -2]
dy = [2, -2, 3, 3, 2, -2, -3, -3]
for tc in range(1, int(input())+1):
    N = int(input())
    x, y, lastx, lasty = map(int, input().split())
    queue = []
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    count = 0
    if (x, y) == (lastx, lasty):
        print(f"#{tc} {count}")
        continue

    for i in range(8):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and not visited[x + dx[i]][y + dy[i]]:
            visited[x + dx[i]][y + dy[i]] = 1
            queue.append((x + dx[i], y + dy[i], 1))

    while len(queue):
        x, y, count = queue.pop(0)
        if (x, y) == (lastx, lasty):
            break
        for i in range(8):
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and not visited[x + dx[i]][y + dy[i]]:
                visited[x + dx[i]][y + dy[i]] = 1
                queue.append((x + dx[i], y + dy[i], count + 1))
    print(f"#{tc} {count}")
