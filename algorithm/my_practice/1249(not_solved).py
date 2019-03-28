# import sys
# sys.stdin = open('input.txt', 'r')


def find_time(x, y, x_before, y_before):
    global N
    if x < 0 or x >= N or y < 0 or y >= N:
        return 10000000000

    if cost[x][y] == -1:
        tmp = []
        for i in range(4):
            tmpx = x + dx[i]
            tmpy = y + dy[i]
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and \
                    (x + dx[i] != x_before or y + dy[i] != y_before):
                if not visited[x + dx[i]][y + dy[i]]:
                    visited[tmpx][tmpy] = 1
                    tmp.append(find_time(x + dx[i], y + dy[i], x, y))
                    visited[tmpx][tmpy] = 0
                else:
                    tmp.append(1000000000001)
        # cost[x][y] = min([find_time(x, y - 1), find_time(x - 1, y)]) + int(m[x][y])
        cost[x][y] = min(tmp) + int(m[x][y])
    visited[x][y] = 1
    return cost[x][y]


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
for tc in range(1, int(input()) + 1):
    N = int(input())
    m = [0] * N
    for i in range(N):
        m[i] = list(input())
    visited = [[0] * N for _ in range(N)]
    cost = [[-1] * N for _ in range(N)]
    cost[0][0] = 0
    visited[N - 1][N - 1] = 1
    find_time(N - 1, N - 1, N - 1, N - 1)
    # print(f"#{tc} {min_time}")
    print(cost)
    print(visited)
    print(cost[N - 1][N - 1])
