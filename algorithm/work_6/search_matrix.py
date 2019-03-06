import sys
sys.stdin = open('input.txt', 'r')

def search(cs, rs):
    global N
    c_cnt, r_cnt = 0, 0
    for i in range(cs, N):
        if m[i][rs]:
            c_cnt += 1
        else:
            break
    for i in range(rs, N):
        if m[cs][i]:
            r_cnt += 1
        else:
            break
    for i in range(cs, cs+c_cnt):
        for j in range(rs, rs+r_cnt):
            visited[i][j] = 1
    result.append([c_cnt * r_cnt, c_cnt, r_cnt])

for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))
    visited = [[0] * N for _ in range(N)]

    result = []

    for i in range(N):
        for j in range(N):
            if m[i][j] and not visited[i][j]:
                search(i, j)

    cnt = len(result)
    result = sorted(result)

    print(f"#{tc} {cnt}", end=' ')
    for i in range(cnt):
        print(result[i][1], result[i][2], end=' ')
    print()