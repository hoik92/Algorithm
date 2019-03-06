# import sys
# sys.stdin = open('input5097.txt', 'r')

def isEmpty():
    global front, rear
    return front == rear

def isFull():
    global front, rear, N
    return front == (rear + 1) % (N + 1)

def enQueue(i):
    global rear, N
    if not isFull():
        rear = (rear + 1) % (N + 1)
        queue[rear] = i

def deQueue():
    global front, N
    if not isEmpty():
        front = (front + 1) % (N + 1)
        i = queue[front]
        queue[front] = 0
        return i

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))

    # m = M % N
    # print(f"#{tc} {N_list[m]}")

    queue = [0] * (N + 1)
    front, rear = 0, 0

    for i in range(1, M+1):
        j = i % N
        if isFull():
            result = deQueue()
        enQueue(N_list[j])
    print(f"#{tc} {result}")