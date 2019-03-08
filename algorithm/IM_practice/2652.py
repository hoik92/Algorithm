def find_e(x, y):
    global N
    visited[x][y] = 1
    col_cnt, row_cnt = 1, 1
    flag = 0
    while True:
        if x + 1 < N and m[x + 1][y] == 1

N = int(input())
u, v, w, x, y = map(int, input().split())
m = [0] * N
for i in range(N):
    m[i] = list(map(int, input().split()))

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if m[i][j] and not visited[i][j]:
            find_e(i, j)