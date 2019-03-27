def find_min(n, depth, count):
    global N, min_sum
    if count > min_sum:
        return
    if depth == N:
        if count < min_sum:
            min_sum = count
        return
    elif depth == N - 1:
        find_min(0, depth + 1, count + m[n][0])
    else:
        for i in range(1, N):
            if i != n and not visited[i]:
                visited[i] = 1
                find_min(i, depth + 1, count + m[n][i])
                visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    visited = [0] * N

    min_sum = 100 * N
    find_min(0, 0, 0)
    print(f"#{tc} {min_sum}")
