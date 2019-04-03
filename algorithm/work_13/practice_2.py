iinnppuutt = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
N = len(iinnppuutt) // 2
m = [[] for _ in range(N + 1)]
for i in range(N):
    m[iinnppuutt[2 * i]].append(iinnppuutt[2 * i + 1])
    m[iinnppuutt[2 * i + 1]].append(iinnppuutt[2 * i])

visited = [0] * (N + 1)
visited[1] = 1
queue = [1]

while queue:
    v = queue.pop(0)
    print(v, end=' ')
    for i in m[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = 1
