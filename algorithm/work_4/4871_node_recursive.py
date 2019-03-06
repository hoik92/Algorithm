def DFS_r(S, G, ans):
    if S == G:
        return 1
    visited[S] = 1

    for i in range(1, V+1):
        if m[S][i] and not visited[i]:
            ans = DFS_r(i, G, ans)
    return ans

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    m = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        x, y = map(int, input().split())
        m[x][y] = 1

    S, G = map(int, input().split())
    ans = 0
    ans = DFS_r(S, G, ans)
    print(f"#{tc} {ans}")