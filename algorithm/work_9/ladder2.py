import sys
sys.stdin = open('input.txt', 'r')

dx = [1, -1]
def ladder(n):
    global min_distance, min_idx, N
    idx = n
    cnt = 0
    for k in range(N):
        cnt += 1
        for j in range(2):
            if 0 <= n + dx[j] < N and m[k][n + dx[j]]:
                while 0 <= n + dx[j] < N and m[k][n + dx[j]]:
                    cnt += 1
                    n += dx[j]
                break
    if min_distance > cnt:
        min_distance = cnt
        min_idx = idx

for tc in range(1, 11):
    t = input()
    N = 100
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    min_distance = N * N
    min_idx = 0
    for i in range(N):
        if m[0][i]:
            ladder(i)
    print("#{} {}".format(tc, min_idx))