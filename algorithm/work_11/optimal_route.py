def find_route(location, count, depth):
    global N, min_route
    if count >= min_route:
        return
    if depth == N + 1:
        if count < min_route:
            min_route = count
        return
    elif depth == N:
        find_route(location, count + abs(location[0] - loca[1][0]) + abs(location[1] - loca[1][1]), depth + 1)
    else:
        for i in range(2, N + 2):
            if not visited[i]:
                visited[i] = 1
                find_route(loca[i], count + abs(location[0] - loca[i][0]) + abs(location[1] - loca[i][1]), depth + 1)
                visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    m = list(map(int, input().split()))
    loca = [0] * (N + 2)
    for i in range(N + 2):
        loca[i] = (m[2 * i], m[2 * i + 1])

    visited = [0] * (N + 2)
    min_route = 100 * (N + 2)
    find_route(loca[0], 0, 0)
    print(f"#{tc} {min_route}")
