def find_idx():
    global N, M
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if m[i][j] == '1':
                return i, j


pattern = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    m = [0] * N

    for i in range(N):
        m[i] = input()

    row, col = find_idx()

    password = [0] * 8
    for i in range(8):
        tmp = m[row][col - 6:col + 1]
        for j in range(10):
            if tmp == pattern[j]:
                password[7 - i] = j
        col -= 7

    confirm, result = 0, 0
    for i in range(8):
        result += password[i]
        if i % 2:
            confirm += password[i]
        else:
            confirm += 3 * password[i]

    if confirm % 10:
        result = 0
    print(f"#{tc} {result}")
