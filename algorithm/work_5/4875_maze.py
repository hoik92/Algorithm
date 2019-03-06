import sys
sys.stdin = open('input4875.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    m = [[0] * N for _ in range(N)]
    for i in range(N):
        s = input()
        for j in range(N):
            m[i][j] = int(s[j])

    stack = [0] * (N * N)
    top = -1
    visited = [[0] * N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(N):
        if m[0][i] == 3:
            x, y = 0, i
            visited[0][i] = 1
            # top += 1
            # stack[top] = x, y
            break

    result = 1
    while m[x][y] != 2 and result:
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and m[x+dx[i]][y+dy[i]] != 1 and not visited[x+dx[i]][y+dy[i]]:
                visited[x+dx[i]][y+dy[i]] = 1
                top += 1
                stack[top] = x, y
                x += dx[i]
                y += dy[i]

                break
            if i == 3:
                if top != -1:
                    x, y = stack[top]
                    top -= 1
                else:
                    result = 0

    print(f"#{tc} {result}")