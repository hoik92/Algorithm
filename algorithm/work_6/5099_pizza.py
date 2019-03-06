def enQueue(i):
    global rear
    if queue[rear] == 0:
        queue[rear] = i

def deQueue():
    global rear, N, result
    rear = (rear + 1) % N
    n = queue[rear]
    if n != 0:
        C[n[0]][1] = C[n[0]][1] // 2
        if C[n[0]][1] == 0:
            result = n[0]
            queue[rear] = 0
        else:
            queue[rear] = 0
            enQueue(C[n[0]])

def pizza():
    global rear, N, idx, M, flag

    if idx != M and queue[rear] == 0:
        enQueue(C[idx])
        idx += 1
    deQueue()
    if idx == M:
        cnt = 0
        for i in range(N):
            if queue[i] == 0:
                cnt += 1
        if cnt == N:
            flag = 1
            return



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    result, idx = -1, 0
    flag = 0

    queue = [0] * N
    rear = 0

    for i in range(M):
        C[i] = [i, C[i]]
    # print(C)
    while not flag:
        pizza()
        # print(idx, rear, queue)

    print(f"#{tc} {result + 1}")