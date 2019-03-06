m = [0] * 5
an = [0] * 5
for i in range(5):
    m[i] = list(map(int, input().split()))
for i in range(5):
    an[i] = list(map(int, input().split()))

cnt, result = 0, 0
flag = False
bingo, bingo_cnt = 0, 0
for i in range(5):
    for j in range(5):
        tmp = an[i][j]
        for k in range(5):
            for l in range(5):
                if m[k][l] == tmp:
                    m[k][l] = 0
                    cnt += 1
                    flag = True
                    break
            if flag:
                flag = False
                break
        if cnt > 10:
            for k in range(5):
                if m[k][0] == 0:
                    bingo_cnt += 1
                    for l in range(1, 5):
                        if m[k][l] == 0:
                            bingo_cnt += 1
                    if bingo_cnt == 5:
                        bingo += 1
                    bingo_cnt = 0
                if m[0][k] == 0:
                    bingo_cnt += 1
                    for l in range(1, 5):
                        if m[l][k] == 0:
                            bingo_cnt += 1
                    if bingo_cnt == 5:
                        bingo += 1
                    bingo_cnt = 0
            if m[0][0] == 0:
                bingo_cnt += 1
                for k in range(1, 5):
                    if m[k][k] == 0:
                        bingo_cnt += 1
                if bingo_cnt == 5:
                    bingo += 1
                bingo_cnt = 0
            if m[4][0] == 0:
                bingo_cnt += 1
                for k in range(1, 5):
                    if m[4 - k][k] == 0:
                        bingo_cnt += 1
                if bingo_cnt == 5:
                    bingo += 1
                bingo_cnt = 0
        if bingo == 3:
            result = cnt
            break
        else:
            bingo = 0
    if result:
        break

print(result)