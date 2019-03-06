def enQueue(v):
    global front, rear
    rear += 1
    queue[rear] = v

def deQueue():
    global front, rear
    front += 1
    n = queue[front]
    queue[front] = 0
    return n

def BFS(v):
    global front, rear
    enQueue(v)
    # visited[v] = 1
    while front != rear:
        print(queue)
        v = deQueue()
        # print(v, end=' ')
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
        for i in G[v]:
            if not visited[i]:
                enQueue(i)
                # visited[i] = 1


N = 7
visited = [0] * (N+1)
queue = [0] * 100
front, rear = -1, -1

G = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]

BFS(1)