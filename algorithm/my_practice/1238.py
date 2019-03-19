def BFS():
    global n, max_cnt, max_num

    while len(queue) != 0:
        cnt, s = queue.pop(0)
        if cnt > max_cnt:
            max_cnt = cnt
            max_num = s
        elif cnt == max_cnt and s > max_num:
            max_num = s
        for i in range(n):
            if m[i][0] == s and not visited[m[i][1]]:
                visited[m[i][1]] = 1
                queue.append((cnt + 1, m[i][1]))


for tc in range(1, 11):
    N, start = map(int, input().split())
    M = list(map(int, input().split()))

    n = N // 2
    m = [0] * n
    visited = [0] * 101
    visited[start] = 1
    for i in range(n):
        m[i] = [M[2 * i], M[2 * i + 1]]

    queue = []
    max_cnt, max_num = 0, 0
    for i in range(n):
        if m[i][0] == start:
            visited[m[i][1]] = 1
            queue.append((1, m[i][1]))
            BFS()
            break
    print(f"#{tc} {max_num}")
