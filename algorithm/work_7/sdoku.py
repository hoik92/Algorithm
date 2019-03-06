for tc in range(1, int(input())+1):
    m = [0] * 9
    for i in range(9):
        m[i] = list(map(int, input().split()))

    result = 1
    for i in range(9):
        if not result:
            break
        cnt_row = [0] * 10
        cnt_col = [0] * 10
        for j in range(9):
            if cnt_row[m[i][j]] == 0:
                cnt_row[m[i][j]] += 1
            else:
                result = 0
                break

            if cnt_col[m[j][i]] == 0:
                cnt_col[m[j][i]] += 1
            else:
                result = 0
                break

    for i in range(3):
        if not result:
            break
        for j in range(3):
            if not result:
                break
            cnt_mat = [0] * 10
            for k in range(3):
                for l in range(3):
                    if cnt_mat[m[3 * i + k][3 * j + l]] == 0:
                        cnt_mat[m[3 * i + k][3 * j + l]] += 1
                    else:
                        result = 0
                        break
    print("#{} {}".format(tc, result))