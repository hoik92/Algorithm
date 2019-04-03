def dfs(x, y, s, cnt):
    if cnt == 7:
        if not result.get(s):
            result[s] = 1
        return

    for i in range(4):
        if 0 <= x + dx[i] < 4 and 0 <= y + dy[i] < 4:
            dfs(x + dx[i], y + dy[i], s + m[x + dx[i]][y + dy[i]], cnt + 1)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, int(input())+1):
    m = [0] * 4
    for i in range(4):
        m[i] = input().split()

    result = {}
    for i in range(4):
        for j in range(4):
            dfs(i, j, m[i][j], 1)
    print(f"#{tc} {len(result)}")
