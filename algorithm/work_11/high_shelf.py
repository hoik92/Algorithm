def find_min(idx, count):
    global N, B, min_sum
    if min_sum == B:
        return
    if B <= count:
        if count <= min_sum:
            min_sum = count
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            find_min(i, count + m[i])
            visited[i] = 0


for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    m = list(map(int, input().split()))
    S = 0
    for i in m:
        S += i

    min_sum = S
    visited = [0] * N
    find_min(0, 0)
    print(f"#{tc} {min_sum - B}")
