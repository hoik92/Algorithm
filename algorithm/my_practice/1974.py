def find_row(arr):
    global result
    count = [0] * 10
    for i in range(9):
        if not count[arr[i]]:
            count[arr[i]] += 1
        else:
            result = 0
            return


def find_col(col):
    global result
    count = [0] * 10
    for i in range(9):
        if not count[m[i][col]]:
            count[m[i][col]] += 1
        else:
            result = 0
            return


def find_mat(x, y):
    global result
    count = [0] * 10
    for i in range(3):
        for j in range(3):
            if not count[m[x + i][y + j]]:
                count[m[x + i][y + j]] += 1
            else:
                result = 0
                return


for tc in range(1, int(input())+1):
    m = [0] * 9
    for i in range(9):
        m[i] = list(map(int, input().split()))
    result = 1
    for i in range(9):
        if result:
            find_row(m[i])
            find_col(i)
        else:
            break

    for i in range(3):
        for j in range(3):
            if result:
                find_mat(3 * i, 3 * j)
            else:
                break
    print("#{} {}".format(tc, result))
