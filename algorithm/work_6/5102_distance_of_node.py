def isEmpty():
    global front, rear
    return front == rear

def isFull():
    global rear, V
    return rear == V * V - 1

def enQueue(i):
    global rear
    if not isFull():
        rear += 1
        queue[rear] = i

def deQueue():
    global front
    if not isEmpty():
        front += 1
        i = queue[front]
        queue[front] = 0
        return i
    else:
        return [-1, 0]

def BFS(S):
    global G, V, result
    cnt = 0
    while S != G and S != -1:
        if not visited[S]:
            visited[S] = 1
            cnt += 1
        for i in range(1, V + 1):
            if m[S][i] and not visited[i]:
                enQueue([i, cnt])
        n = deQueue()
        S, cnt = n[0], n[1]
    return cnt


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    m = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    result, cnt = 0, 0

    queue = [0] * (V * V)
    front, rear = -1, -1

    for i in range(E):
        x, y = map(int, input().split())
        m[x][y], m[y][x] = 1, 1

    S, G = map(int, input().split())
    cnt = BFS(S)
    print(f"#{tc} {cnt}")