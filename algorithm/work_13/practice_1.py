def DFS_re(n):
    print(n, end=' ')

    for i in m:
        if i[0] == n and not visited[i[1]]:
            visited[i[1]] = 1
            DFS_re(i[1])
        elif i[1] == n and not visited[i[0]]:
            visited[i[0]] = 1
            DFS_re(i[0])


def DFS(n):
    stack = [n]
    while len(stack):
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for i in m:
                if i[0] == v and not visited[i[1]]:
                    stack.append(i[1])
                elif i[1] == v and not visited[i[0]]:
                    stack.append(i[0])


iinnppuutt = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
N = len(iinnppuutt)
m = [0] * (N // 2)
visited = [0] * (N // 2 + 1)

for i in range(N // 2):
    m[i] = (iinnppuutt[2 * i], iinnppuutt[2 * i + 1])

# visited[1] = 1
# DFS_re(1)
DFS(1)
