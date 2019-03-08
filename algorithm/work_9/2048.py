def left(m, N):
    for i in range(N):
        for j in range(N):
            if not m[i][j]:
                for k in range(j, N):
                    if not m[i][j]:
                        m[i].pop(j)
                        m[i].append(0)

    for i in range(N):
        for j in range(N - 1):
            if m[i][j] == m[i][j + 1]:
                m[i][j] += m[i][j + 1]
                m[i].pop(j + 1)
                m[i].append(0)
    return m

def right(m, N):
    for i in range(N):
        m[i] = m[i][::-1]
    return m

def up(m, N):
    for i in range(N):
        for j in range(N):
            if j > i:
                m[i][j], m[j][i] = m[j][i], m[i][j]
    return m

def down(m, N):
    for i in range(N):
        for j in range(N):
            if j > i:
                m[N - 1 - i][j], m[N - 1 - j][i] = m[N - 1 - j][i], m[N - 1 - i][j]
    return m

for tc in range(1, int(input())+1):
    N, S = input().split()
    N = int(N)
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    if S == 'left':
        m = left(m, N)
    elif S == 'right':
        m = right(m, N)
        m = left(m, N)
        m = right(m, N)
    elif S == 'up':
        m = up(m, N)
        m = left(m, N)
        m = up(m, N)
    else:
        m = down(m, N)
        m = left(m, N)
        m = down(m, N)
    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(m[i][j], end=' ')
        print()