def rotation(m):
    global N
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][N-1-i] = m[i][j]
    return result

for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    m_90 = rotation(m)
    m_180 = rotation(m_90)
    m_270 = rotation(m_180)

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            print(m_90[i][j], end='')
        print('', end=' ')
        for j in range(N):
            print(m_180[i][j], end='')
        print('', end=' ')
        for j in range(N):
            print(m_270[i][j], end='')
        print()