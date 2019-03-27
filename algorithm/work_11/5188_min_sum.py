def find_min(x, y, count):
    global min_sum, N
    if (x, y) == (N - 1, N - 1):
        if count < min_sum:
            min_sum = count
        return
    if count > min_sum:
        return

    for i in range(2):
        if x + dx[i] < N and y + dy[i] < N:
            find_min(x + dx[i], y + dy[i], count + m[x + dx[i]][y + dy[i]])


dx = [0, 1]
dy = [1, 0]
for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    min_sum = 10 * (N * N)
    find_min(0, 0, m[0][0])

    print(f"#{tc} {min_sum}")
