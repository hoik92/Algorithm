# import sys
# sys.stdin = open('input.txt', 'r')


def find_max(depth, count):
    global N, max_p
    if count < max_p:
        return
    if depth == N:
        if count > max_p:
            max_p = count
        return
    for i in range(N):
        if p[depth][i] and not visited[i]:
            visited[i] = 1
            find_max(depth + 1, count * p[depth][i] / 100)
            visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    p = [0] * N
    for i in range(N):
        p[i] = list(map(int, input().split()))

    visited = [0] * N
    max_p = 0
    find_max(0, 1)
    print(f"#{tc} {(max_p * 100):.6f}")
