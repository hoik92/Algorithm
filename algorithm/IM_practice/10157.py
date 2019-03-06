dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
C, R = map(int, input().split())
K = int(input())
if K > C * R:
    print(0)
else:
    m = [[0] * R for _ in range(C)]
    drt = 0
    x, y = 0, 0
    m[x][y] = 1
    for i in range(2, K + 1):
        if not (0 <= x + dx[drt] < C and 0 <= y + dy[drt] < R and not m[x + dx[drt]][y + dy[drt]]):
            drt = (drt + 1) % 4
        x += dx[drt]
        y += dy[drt]
        m[x][y] = i
    print(x + 1, y + 1)