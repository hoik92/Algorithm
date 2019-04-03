def find_min(d):
    N = len(d)
    min_val = 100
    idx = 0
    for i in range(N):
        if d[i] <= min_val and not visited[i]:
            min_val = d[i]
            idx = i
    return idx


n = 7
m = [[100] * n for _ in range(n)]
m[0][1] = 32
m[1][0] = 32
m[0][2] = 31
m[2][0] = 31
m[0][5] = 60
m[5][0] = 60
m[0][6] = 51
m[6][0] = 51
m[1][2] = 21
m[2][1] = 21
m[2][4] = 46
m[4][2] = 46
m[2][6] = 25
m[6][2] = 25
m[3][4] = 34
m[4][3] = 34
m[3][5] = 18
m[5][3] = 18
m[4][6] = 51
m[6][4] = 51
m[4][5] = 40
m[5][4] = 40
for i in range(n):
    m[i][i] = 0

visited = [0] * n
visited[0] = 1
d = m[0][:]
while True:
    idx = find_min(d)
    visited[idx] = 1
    cnt = 0
    for i in range(1, n):
        if visited[i]:
            cnt += 1
        else:
            break
    if cnt == n - 1:
        break

    for i in range(1, n):
        if m[idx][i] != 100 and not visited[i]:
            if d[i] > m[idx][i]:
                d[i] = m[idx][i]
print(d)
# [(12, 1, 7), (13, 4, 7), (17, 1, 5), (20, 3, 5), (24, 2, 4), (37, 3, 6)]
