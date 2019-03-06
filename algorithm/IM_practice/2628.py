row, col = map(int, input().split())
m = [[0] * row for _ in range(col)]
N = int(input())
for i in range(row):
    m[0][i] = 1
for i in range(col):
    m[i][0] = 1
for i in range(N):
    dct, idx = map(int, input().split())
    if dct:
        for j in range(col):
            m[j][idx] = 1
    else:
        for j in range(row):
            m[idx][j] = 1

cnt = []
for i in range(col):
    for j in range(row):
        if m[i][j] == 0:
            cnt_row, cnt_col = 0, 0
            y, x = i, j
            for k in range(x, row):
                if m[y][k] == 0:
                    cnt_row += 1
                else:
                    break
            for k in range(y, col):
                if m[k][x] == 0:
                    cnt_col += 1
                else:
                    break

            for k in range(y, y + cnt_col):
                for l in range(x, x + cnt_row):
                    m[k][l] = 2
            cnt.append((cnt_row + 1) * (cnt_col + 1))
print(max(cnt))