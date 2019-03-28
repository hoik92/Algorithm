def find_cost(depth, cost):
    global N, min_cost
    if cost >= min_cost:
        return
    if depth == N:
        if cost < min_cost:
            min_cost = cost
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find_cost(depth + 1, cost + m[depth][i])
            visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    min_cost = 0
    for i in range(N):
        m[i] = list(map(int, input().split()))
        min_cost += max(m[i])

    visited = [0] * N
    find_cost(0, 0)
    print(f"#{tc} {min_cost}")
