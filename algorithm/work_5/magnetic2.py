import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    m = [0] * N
    cnt = 0
    for i in range(N):
        m[i] = list(map(int, input().split()))

    for i in range(N):
        for j in range(N):
            if m[N-1-i][j] == 1:
                idx = N-1 - i
                while idx < N-1 and not m[idx+1][j]:
                    m[idx][j] = 0
                    m[idx+1][j] = 1
                    idx += 1
                if idx != N-1 and m[idx+1][j] == 2:
                    cnt += 1

    print(f"#{tc} {cnt}")