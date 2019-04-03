def greedy():
    global N
    tmp_cookie = [0] * N
    tmp_robot = [0] * N
    for i in range(N):
        tmp_cookie[i] = cookie[i][0] + cookie[i][1]
        tmp_robot[i] = robot[i][0] + robot[i][1]
    tmp = 0
    for i in range(N):
        max_cookie, max_robot = 200, 200
        idx_cookie, idx_robot = 0, 0
        for j in range(N):
            if tmp_cookie[j] < max_cookie:
                max_cookie = tmp_cookie[j]
                idx_cookie = j
            if tmp_robot[j] < max_robot:
                max_robot = tmp_robot[j]
                idx_robot = j
        tmp += abs(robot[idx_robot][0] - cookie[idx_cookie][0]) + abs(robot[idx_robot][1] - cookie[idx_cookie][1])
        tmp_cookie[idx_cookie], tmp_robot[idx_robot] = 200, 200
    return tmp


def find(depth, count):
    global N, min_val
    if count >= min_val:
        return
    if depth == N:
        if count < min_val:
            min_val = count
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find(depth + 1, count + abs(robot[i][0] - cookie[depth][0]) + abs(robot[i][1] - cookie[depth][1]))
            visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    m = list(map(int, input().split()))
    n = list(map(int, input().split()))
    cookie = [0] * N
    robot = [0] * N
    for i in range(N):
        cookie[i] = (m[2 * i], m[2 * i + 1])
        robot[i] = (n[2 * i], n[2 * i + 1])
    visited = [0] * N
    min_val = greedy()
    find(0, 0)
    print(f"#{tc} {min_val}")
