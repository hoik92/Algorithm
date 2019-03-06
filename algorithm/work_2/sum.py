import sys
sys.stdin = open('input.txt', 'r')

def max_result(arr):
    result = 0
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += arr[i][j]
        if tmp > result:
            result = tmp
    return result

for tc in range(10):
    T = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
    
    result_col = max_result(arr)

    for i in range(100):
        for j in range(100):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    result_row = max_result(arr)

    result_mat1 = 0
    result_mat2 = 0
    for i in range(100):
        result_mat1 += arr[i][i]
        result_mat2 += arr[i][99-i]
    
    if result_mat1 > result_mat2:
        result_mat = result_mat1
    else:
        result_mat = result_mat2

    if result_col > result_row:
        result = result_col
    else:
        result = result_row

    if result_mat > result:
        result = result_mat

    print(f"#{T} {result}")