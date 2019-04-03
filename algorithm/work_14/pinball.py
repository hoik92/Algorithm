def pinball(x, y, drt):
    global N, cnt
    startx, starty = x, y
    tmpx, tmpy = x, y
    while True:
        tmpx, tmpy = tmpx + dx[drt], tmpy + dy[drt]
        if (tmpx, tmpy) == (startx, starty):
            break
        if tmpx == N:
            drt = 3
            cnt += 1
            continue
        elif tmpx == -1:
            drt = 1
            cnt += 1
            continue
        if tmpy == N:
            drt = 2
            cnt += 1
            continue
        elif tmpy == -1:
            drt = 0
            cnt += 1
            continue
        if m[tmpx][tmpy] == 1:
            if drt == 0:
                drt = 2
            elif drt == 3:
                drt = 1
            elif drt == 1:
                drt = 0
            else:
                drt = 3
            cnt += 1
        elif m[tmpx][tmpy] == 2:
            if drt == 0:
                drt = 2
            elif drt == 1:
                drt = 3
            elif drt == 2:
                drt = 1
            else:
                drt = 0
            cnt += 1
        elif m[tmpx][tmpy] == 3:
            if drt == 2:
                drt = 0
            elif drt == 1:
                drt = 3
            elif drt == 0:
                drt = 1
            else:
                drt = 2
            cnt += 1
        elif m[tmpx][tmpy] == 4:
            if drt == 2:
                drt = 0
            elif drt == 3:
                drt = 1
            elif drt == 0:
                drt = 3
            else:
                drt = 2
            cnt += 1
        elif m[tmpx][tmpy] == 5:
            if drt == 0:
                drt = 2
            elif drt == 1:
                drt = 3
            elif drt == 2:
                drt = 0
            else:
                drt = 1
            cnt += 1
        elif m[tmpx][tmpy] == -1:
            break
        elif m[tmpx][tmpy] > 5:
            if (tmpx, tmpy) == hole[m[tmpx][tmpy]][0]:
                tmpx, tmpy = hole[m[tmpx][tmpy]][1]
            else:
                tmpx, tmpy = hole[m[tmpx][tmpy]][0]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, int(input())+1):
    N = int(input())
    m = [[0] * N for _ in range(N)]
    for i in range(N):
        m[i] = list(map(int, input().split()))

    hole = [0] * 11
    for i in range(N):
        for j in range(N):
            if m[i][j] > 5:
                if hole[m[i][j]]:
                    hole[m[i][j]] = [hole[m[i][j]], (i, j)]
                else:
                    hole[m[i][j]] = (i, j)

    max_cnt = 0
    for i in range(N):
        for j in range(N):
            if m[i][j] == 0:
                for k in range(4):
                    cnt = 0
                    pinball(i, j, k)
                    if cnt > max_cnt:
                        max_cnt = cnt
    print(f"#{tc} {max_cnt}")
